# besnardTask App

This app is a simple CRUD that displays the 4 values and the 12 principles of Agile Software Development.

## Required packages to install

## Venv (need to run 'python manage.py runserver' in a virtual environment if using python2)
```
$ pip install virtualenv
$ virtualenv venv
```
### npm package
```
$ npm install
```

### Axios
```
$ npm install axios
```

### Vue CLI
```
$ npm install -g @vue/cli
```

## To run the app

1. In besnard_task_django folder. Run **populate.py** under besnard_task_django\app (this will make migrations and populate the database)
1. In besnard_task_django folder. Run ```python manage.py runserver``` to start the backend of the application.
1. In besnard_task_vue folder. Run ```npm run serve``` to start the frontend of the application
