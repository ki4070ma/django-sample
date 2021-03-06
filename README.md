[![Job Status](https://inspecode.rocro.com/badges/github.com/ki4070ma/django-sample/status?token=N1SD8z0OyquMVWLtLn7_LTCq-uSng7BvaUZekdMtCGg)](https://inspecode.rocro.com/jobs/github.com/ki4070ma/django-sample/latest?completed=true) [![Report](https://inspecode.rocro.com/badges/github.com/ki4070ma/django-sample/report?token=N1SD8z0OyquMVWLtLn7_LTCq-uSng7BvaUZekdMtCGg&branch=master)](https://inspecode.rocro.com/reports/github.com/ki4070ma/django-sample/branch/master/summary)

# Readme
* To learn backend

# Step by step
1. Create project
   * ```django-admin start project mysite```
2. Run server for development
   * ```python manage.py runserver [0:8080]```
3. Create application
   * ```python manage.py startapp polls```
4. Set up database
   * ```python manage.py migrate```
   * ```python manage.py makemigrations polls```
   * ```python manage.py sqlmigrate polls 0001```
      * To check sql execution on migration
   * ```python manage.py migrate```
      * Migrate polls table into sqlite database 
5. Browse sqlite data via Django API
   * ```python manage.py shell```
   * See https://docs.djangoproject.com/ja/2.1/intro/tutorial02/

# Run tests
* ```python manage.py test polls```

# Run tests via behave
* Initialize database and run server
   * ```bash initialize_model.sh && python manage.py runserver```
* Run test
   * ```behave```

# Development
* Autopep
   * ```python -m autopep8 -r --global-config .config-pep8 -i .```

# Reference
* Writing your first Django app, part 1
   * https://docs.djangoproject.com/en/2.1/intro/tutorial01/
   * https://docs.djangoproject.com/ja/2.1/intro/tutorial01/
* SQLite browser
   * https://sqlitebrowser.org/
* Selenium web driver doc
   * https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.remote.webdriver
