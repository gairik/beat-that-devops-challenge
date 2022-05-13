''' 
Write a program that can list all open pull-requests of a git-repository on
github.com that are younger than 3 days. For each pull-request the program shall
gather the following infos about its commit-statuses for the HEAD commit:

state: <as provided by github (either success, failure, or pending)>
statuses: # list of all statuses provided to the commit
  - state: <as provided by github (either success, failure, or pending)>
    context: <as provided by github (string)>
    updated_at: <as provided by github (timestamp)>
  -

{state:open, status : [{state: open, context: bla, updated_at: bla}, {state: open, context: bla, updated_at: bla}, {state: open, context: bla, updated_at: bla}]}
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
HTTPConnection.debuglevel = 1


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

def commitDetails(statuses_url):
    
    commit_details = getReq(statuses_url)
    status = []
    for commits in commit_details:
        temp = {}
        state = commits['state']
        context = commits['context']
        updated_at = commits['updated_at']
        temp = {'state':state, 'context': context, 'updated_at': updated_at}
        status.append(temp)
    
    return (status)

def threeDaysOld(response_data):
    
    today = datetime.date.today()
    final_data = []
    for response in response_data:
        created_at = response['created_at'].split('T')[0]
        created_at = datetime.datetime.strptime(created_at,'%Y-%m-%d').date()
        age = (today - created_at).days

        if age <=3:
            commitDetails_list = commitDetails(response['statuses_url'])
            final_data.append({'pr': response['url'], 'state': response['state'], 'status': commitDetails_list})

    if final_data is not None:
        
        return final_data
    else:
        return None     

@app.route("/config" , methods=['GET'])
def config():
    return ('user is {0}, github_token {1}, owner {2}, project {3}'.format(user, github_token, owner, project))


@app.route("/" , methods=['GET'])
def main():
    response_data = getReq('{0}/repos/{1}/{2}/pulls'.format(github_api,owner,project))
    if response_data is not None:   
            final_data = threeDaysOld(response_data)
    return (json.dumps(final_data, default = str, indent=4, sort_keys=True))


app.run(host="0.0.0.0", port=5555 , debug=True)
