"""
Authentication via bearer token using requests

Source: https://stackoverflow.com/questions/29931671/making-an-api-call-in-python-with-an-api-that-requires-a-bearer-token
"""
from pprint import pprint
import os
import sys
import time

import base64
import requests

time.sleep(3)

USERNAME = "johndoe"
PASSWORD = os.environ.get("API_PASSWORD")

# how to remove a password from code?
# 1: input("enter your password:")  # TODO: remove this!!!
# 2: open('mypassword.txt').read().strip()
# 3: os.environ.get("API_PASSWORD")

URL = "http://" + sys.argv[1]  # reads a command-line argument

# key + secret that the server might need
# (not used by example server)
consumer_key = 'ggczWttBWlTjXCEtk3Yie_WJGEIa'
consumer_secret = 'uuzPjjJykiuuLfHkfgSdXLV98Ciga'
consumer_key_secret = consumer_key+":"+consumer_secret
consumer_key_secret_enc = base64.b64encode(consumer_key_secret.encode()).decode()

#
# Part 1: Authenticate with username + password
#
headersAuth = {
    'Authorization': 'Basic '+ str(consumer_key_secret_enc),
}

data = {
  'grant_type': 'password',
  'username': USERNAME,
  'password': PASSWORD
}

response = requests.post(f'{URL}/token', headers=headersAuth, data=data, verify=True)
j = response.json()
pprint(j)

# you can decode the JWT token on jwt.io
jwt_token = j["access_token"]

#
# Part 2: Using authentication to make API calls   
#
print()

# Define header for making API calls that will hold authentication data
headersAPI = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+j['access_token'],
}


# call fails without authentication
response = requests.get(f'{URL}/fruits', verify=True)
print(response.status_code)


# sample API call with authentication
params = (
    ('number', 7),
          )
response = requests.get(f'{URL}/fruits', headers=headersAPI, params=params, verify=True)
pprint(response.json())
