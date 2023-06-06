# JWT-Based-Login
Simple JWT-Based-Login
#1 create virtual environment: python -m venv venv

#2 venv active: venv/Scripts/activate

#3 install: pip install django djangorestframework

#4 create project: django-admin startproject name .

#5 to check: python manage.py migrate
python manage.py runserver

#6 configs: setting.py,urls.py

#7 create app: python manage.py startapp appname

#8 add urls.py file inside app

1. pip install djangorestframework_simplejwt
2. to see package versions: pip freeze
3. change package  version: pip install package_name == version
4. add inside setting.py: 'rest_framework_simplejwt'
5. project level url: 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
path('api/token/',TokenObtainPairView.as_view())
path('api/token/refresh/',TokenRefreshView.as_view())
