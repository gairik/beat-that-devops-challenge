''' 
Get PR details
pr_details  = {'pr_html_url':pr_html_url,
                    'pr_title':pr_title,
                    'pr_user': pr_user_details,
                    'pr_updated_at':pr_updated_at
                    }
'''

from flask import Flask , request , jsonify , redirect
import json
import sys
from os import environ
import os
import requests
from http.client import HTTPConnection
import datetime, time

app = Flask("myapp") 
#HTTPConnection.debuglevel = 1


if os.getenv('GITHUB_USER') is None:
    user = ''
else:
    user = os.getenv('GITHUB_USER')


if os.getenv('GITHUB_TOKEN') is None:
    github_token = ''
else:
    github_token = os.getenv('GITHUB_TOKEN')


if os.getenv('OWNER') is None:
    owner = ''
else:
    owner = os.getenv('OWNER')

if os.getenv('PROJECT') is None:
    project = ''
else:
    project = os.getenv('PROJECT')

github_api = 'https://api.github.com'

owner='argoproj'
project='argo-cd'

def getReq(reqUrl):

    headers = {
        'Accept': 'application/vnd.github.v3+json',
    }
    if user == '' or github_token == '':
        response = requests.get(reqUrl, 
                                headers=headers)
    else:
        response = requests.get(reqUrl, 
                                headers=headers, 
                                auth=(user, github_token))

    if response is not None:
        return response.json()
    else:
        return None

def makePrDetails(response_data):
    
    pr_details = {}

    pr_html_url = response_data[0]['html_url']
    pr_title = response_data[0]['title']
    pr_user_details = response_data[0]['user']
    pr_updated_at = response_data[0]['updated_at']

    pr_details  = {'pr_html_url':pr_html_url,
                    'pr_title':pr_title,
                    'pr_user': pr_user_details,
                    'pr_updated_at':pr_updated_at
                    }

    return (pr_details)   

# @app.route("/config" , methods=['GET'])
# def config():
#     return ('user is {0}, github_token {1}, owner {2}, project {3}'.format(user, github_token, owner, project))


# @app.route("/" , methods=['GET'])
# def main():
#     response_data = getReq('{0}/repos/{1}/{2}/pulls'.format(github_api,owner,project))
#     if response_data is not None:   
#             final_data = threeDaysOld(response_data)
#     return (json.dumps(final_data, default = str, indent=4, sort_keys=True))


# app.run(host="0.0.0.0", port=5555 , debug=True)

def main():
    response_data = getReq('{0}/repos/{1}/{2}/pulls'.format(github_api,owner,project))
    pr_details = makePrDetails(response_data)
    print (pr_details)
    #return (json.dumps(final_data, default = str, indent=4, sort_keys=True))

main()