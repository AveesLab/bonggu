from huggingface_hub import snapshot_download
import argparse
import sys

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
    print("Finish main.py")