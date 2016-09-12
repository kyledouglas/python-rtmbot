from __future__ import unicode_literals
from client import slack_client as sc


def process_message(data):
    '''If a user passes 'print users' in a message, print the users in the slack
    team to the console. (Don't run this in production probably)'''
    print(data['text'])
    if 'bot intl top 10' in data['text']:
        print('Someday that will happen')
