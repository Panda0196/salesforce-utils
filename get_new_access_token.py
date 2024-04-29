#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests
from dotenv import load_dotenv

load_dotenv()
SALES_KEY = os.getenv('SALES_CLIENT_KEY')
SALES_SECRET = os.getenv('SALES_CLIENT_SECRET')

def get_new_access_token(refresh_token):
    auth_url = 'https://login.salesforce.com/services/oauth2/token'

    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": SALES_KEY,
        "client_secret": SALES_SECRET
    }

    response = requests.post(auth_url, data=payload)
    response_json = response.json()

    print(response_json)
    if response.status_code == 200:
        print("OK")


if len(sys.argv) > 1:
    get_new_access_token(sys.argv[1])
else:
    print("No argument: refresh token!")