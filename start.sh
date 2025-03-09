#!/bin/bash

# Function to check if a process is running
is_running() {
    pgrep -f "$1" > /dev/null 2>&1
}

# Function to kill a running process
kill_process() {
    pkill -f "$1"
}

# Start backend in production mode
if is_running "flask --app ./src/main.py run"; then
    echo "Flask app is already running. Killing the process..."
    kill_process "flask --app ./src/main.py run"
fi

cd backend
source .venv/bin/activate
export FLASK_ENV=production
flask --app ./src/main.py run --host 0.0.0.0 --port 5000 &
cd ..

# Start frontend in production mode
if is_running "npm run serve -- -l 80"; then
    echo "Next.js app is already running. Killing the process..."
    kill_process "npm run serve -- -l 80"
fi

cd frontend
npm run serve -- -l 80 &
cd ..