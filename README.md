Kando is an effective project management software that is based on the Kanban method
# kando

Install this project by following the instructions below:


Install python2 if you do not already have it
Install python-pip
Change directory to root of project
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python ./manage.py createsuperuser
python manage.py runserver 8000
Go to http://127.0.0.1:8000/admin/ on your broswer, after logging in, create a Kando user


Install frontend

Navigate to /frontend/ui
sudo npm install -g bower
npm install --save-dev gulp
npm install