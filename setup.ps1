# Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip

# CUDA-enabled version of torch
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu116

# Install Stable Diffusion packages
pip install diffusers==0.3.0 transformers scipy ftfy
