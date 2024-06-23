#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import requests

def revoke_refresh_token(r):
    url = 'https://login.salesforce.com/services/oauth2/revoke'
    response = requests.post(url, data={'token':r})

    if response.status_code == 200:
        print(response)
    else:
        raise Exception({"REVOKE_REFRESH_TOKEN" : response_json})

if len(sys.argv) > 1:
    revoke_refresh_token(sys.argv[1])
else:
    print("No argument: refresh token!")