#!/bin/bash

# Create a virtual environment in the .venv directory
cd backend

python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Upgrade pip to the latest version
echo "Installing ..."
pip install -r requirements.txt --quiet
echo "Install playwright browser"
playwright install
echo "Complete"

# install serve
cd ../frontend
npm install --omit=dev --silent
echo "Complete"

# setup service file
cd ..
sudo cp stillframe.service /etc/systemd/system/stillframe.service
sudo systemctl daemon-reload
sudo systemctl enable stillframe
sudo systemctl start stillframe
echo "Service started"