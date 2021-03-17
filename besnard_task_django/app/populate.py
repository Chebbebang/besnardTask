# Run the script to populate database.

import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'besnard_task.settings'

# Run to load data from besnard_app.json script inside of DJANGO shell.
os.chdir('../')
os.system('cmd /C py manage.py makemigrations')
os.system('cmd /C py manage.py migrate')
os.system('cmd /C py manage.py loaddata besnard_app.json')