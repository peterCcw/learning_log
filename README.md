# Learning Log
Alien Invasion is my implementation of the web application based on tutorial from "Python Crash Course, 2nd Edition". 
It contains some additional simple features which expand project from the book.
### Table of contents
* [Description](#description)
    * [About](#about)
    * [Additional features](#additional-features)
* [Technologies](#technologies)
* [How to use](#how-to-use)
    * [Installation](#installation)
    * [Manual](#manual)
    
    
### Description  
##### About
This project was made to practise **Python 3** and to try **Django**. It is based on tutorial from the book, but I added
very simple original features to make the application more useful for the users. The application is very simple version
of log book, designed to use for learning new things. Same as with ***Alien Invasion*** my main goal was to write good
quality code according to the **Python Enhancement Proposals** and to learn very basics of **Django**. 
##### Additional features
Besides content provided by tutorial, the application contains also:
* **Delete and editing** - user is able to delete and edit entries and topics
* **Additional styling** - some additional styling added, buttons, messages etc.
### Technologies
* [**Python 3.8.5**](https://www.python.org/)
* [**Django 3.1.1**](https://www.djangoproject.com/)
* [**django-bootstrap 2.2.0**](https://django-bootstrap4.readthedocs.io/)
### How to use
##### Launching up
Requirements:
all the requirements are mentioned in [Technologies](#technologies) section. You can check the application on your local
computer by running django developer server. Firstly, install Django and django-bootstrap:
```commandline
pip install django
```
```commandline
pip install django-bootstrap4
```
Download all files manually and place them in a specific directory.
If you have git installed, you can also use code below (in specific directory):
```commandline
git clone https://github.com/peterCcw/learning_log
```
Move to directory with the application files and use:
```commandline
python manage.py migrate
```
and next:
```commandline
python manage.py runserver
```
Application should be available at http://127.0.0.1:8000/

##### Manual
Application gives you possibility to register your account and to create topics. For each topic you can post entries
about your progress during learning.

Topics and entries can be deleted when you don't need them anymore.
