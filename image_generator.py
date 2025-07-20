import torch
import tempfile
from diffusers import StableDiffusionPipeline
from transformers import pipeline, set_seed
# from authtoken import auth_token
from PIL import Image
import platform
import os
import subprocess
import tempfile
from torch import autocast

auth_token = os.environ.get('auth_token')
model = "CompVis/stable-diffusion-v1-4"
device =  "cuda"
pipe = StableDiffusionPipeline.from_pretrained(model, variant='fp16', torch_dtype= torch.float16)
pipe.to(device)
def image_generator(prompt):
    prompt += ", 4k, high resolution"
    with autocast(device):
        image = pipe(prompt, guidance_scale=8.5)["images"][0]
    image_name = 'generatedImage.png'
    image.save(image_name)
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
        image.save(temp_file.name)
        image_path = temp_file.name

        # Open the image using the default viewer in a non-blocking way
        subprocess.Popen(["open", image_path] if platform.system() == "Darwin" else ["xdg-open", image_path] if platform.system() == "Linux" else ["start", image_path], shell=True)