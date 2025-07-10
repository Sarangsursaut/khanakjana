#!/bin/bash

# Step 1: Install Python dependencies
pip install -r requirements.txt

# Step 2: Build Tailwind CSS (in z_dev folder)
cd z_dev
npm install
npm run prod
cd ..

# Step 3: Collect Django static files
python manage.py collectstatic --noinput
