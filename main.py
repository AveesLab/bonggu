from huggingface_hub import snapshot_download
import argparse
import sys
import subprocess

def parse_args():
    parser = argparse.ArgumentParser(description="Download Open Source LLM Weight File in Huggingface")
    parser.add_argument("--model", type = str, help = "Enter Model repo. ex) user_name/model_name", 
                        default = "beomi/Llama-3-Open-Ko-8B")
    parser.add_argument("--save_dir", type = str, help = "Set your model dir",
                        default = "models")
    parser.add_argument("--symlinks", type = bool, help = "Use symlinks",
                        default = False)
    parser.add_argument("--revision", type = str, help = "Select version",
                        default = "main")
    
    if len(sys.argv) == 0:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    print("Start main.py")
    args = parse_args()
    snapshot_download(repo_id = args.model, local_dir = args.save_dir, 
                      local_dir_use_symlinks = args.symlinks, revision = args.revision)
    
    print("Start git clone")
    subprocess.run(['git', 'clone', 'https://github.com/ggerganov/llama.cpp.git', '../llama.cpp'])
    print("make")
    subprocess.run(['make', '-C', '../llama.cpp/'])
    print("install")
    subprocess.run(['pip', 'install', '-r', '../llama.cpp/requirements.txt'])
    print("convert")
    subprocess.run(['python', '../llama.cpp/convert_hf_to_gguf.py', 'models', '--outfile', 'llama-3-open-ko-8b.gguf', '--outtype', 'q8_0'])
    print("mv")
    subprocess.run(['mv', 'llama-3-open-ko-8b.gguf', '../llama.cpp/models'])
    subprocess.run(['../llama.cpp/llama-cli', '-m', '../llama.cpp/models/llama-3-open-ko-8b.gguf', '-p', '안녕', '-cnv'])
    print("Finish main.py")