import sys
import torch
from diffusers import StableDiffusionPipeline
from PIL import Image

ACCESS_TOKEN = sys.argv[1]
PROMPT = sys.argv[2]
FILE_NAME = sys.argv[3] if len(sys.argv) > 3 else 'test'

# Default is 7.5, more = better quality images, less diversity
GUIDANCE_SCALE = 7.5

# Default is 50, more = slower, better quality images
INFERENCE_STEPS = 50 

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", use_auth_token=ACCESS_TOKEN)

pipe.to("cuda")

with torch.autocast("cuda"):
    result = pipe(PROMPT, guidance_scale=GUIDANCE_SCALE, num_inference_steps=INFERENCE_STEPS)

image = result["sample"][0]

image.save("output/{0}.png".format(FILE_NAME))
