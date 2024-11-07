import sys, os
from tkinter import *
from tkinter import ttk
import subprocess


repo_id = {'test' : 'beomi/Llama-3-Open-Ko-8B',
            'LLaMA3.1' : "meta-llama/Llama-3.1-8B",
            'Mistral7B' : 'mistralai/Mistral-7B-v0.1',
            'EXAONE': 'LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct'}

selected_values = {'model' : 'LLaMA3.1', 'qt' : 'q8_0'}

def download_model():
    try:
        from huggingface_hub import snapshot_download
    except:
        subprocess.check_call([sys.executable, '-m', 'pip', 'intall', '--upgrade', 'huggingface_hub'])
        from huggingface_hub import snapshot_download
    name = repo_id[selected_values['model']]

    repo = name.split('/')
    model_dir, gguf_name = repo[-1], repo[-1] + '.gguf'
    model_path = '../models/'
    if not os.path.isdir(os.path.join(model_path, model_dir)):
        snapshot_download(repo_id = name, local_dir = os.path.join(model_path, model_dir), 
                          local_dir_use_symlinks = False, revision = 'main')
    # print("Check llama.cpp")
    # subprocess.run(['git', 'clone', 'https://github.com/ggerganov/llama.cpp.git', '../llama.cpp'])
    # print("make")
    # subprocess.run(['make', '-C', '../llama.cpp/'])
    # print("install")
    # subprocess.run(['pip', 'install', '-r', '../llama.cpp/requirements.txt'])
    
    llama_dir = '../llama.cpp/'
    
    print("convert")
    # subprocess.run(['python', os.path.join(llama_dir, 'convert_hf_to_gguf.py'), 
                    # os.path.join(model_path, model_dir), '--outfile', gguf_name, 
                    # '--outtype', selected_values['qt']])
    
    print("mv")
    # subprocess.run(['mv', gguf_name, os.path.join(llama_dir, 'models/')])
    # subprocess.run(['../llama.cpp/llama-cli', '-m', os.path.join(llama_dir, 'models/', gguf_name), 
    #                 '-p', "I believe the meaning of life is", '-n', '128'])
    
    print("Finish main.py")
