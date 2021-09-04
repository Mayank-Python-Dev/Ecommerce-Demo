if you already clone this project

create virtualenv

mkvirtualenv

you have to install dependencies first

cmd : pip install -r requirements.txt

generate raw sql using python manage.py makemigrations

then migrate to create table on django admin 

cmd : python manage.py migrate

to run the server 

python manage.py runserver

to work with payment gateway you have to pass merchant id and merchant key which is there in developer.paytm.com
