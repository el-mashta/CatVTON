
import os
import sys
import torch
import shutil
from safetensors.torch import save_file

# --- Pre-computation: Add project directory to Python path ---
# This allows the script to import the necessary local modules like `model.utils`
# Assumes the script is run from /runpod-volume/CatVTON/
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Now we can import from the project
try:
    from diffusers import UNet2DConditionModel
    from accelerate import load_checkpoint_in_model
    from model.utils import get_trainable_module, init_adapter
    from model.attn_processor import SkipAttnProcessor
except ImportError as e:
    print(f"Error: A required library is missing. {e}")
    print("Please ensure you have run 'pip install -r requirements.txt' in your environment.")
    sys.exit(1)


def merge_models():
    """
    Loads the base SD 1.5 inpainting UNet, injects the CatVTON attention
    weights, and saves the result as a single, optimized safetensors file.
    """
    print("--- Starting CatVTON UNet Merge Process ---")

    # --- 1. Define Paths ---
    # Using the standard Hugging Face cache structure within /runpod-volume/models
    HF_HOME = "/runpod-volume/models"
    
    # Note: The original repo 'stable-diffusion-v1-5/stable-diffusion-inpainting' is no longer available.
    # The project uses 'booksforcharlie/stable-diffusion-inpainting' as a replacement.
    # We construct the path to the most likely snapshot directory.
    BASE_MODEL_ID = "booksforcharlie/stable-diffusion-inpainting"
    CATVTON_MODEL_ID = "zhengchong/CatVTON"

    base_model_path = os.path.join(HF_HOME, "hub", f"models--{BASE_MODEL_ID.replace('/', '--')}")
    catvton_model_path = os.path.join(HF_HOME, "hub", f"models--{CATVTON_MODEL_ID.replace('/', '--')}")

    # Find the latest snapshot directory for both models
    try:
        base_snapshot = max(os.listdir(os.path.join(base_model_path, "snapshots")))
        catvton_snapshot = max(os.listdir(os.path.join(catvton_model_path, "snapshots")))
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: Could not find downloaded model snapshots in {HF_HOME}/hub.")
        print("Please ensure you have downloaded both '{BASE_MODEL_ID}' and '{CATVTON_MODEL_ID}' first.")
        print(f"Original error: {e}")
        sys.exit(1)

    base_unet_path = os.path.join(base_model_path, "snapshots", base_snapshot, "unet")
    catvton_attn_path = os.path.join(catvton_model_path, "snapshots", catvton_snapshot, "mix-48k-1024", "attention")
    
    output_dir = os.path.join(HF_HOME, "catvton-unet-merged")

    print(f"Base UNet path: {base_unet_path}")
    print(f"CatVTON Attention path: {catvton_attn_path}")
    print(f"Output directory: {output_dir}")

    # --- 2. Create Output Directory ---
    os.makedirs(output_dir, exist_ok=True)

    # --- 3. Load Base UNet ---
    print("\nLoading base UNet from disk...")
    try:
        unet = UNet2DConditionModel.from_pretrained(base_unet_path)
        print("Base UNet loaded successfully.")
    except Exception as e:
        print(f"Failed to load base UNet: {e}")
        print("Please verify the path and integrity of the base model files.")
        sys.exit(1)

    # --- 4. Inject CatVTON Attention Weights ---
    print("Initializing adapter and injecting CatVTON attention weights...")
    try:
        # This step modifies the UNet in place
        init_adapter(unet, cross_attn_cls=SkipAttnProcessor)
        attn_modules = get_trainable_module(unet, "attention")
        load_checkpoint_in_model(attn_modules, catvton_attn_path)
        print("Attention weights injected successfully.")
    except Exception as e:
        print(f"Failed to inject attention weights: {e}")
        print("This may indicate an incompatibility or a problem with the CatVTON checkpoint.")
        sys.exit(1)

    # --- 5. Save the Merged UNet ---
    output_file = os.path.join(output_dir, "diffusion_pytorch_model.safetensors")
    print(f"\nSaving merged UNet to: {output_file}")
    try:
        # Fetch the state_dict from the modified UNet
        state_dict = unet.state_dict()
        save_file(state_dict, output_file)
        print("Save complete.")
    except Exception as e:
        print(f"Failed to save the merged model: {e}")
        sys.exit(1)

    # --- 6. Copy the UNet's config.json ---
    # This is crucial for allowing `from_pretrained` to work on our new directory
    config_src = os.path.join(base_unet_path, "config.json")
    config_dst = os.path.join(output_dir, "config.json")
    print(f"Copying UNet config from {config_src} to {config_dst}")
    try:
        shutil.copyfile(config_src, config_dst)
        print("Config file copied.")
    except Exception as e:
        print(f"Failed to copy config file: {e}")
        sys.exit(1)

    print("\n--- Success! ---")
    print("Your optimized, merged UNet is ready for use.")
    print(f"Use the following path in your pipeline: '{output_dir}'")


if __name__ == "__main__":
    merge_models()
