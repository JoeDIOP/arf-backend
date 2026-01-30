#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# Création automatique du superuser si demandé
if [ "$CREATE_SUPERUSER" = "True" ]; then
  echo "Creating Django superuser..."
  python manage.py createsuperuser --no-input || true
else
  echo "Skipping superuser creation."
fi
