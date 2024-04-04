#!/bin/bash
set -e

echo "1. Installing python venv...."
python3 -mvenv venv
echo "   Python venv done."

echo "2. Installing python packages with pip......"
. venv/bin/activate
pip install -r requirements.txt
echo "   Installing python packages done."

echo "3. Starting front end flask server....."
python manage.py runserver $FRONTENDPORT &
echo "   Front end flask server is up ....."
