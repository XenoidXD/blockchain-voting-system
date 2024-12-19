# ! This is just example, adjust it to the server are you using

#!/bin/bash

# Set the application directory on the server
APP_DIR="/var/www/voting-app"

# Set the virtual environment directory
VENV_DIR="$APP_DIR/venv"

# Set the system user to run gunicorn
SYSTEMD_USER=www-data

# Stop any running instances of gunicorn
systemctl stop voting-app.service

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Update the application code (e.g., using git pull)
cd "$APP_DIR"
git pull origin main

# Install dependencies
pip install -r requirements.txt

# Migrate database (jika ada)
# python manage.py migrate

# Collect static files (jika ada)
# python manage.py collectstatic --noinput

# Restart gunicorn using systemd
systemctl restart voting-app.service

echo "Application deployed successfully!"
