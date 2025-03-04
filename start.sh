#!/bin/bash

# Function to check if a process is running
is_running() {
    pgrep -f "$1" > /dev/null 2>&1
}

# Start backend in production mode if not already running
if ! is_running "flask --app ./src/app.py run"; then
    cd backend
    source .venv/bin/activate
    export FLASK_ENV=production
    flask --app ./src/app.py run --host 0.0.0.0 --port 5000 &
    cd ..
else
    echo "Flask app is already running."
fi

# Start frontend in production mode if not already running
if ! is_running "npm run start --port 3000"; then
    cd ../frontend
    npm run start --port 3000
else
    echo "Next.js app is already running."
fi