import subprocess
from utils.tools import *


repo_id = {'test' : 'beomi/Llama-3-Open-Ko-8B',
            'LLaMA3' : "meta-llama/Llama-3-8B-Instruct",
            'Mistral7B' : 'mistralai/Mistral-7B-v0.1',
            'EXAONE': 'LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct',
            "LLAVA-v1" : "mys/ggml_llava-v1.5-7b"}

selected_values = {'model' : 'LLaMA3.1', 'qt' : 'q8_0'}


def download_model_mac(info):
    try:
        from huggingface_hub import snapshot_download
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'huggingface_hub'])
        from huggingface_hub import snapshot_download
    # name = repo_id[info['llm']]
    name = repo_id[info['lmm']]

    repo = name.split('/')
    model_dir, gguf_name = repo[-1], repo[-1] + '.gguf'
    model_path = '../models/'
    llama_dir = '../llama.cpp/'
    # if not check_dir(os.path.join(model_path, model_dir)):
    #     snapshot_download(repo_id = name, local_dir = os.path.join(model_path, model_dir), 
    #                       local_dir_use_symlinks = False, revision = 'main')
    
    # if not check_dir(llama_dir):
    #     subprocess.run(['git', 'clone', 'https://github.com/ggerganov/llama.cpp.git', '../llama.cpp'])
    #     subprocess.run(['make', '-C', '../llama.cpp/'])
    #     subprocess.run(['pip', 'install', '-r', '../llama.cpp/requirements.txt'])
    
    
    # if not check_file(os.path.join(llama_dir, 'models/', gguf_name)):
    #     subprocess.run(['python', os.path.join(llama_dir, 'convert_hf_to_gguf.py'), 
    #                     os.path.join(model_path, model_dir), '--outfile', gguf_name, 
    #                     '--outtype', info['qt']])
    
    #     subprocess.run(['mv', gguf_name, os.path.join(llama_dir, 'models/')])


    if info['mode'] == 'Basic':
        subprocess.run(['../llama.cpp/llama-cli', '-m', os.path.join(llama_dir, 'models/', gguf_name), 
                        '-p', "I believe the meaning of life is", '-n', '128'])
    elif info['mode'] == 'Conversation':
        subprocess.run(['../llama.cpp/llama-cli', '-m', os.path.join(llama_dir, 'models/', gguf_name), 
                        '-p', "I believe the meaning of life is", '-cnv'])
    else:
        subprocess.run(['../llama.cpp/llama-llava-cli', '-m', "../llava-v1.5-7b/ggml-model-q4_k.gguf", 
                        '--mmproj', '../llava-v1.5-7b/mmproj-model-f16.gguf', '--image', '../llama.cpp/2.png', '-p', 
                        "Explain the traffic situation around you"])

def download_model_win(info):
    try:
        from huggingface_hub import snapshot_download
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'huggingface_hub'])
        from huggingface_hub import snapshot_download
    name = repo_id[info['model']]

    repo = name.split('/')
    model_dir, gguf_name = repo[-1], repo[-1] + '.gguf'
    model_path = '../models'
    llama_dir = '../llama.cpp'
    if not check_dir(os.path.join(model_path, model_dir)):
        snapshot_download(repo_id = name, local_dir = os.path.join(model_path, model_dir), 
                          local_dir_use_symlinks = False, revision = 'main')
    
    if not check_dir(llama_dir):
        subprocess.run(['git', 'clone', 'https://github.com/ggerganov/llama.cpp.git', '..\llama.cpp'])
        os.mkdir('../llama.cpp/build')
        subprocess.run(['cmake', '-S', '../llama.cpp/', '-B', '../llama.cpp/build'])
        subprocess.run(['cmake', '--build', '../llama.cpp/build', '--config', 'Release'])
        subprocess.run(['move', '..\\llama.cpp\\build\\bin\\Release\\*', '..\\llama.cpp'], shell=True)
        subprocess.run(['pip', 'install', '-r', '../llama.cpp/requirements.txt'])
    
    if not check_file(os.path.join(llama_dir, 'models', gguf_name)):
        subprocess.run(['python', os.path.join(llama_dir, 'convert_hf_to_gguf.py'), 
                        os.path.join(model_path, model_dir), '--outfile', gguf_name, 
                        '--outtype', info['qt']], shell= True)
    
        subprocess.run(['move', gguf_name, os.path.join(llama_dir, 'models/')], shell = True)
    
    if info['mode'] == 'Basic':
        subprocess.run(['../llama.cpp/llama-cli', '-m', os.path.join(llama_dir, 'models/', gguf_name), 
                        '-p', "I believe the meaning of life is", '-n', '128'])
    elif info['mode'] == 'Conversation':
        subprocess.run(['../llama.cpp/llama-cli', '-m', os.path.join(llama_dir, 'models/', gguf_name), 
                        '-p', "I believe the meaning of life is", '-cnv'])
