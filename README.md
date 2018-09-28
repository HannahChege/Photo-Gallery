# TITLE
Photo-Gallery
#Built By
 Hannah Njeri
#Description 
This is a Personal gallery application that i have  build with Django application used to  display your photos for others to view.As for this application i decide to major on Fashion of which i have different categories of which i have classified thm into three parts:
1.Mens Wear
2.Ladies Wear
3.Kids Wear 
You can view the site at:Heroku

User Stories These are the behaviours/features that the application implements for use by a user.

As a user of the application you should be able to:

View different photos that interest you.
Click on a single photo to expand it and also view the details of the photo. The photo details  appear on a modal within the same route as the main page.
Search for different categories of photos. (ie. Ladies wear, Mens wear)
Copy a link to the photo to share with your  friends.
View photos based on the location they were taken.
SetUp / Installation Requirements Prerequisites python3.6 pip virtualenv Cloning In your terminal:

$ git clone https://github.com/HannahChege/Photo-Gallery/ 
$ cd Photo-Gallery
 Running the Application 
Creating the virtual environment

$ python3.6 -m venv --without-pip virtual $ 
source virtual/bin/env 
Installing Django. 
(virtual)$ pip install django==1.11
Confirm that you do have Django.
To achieve this, activate your python shell and run python3.6 on your terminal.
Under your shell input this code:
 >>> import django
>>> django.get_version()
'1.11.5'
Start a Django server.
(virtual)$ python3.6 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
September 28, 2018 - 12:01:08
Django version 1.11, using settings 'gallery.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
 Technologies Used 
Python3.6  
License Copyright (c) 2018 HannahChege

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
