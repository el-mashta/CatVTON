import os
import torch
from PIL import Image
from huggingface_hub import snapshot_download

from model.pipeline import CatVTONPipeline
from model.cloth_masker import AutoMasker, vis_mask
from utils import init_weight_dtype, resize_and_crop, resize_and_padding
from diffusers.image_processor import VaeImageProcessor

def main():
    """
    A simple script to test the CatVTON model pipeline on a GPU.
    """
    print("--- Starting CatVTON GPU Test ---")

    # --- 1. Hardcoded Configuration ---
    # These are based on the defaults in app.py
    base_model_path = "stable-diffusion-v1-5/stable-diffusion-inpainting"
    resume_path = "zhengchong/CatVTON"
    output_dir = "test_output"
    width = 768
    height = 1024
    mixed_precision = "fp16" # or "fp16" if your GPU doesn't support bf16
    allow_tf32 = True
    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    if device == 'cpu':
        print("Warning: No GPU detected. This will be very slow.")
        # Adjust precision for CPU
        mixed_precision = "no"
        allow_tf32 = False


    # --- 2. Download and Load Models ---
    print(f"Downloading models from Hugging Face repo: {resume_path}...")
    try:
        repo_path = snapshot_download(repo_id=resume_path)
        print("Model download complete.")
    except Exception as e:
        print(f"Error downloading models: {e}")
        print("Please check your internet connection and Hugging Face Hub credentials.")
        return

    print("Initializing CatVTONPipeline...")
    try:
        pipeline = CatVTONPipeline(
            base_ckpt=base_model_path,
            attn_ckpt=repo_path,
            attn_ckpt_version="mix",
            weight_dtype=init_weight_dtype(mixed_precision),
            use_tf32=allow_tf32,
            device=device
        )
        print("Pipeline initialized successfully.")
    except Exception as e:
        print(f"Error initializing pipeline: {e}")
        print("This might be a dependency issue. Check your torch, diffusers, and transformers versions.")
        return

    print("Initializing AutoMasker...")
    try:
        mask_processor = VaeImageProcessor(vae_scale_factor=8, do_normalize=False, do_binarize=True, do_convert_grayscale=True)
        automasker = AutoMasker(
            densepose_ckpt=os.path.join(repo_path, "DensePose"),
            schp_ckpt=os.path.join(repo_path, "SCHP"),
            device=device,
        )
        print("AutoMasker initialized successfully.")
    except Exception as e:
        print(f"Error initializing AutoMasker: {e}")
        print("This could be related to fvcore or detectron2 dependencies.")
        return

    # --- 3. Prepare Input Data ---
    # Using example images provided in the repository
    person_image_path = "resource/demo/example/person/men/01.jpg"
    cloth_image_path = "resource/demo/example/condition/upper/01.jpg"
    cloth_type = "upper" # or "lower", "overall"

    print(f"Loading person image: {person_image_path}")
    print(f"Loading cloth image: {cloth_image_path}")

    if not os.path.exists(person_image_path) or not os.path.exists(cloth_image_path):
        print("Error: Example images not found. Please ensure the following files exist:")
        print(f"- {person_image_path}")
        print(f"- {cloth_image_path}")
        return

    person_image = Image.open(person_image_path).convert("RGB")
    cloth_image = Image.open(cloth_image_path).convert("RGB")

    # Resize and crop images
    person_image = resize_and_crop(person_image, (width, height))
    cloth_image = resize_and_padding(cloth_image, (width, height))

    # --- 4. Generate Mask ---
    print("Generating mask for the person image...")
    try:
        mask = automasker(person_image, cloth_type)['mask']
        mask = mask_processor.blur(mask, blur_factor=9)
        print("Mask generated successfully.")
    except Exception as e:
        print(f"Error during mask generation: {e}")
        return


    # --- 5. Run Inference ---
    print("Running inference... (This may take a moment)")
    # Hardcoded inference parameters
    num_inference_steps = 50
    guidance_scale = 2.5
    seed = 42
    generator = torch.Generator(device=device).manual_seed(seed)

    try:
        with torch.no_grad():
            result_image = pipeline(
                image=person_image,
                condition_image=cloth_image,
                mask=mask,
                num_inference_steps=num_inference_steps,
                guidance_scale=guidance_scale,
                generator=generator
            )[0]
        print("Inference complete.")
    except Exception as e:
        print(f"An error occurred during inference: {e}")
        print("If this is a CUDA error, you might be out of memory. Try reducing image size.")
        return

    # --- 6. Save Output ---
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir, "test_output.png")
    result_image.save(output_path)
    print(f"--- Test Complete ---")
    print(f"Result saved to: {output_path}")


if __name__ == "__main__":
    main()
