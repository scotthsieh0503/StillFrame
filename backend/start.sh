#!/bin/bash

source .venv/bin/activate
flask --app ./src/app.py run --host 0.0.0.0 --port 5000