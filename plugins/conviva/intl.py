import requests
import json
import sys
import pymysql
import csv
import base64
import re
from datetime import datetime
from pprint import pprint
from Crypto.Cipher import XOR
from __future__ import unicode_literals
from client import slack_client as sc

outputs = []

def process_message(data):
    '''If a user passes 'print users' in a message, print the users in the slack
    team to the console. (Don't run this in production probably)'''
    if 'bot intl top 10' in data['text']:

        print('Someday that will happen')

        url = "https://api.conviva.com/insights/2/metrics.json"

        querystring = {"metrics":"audience_metriclens","metriclens_dimension_id":"11761","filter_ids":"3730"

        headers = {
            'authorization': "Basic ZTN0b0Blc3BuLmNvbTpFc3BuMTIzNA==",
            }
        response = requests.request("GET", url, headers=headers, params=querystring)
        dump = response.json()
        pprint(dump)
        total3730 = dump['audience_metriclens']['tables'][filter]['total_row']
        outputs.append(["G04MZ9ZTP", total3730])
