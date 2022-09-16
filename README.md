# Stable Diffusion

## Setup

1. Create https://huggingface.co profile and access token
2. Grant profile access to https://huggingface.co/CompVis/stable-diffusion-v1-4
3. Read https://huggingface.co/blog/stable_diffusion#running-stable-diffusion

## Initialisation

Run `setup.ps1` to set up/install

## Running

First run `activate.ps1` to activate the `venv` if not already active. Then:

* `python test.py <YOUR_ACCESS_TOKEN> <PROMPT>` (generates `/output/test.png`)
* `python test.py <YOUR_ACCESS_TOKEN> <PROMPT> myfilename` (generates `/output/myfilename.png`)
