#!/bin/bash

# Create a virtual environment in the .venv directory
cd backend

python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip to the latest version
echo "Installing ..."
pip install -r requirements.txt --quiet

# install serve
cd ../frontend
npm install --omit=dev --silent
echo "Complete"

# Add start.sh to run at startup using crontab
(crontab -l 2>/dev/null | grep -q "@reboot /app/StillFrame/start.sh") || (crontab -l 2>/dev/null; echo "@reboot /app/StillFrame/start.sh") | crontab -
