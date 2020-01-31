# 1. Create a virtualenv for your project. 
	python 3.7+
# 2. Activate virtualenv and install requirements
	pip install -r requirements.txt
# 3. Change the database settings. I have just used SQLite, because you should set your Postgres. 

Just do like that;

DATABASES = {
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<databasename>',
        'USER': '<db user name>',
        'PASSWORD': '<db password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# 4. Make migrations for db and migrate them.
	python manage.py makemigrations
	python manage.py migrate
# 5. Create your first super user.
	python manage.py createsuperuser
# 6. Run the django server
	python manage.py runserver.
# 7. Enjoy your APIs with Postman.
