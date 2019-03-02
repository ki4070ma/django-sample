# Readme
* To learn backend

# Step by step
1. Create project
   * ```django-admin start project mysite```
2. Run server for development
   * ```python manage.py runserver {0:8080}```
3. Create application
   * ```python manage.py startapp polls```
4. Set up database
   * ```python manage.py migrate```
   * ```python manage.py makemigrations polls```
   * ```python manage.py sqlmigrate polls 0001```
      * To check sql execution on migration
   * ```python manage.py migrate```
      * Migrate polls table into sqlite database 

# Reference
* Writing your first Django app, part 1
   * https://docs.djangoproject.com/en/2.1/intro/tutorial01/
   * https://docs.djangoproject.com/ja/2.1/intro/tutorial01/
