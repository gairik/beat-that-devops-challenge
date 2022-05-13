# Goal

Buid an application that that gets the PRs from argo-cd project in Github not older than 3 days:

```
state: <as provided by github (either success, failure, or pending)>
statuses: # list of all statuses provided to the commit
  - state: <as provided by github (either success, failure, or pending)>
    context: <as provided by github (string)>
    updated_at: <as provided by github (timestamp)>

{state:open, 
status : [{state: open, context: somecontext, updated_at: date}, {state: open, context: somecontext, updated_at: date}, {state: open, context: somecontext, updated_at: date}]}

```


| Name   | Method      | URL
| ---    | ---         | ---
| List   | `GET`       | `curl http://127.0.0.1:5555/ `

# Terminologies and Descriptions:
1. **Docker**  
Tool to contanarize applications in isolated environment to deploy. It is used to package code with dependencies into a deployable unit.
2. **Kubernetes**  
Kubernetes is an open-source container orchestration system for automating software deployment, scaling, and management.


# Pre-requsits
1. `docker-compose` 
2. `docker`


# Plan 
The application is wriiten using Flask python . To achive this in an easy way `docker-compose` tool is used. The dev can make changes in the application ie `app.py` in our case. After that the docker-compose tool is used to spin up the docker container ie the python app with latest code changes. The `docker-compose.yaml` has the configurations to build and run the containers with different configurations like ports, env variables etc.  


# Locally
Make changes in the python applicaiton and run locally using `docker-compose` tool


`docker-compose up --build -d`  
Run the command 

```

docker-compose up --build -d
```


## Test the API using CURL

1. GET  
`curl http://127.0.0.1:5555/ `

# Something extra: Add Kubernetes resource (Bonus!)
1. flask - deployemnt, service


`cd k8s/`

# Create Flask deplpment/service
`docker build -t flask-app .`  
`kubectl create -f flask-github.yaml`



```
#Check the pods 
kubectl get pods

Check services
kubectl get svc
```


# Something extra: github Actions : build and test!

Do you want to know about `github actions `? Ofcourse you do! ;)
It is a CI (Continious Integration) system offered by github for free!  

## Terminology
1. **Workflows**
A workflow is a configurable automated process that will run one or more jobs. Workflows are defined by a YAML file checked in to your repository and will run when triggered by an event in your repository, or they can be triggered manually, or at a defined schedule.  
2. **Events**
An event is a specific activity in a repository that triggers a workflow run. For e.g. Push  
3. **Jobs**  
A job is a set of steps in a workflow that execute on the same runner. Each step is either a shell script that will be executed, or an action that will be run.  
4. **Runners**
A runner is a server that runs your workflows when they're triggered. Each runner can run a single job at a time. GitHub provides Ubuntu Linux, Microsoft Windows, and macOS runners to run your workflows


In our CI we are running the docker containers using the `docker-compose --build -d` command.  `-d` runs the container gives the shell back after the command finishes executing.  
Later we are doing a simple `CURL` to the API to check it the server is up and running.  
