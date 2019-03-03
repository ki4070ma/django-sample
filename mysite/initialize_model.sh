#!/usr/bin/env bash

# [Usage]: bash ./initialize_model.sh
# [**CAUTION**]: current db(db.sqlite) will be deleted!!!

rm db.sqlite3
python manage.py migrate
python manage.py makemigrations polls
python manage.py migrate
python manage.py shell < initialize_model.py