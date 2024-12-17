#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Run the Flask development server
export FLASK_APP=app.py # ganti app.py dengan nama file aplikasi utama Anda
flask run --debug