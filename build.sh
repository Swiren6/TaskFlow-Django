#!/usr/bin/env bash
# exit on error
set -o errexit
cd todo_app

cd todo_app
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
