#!/bin/bash

set -e

echo "1. Installing python venv...."
python3 -mvenv venv
echo "   Python venv done."

echo "2. Installing python packages with pip......"
. venv/bin/activate
pip install -r requirements.txt
echo "   Installing python packages done."

echo "3. Creating Schemas into DB $POSTGRES_DB......"
rm -rf migrations
python manage.py makemigrations  
python manage.py migrate
echo "   Creating Schemas into DB test done."


echo "4. Starting backend flask server....."
python manage.py  runserver $BACKENDPORT &
echo "   Backend flask server is up ....."

echo "5. Loading data into server....."
sleep 5
python bin/API_load.py dashboard_data.json
echo "   Data Load done ....."

