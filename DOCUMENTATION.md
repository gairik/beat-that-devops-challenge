# Goal

Buid an application in Style!


# Tools required

1. docker
2. minikube

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

# Add Kubernetes resource 
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
# Make your own interesting sub topics

