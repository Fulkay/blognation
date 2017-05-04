import requests
import psycopg2
import psycopg2.extras
from datetime import datetime
import logging

# do not use these
from keys import api_token
from keys import db_password

def fetch_data():
    # api_token = 'insertmytokenhere'

    #url = 'http://api.wunderground.com/api' + api_token + 'conditions/../London_Surrey.json'
    r = request.get(url).json()
    data = r['current_observations']

    location = data['observation_location']['full'] # city, state and observation location
    weather = data['weather']
    temp = data['temp_f'] # temperature in fahrenheit
    humidity = data['relative_humidity']
    precip = data['precip_today_string']
    observation_time = data['observation_time']

fetch_data()
