from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model
model_id = "sd-legacy/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(
    model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

# Define the prompt for image generation
prompt = "A futuristic cityscape at sunset, with flying cars and neon lights"
# Generate the image
image = pipe(prompt, num_inference_steps=50, guidance_scale=7.5).images[0]
# Save the generated image
image.save("generated_image.png")
# Display the generated image
image.show()
