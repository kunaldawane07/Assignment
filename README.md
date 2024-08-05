# Data Analysis 
Hi there! 😊 This is a fun project where we make a web application to look at data from CSV files and show some cool pictures.
## Table of Contents
- [Brief Explanation of the Project](#brief-explanation-of-the-project)
- [Screenshot](#screenshot)
- [Prerequisites](#prerequisites)
- [Installation and Setup](#installation-and-setup)
## Brief Explanation of the Project
The Data Analysis is a simple web application that lets you upload CSV files, analyze the data inside them, and see the results and some neat visualizations on a web page. It's built using Django, a popular web framework for Python, and uses libraries like pandas and seaborn for data analysis and visualization.

## Screenshot
- Upload 
![Screenshot 2024-08-05 134951](https://github.com/user-attachments/assets/156d594d-a1b6-42a9-98fe-b59ddc1d509f)
- Result 
![Screenshot 2024-08-05 135023](https://github.com/user-attachments/assets/73b03c69-e4d7-476d-a6d7-52038a772ca7)
![Screenshot 2024-08-05 135048](https://github.com/user-attachments/assets/8c383754-94fa-42bf-ac5a-8a830390d6e9)
## Prerequisites
- Python
- pip
- Virtual environment tool
## Installation and Setup
1. Clone the repository:
```
git clone https://github.com/kunaldawane07/Assignment.git
cd Assignment
```
2. Activate virtual environment
```
env\Scripts\activate
```
3. Install require packages
```
pip install -r requirements.txt
```
4. Create a Django project and app
```
django-admin startproject assignment
python manage.py startapp assignment_app
```
5. Update `settings.py`
Add 'assignment_app' to the INSTALLED_APPS list in assignment/settings.py.
6. Create templates folder:
```
assignment_app/
              templates/
                        upload.html
                        result.html
```
7. Create urls.py in your app folder:
```
from django.urls import path
from .views import upload_file 

urlpatterns = [
    path('', upload_file, name='upload_file'),
]
```
8. Update project urls.py
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('assignment_app.urls')),
]

```
9. Create forms.py in your app directory
```
from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField()
```
10. Run the migrations:
```
python manage.py migrate
```
11. Start the server:
```
python manage.py runserver
```
