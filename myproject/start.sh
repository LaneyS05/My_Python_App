#!/bin/bash
echo "Starting Django application..."
pip install -r requirements.txt  # Ensure all requirements are installed
python manage.py migrate  # Apply migrations
python manage.py collectstatic --noinput  # Collect static files
gunicorn myproject.wsgi --bind 0.0.0.0:$PORT  # Start the Gunicorn server
