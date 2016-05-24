from MathQuizer import app, models
#from components import sms, email
from flask import render_template, url_for, request, redirect, flash, jsonify
import logging 

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from requests_oauthlib import OAuth2Session
import httplib2
import json
from flask import make_response
import requests

logging.info('view.py file accessed ')

#CLIENT_ID = json.loads(open('secrets/g_client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "MathQuizer"


#
@app.route('/')
def main():
    return render_template('main.html')

#Define the secret key
app.secret_key = 'super_secret_key'