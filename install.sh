#!/bin/bash

# Create a virtual environment in the .venv directory
cd backend

python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip to the latest version
pip install -r requirements.txt

# install serve
npm install -g serve

echo "Virtual environment installed and activated at .venv"