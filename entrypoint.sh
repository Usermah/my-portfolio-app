#!/bin/sh

echo "✅ Running collectstatic..."
python manage.py collectstatic --noinput

echo "✅ Running migrate..."
python manage.py migrate

echo "✅ Creating superuser (will skip if exists)..."
python manage.py createsuperuser --noinput || true

echo "✅ Starting Gunicorn server..."
gunicorn portfolio.wsgi:application --bind 0.0.0.0:8000

