# Manage a K8s cluster

To deploy toy-example applications in the cluster, we create a separate Namespace called *toy-example*.

 - [ ] Create namespace *toy-example*

	   kubectl create Namespace toy-example

 - [ ] Check the creation of toy-example Namespace:

	   kubectl get namespace

 - [ ] List the Pods under this Namespace:

	   kubectl get pods -n toy-example

> **Note:** As we havent deployed any pods yet, the output of this commnad will be no resources found in this namespace

Also, we create a folder for all the toy-example applications in the host machine with `mkdir toy-example` 

## Deploy a simple apache web application

First, we deploy a simple php-apache web application from an online yaml manifest file into the *toy-example* namespace:

 - [ ] Apply the php-apache web app into the cluster

	   kubectl apply -f https://k8s.io/examples/application/php-apache.yaml --namespace=toy-example

Next, we add load (infinite web requests) with another manifest file called infinity-calls.yaml. If we monitor later on the behaviour of this application with Prometheus the added load will provoke changes on the performance of the application. The manifest file of infinity-calls.yaml is described in the following code:

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: infinite-calls-nginx
      labels:
        app: infinite-calls-nginx
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: infinite-calls-nginx
      template:
        metadata:
          name: infinite-calls-nginx
          labels:
            app: infinite-calls-nginx
        spec:
          containers:
          - name: infinite-calls-nginx
            image: busybox
            command:
            - /bin/sh
            - -c
            - "while true; do wget -q -O- http://my-nginx; done"

 - [ ] Navigate into the toy-example folder in the machine

	   cd toy-example

 - [ ] Create and apply the infinite-calls.yaml to the cluster

	   kubectl apply -f infinite-calls-nginx.yaml --namespace=toy-example

 - [ ] Check the current running pods in the toy-example namespace

	   kubectl get pods -n toy-example

 - [ ] Check the deployment and service of the pod

	   kubectl get deployments -n toy-example
	   kubectl get service -n toy-example

## Deploy a simple mongodb application

 - [ ] Create the following manifest file with an IDE to toy-example
       folder

	    apiVersion: apps/v1
	    kind: Deployment
	    metadata:
	      name: mongodb-deployment
	      labels:
	        app: mongodb
	    spec:
	      replicas: 1
	      selector:
	        matchLabels:
	          app: mongodb
	      template:
	        metadata:
	          labels:
	            app: mongodb
	        spec:
	          containers:
	          - name: mongodb
	            image: mongo
	            ports:
	            - containerPort: 27017
	    ---
	    apiVersion: v1
	    kind: Service
	    metadata:
	      name: mongodb-service
	    spec:
	      selector:
	        app: mongodb
	      ports:
	        - protocol: TCP
	          port: 27017
	          targetPort: 27017 

 - [ ] Apply the manifest file to the K8s cluster

	   kubectl apply -f mongodb_app.yaml --namespace=toy-example
  
  

 - [ ] Check the pod, deployment and service of the mongodb application

	   kubectl get deployments -n toy-example
	   kubectl get service -n toy-example
	   kubectl get pods -n toy-example

## Deploy a simple nodejs Hello World application with 5 replicasets

In this part, we deploy a simple nodejs Hello World application that has only a Deployment Kubernetes kind in the manifest file and is configured to create 5 pods of the same application.

 - [ ] Apply it in the K8s cluster:

	   kubectl apply -f https://k8s.io/examples/service/load-balancer-example.yaml --namespace=toy-example
 
 

 - [ ] Check the Pod, Deployment, Service and Replicasets of the nodejs
       application

	   kubectl get deployments -n toy-example
	   kubectl get service -n toy-example
	   kubectl get pods -n toy-example
	   kubectl get replicasets -n toy-example
    
 We will notice that there is no Service related to this application. Every Deployment kind always creates a Pod (1 or more depending the value of Replicasets). To expose the application to the outside world a Service kind is needed.

 - [ ] Create a Service object that exposes the deployment:

	   kubectl expose deployment hello-world -n toy-example --type=LoadBalancer --name=my-nodejs-service
    
 > **Note:**  hello-world is the name of the Deployment and my-nodejs-service is the name of the Service
 
 > **Note:**  kubectl apply -f command creates and deployes a file which is either in the web (online in a repo) or in a host folder. To delete a deployed application we use `kubectl delete -f applicaition_name.yaml` When we want to delete a yaml file we deployed from the host computer we must be on the same folder this file exists. Then we can execute the kubectl delete command. 

