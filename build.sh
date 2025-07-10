#!/bin/bash

# Install Python packages
pip install -r requirements.txt

# Install Tailwind dependencies
npm install

# Build Tailwind CSS
npm run prod

# Collect Django static files
python manage.py collectstatic --noinput