#!/bin/bash

# install apt packages
sudo apt-get update
# these are the packages required to run playwright
sudo apt-get install -y libpci3 libx11-dev libgtk-3-0 libdbus-1-3 libegl1-mesa libgles2-mesa xvfb firefox-esr libgtk-4-1 libgraphene-1.0-0

# install noto fonts
sudo apt-get install -y fonts-noto


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