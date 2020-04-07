from flask import Flask, request, Response

# Cliente HTTP
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return str(100*12)
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'

#adding variables
@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

@app.route('/guess', methods=['GET','POST', 'PUT'])
def login():
  if request.method == 'POST':
    #check user details from db
    return method_post()
  elif request.method == 'GET':
    #serve login page
    return method_get()
  elif request.method == 'PUT':
    response = requests.get('https://api.bitso.com/v3/available_books/')
    return Response(
      response.text,
      status=response.status_code,
      content_type=response.headers['Content-Type']
    )

def method_post():
    return 'Your request was a POST'

def method_get():
    return 'Your request was a GET'

# install python 3 on your local machine
# pip3 install virtualenv

#crea un directorio/folder donde pondras tu API y virtualenv
# virtualenv env (esto se crea en el mismo lugar donde va app.py)
# for activate the virtualenv
# source env/bin/activate
# once your virtualenv is running:
# pip install flask
# pip install requests

# set FLASK_ENV=development 
# set FLASK_APP=app.py

# Para correrlo
# flask run

# para desactivar virtualenv
# deactivate