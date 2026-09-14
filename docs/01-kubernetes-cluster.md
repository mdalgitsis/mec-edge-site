# Set up a K8s cluster

A K8s cluster is composed of many nodes, which can be splitted into two types:

- The master node, which hosts the K8s control plane that controls and manages the whole K8s system
- The worker nodes that run the actual applications which are deployed

The more efficient way to a fully functioning Kubernetes cluster is by using kubeadm. kubeadm is a tool that sets up a single or multi-node cluster that is great for both testing Kubernetes and developing apps in bare-metal implementations. Also, it is a manual cluster installation that helps us to configure it in that way to be compliant with OSM. Other possible methods  to set up a K8s cluster can be found [here](https://itnext.io/kubernetes-installation-methods-the-complete-guide-1036c860a2b3) .

## Create a K8s cluster

To create a K8s cluster on a bare-metal or virtual machine, a container runtime, the kubelet, kubectl, and kubeadm tool must be installed. 

A container runtime, also known as container engine, is a software component that can run containers on a host operating system. Docker (Containerd) is the leading container system, offering a full suite of features, with free or paid options. It is the default Kubernetes container runtime, providing image specifications, a command-line interface (CLI) and a container image-building service. 

The kubelet, in Kubernetes, is an agent that runs on every computing node and receives commands specifying what containers should be running, and relays them to a container runtime on the node. It also collects information from the container runtime about currently running containers, and passes it back to the Kubernetes control plane.

kubectl is the command line tool for communicating with a Kubernetes cluster's control plane and kubeadm, as described above, is the tool to set-up a K8s cluster.

## Container runtime installation

 - [ ] Getting the Docker gpg key to install docker:

       curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

 - [ ] Add the Docker Ubuntu repository:

       sudo apt-get update
       sudo apt-get install ca-certificates curl gnupg lsb-release
       curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
       echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

 - [ ] Update the packages:

       sudo apt-get update

 - [ ] Install docker and docker components:

       sudo apt-get install -y docker-ce docker-ce-cli containerd.io

## Kubernetes components installation (kubelet, kubectl, kubeadm)

> **⚠️ These two commands no longer work.** The Google-hosted Kubernetes apt repository
> (`apt.kubernetes.io` / `packages.cloud.google.com/apt`) was **deprecated in 2023 and has since been switched
> off** — `https://apt.kubernetes.io/dists/kubernetes-xenial/Release` now returns 404, so `apt-get update` fails
> and nothing installs. `apt-key` is also deprecated on modern Debian/Ubuntu.
>
> The replacement is the community-hosted `pkgs.k8s.io`, with the key stored in a keyring rather than `apt-key`.
> Pick the minor version you want — the repository is versioned, so there is no "latest" across minors:
>
> ```bash
> K8S_MINOR=v1.31
> sudo mkdir -p /etc/apt/keyrings
> curl -fsSL "https://pkgs.k8s.io/core:/stable:/${K8S_MINOR}/deb/Release.key" \
>   | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
> echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/${K8S_MINOR}/deb/ /" \
>   | sudo tee /etc/apt/sources.list.d/kubernetes.list
> sudo apt-get update
> ```
>
> The original 2022 commands are kept below for the record.

 - [ ] Get the Kubernetes gpg key:

       curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

 - [ ] Add the Kubernetes repository:

       cat << EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list deb https://apt.kubernetes.io/ kubernetes-xenial main EOF

 - [ ] Update the packages:
    
       sudo apt-get update

 - [ ] Install kubelet, kubeadm, and kubectl with the latest or a
       specific version:

       sudo apt-get install -y kubelet=1.20.11-00 kubeadm=1.20.11-00 kubectl=1.20.11-00
   

 - [ ] Hold them at the current version:

       sudo apt-mark hold kubelet kubeadm kubectl

## kubeadm cluster initiation

 - [ ] Beforehand swappoff the swapp memory

	   sudo swapoff -a

 - [ ] Initialize the kubeadm cluster

	   sudo kubeadm init --pod-network-cidr=10.244.0.0/16

 - [ ] Set up local kubeconfig

	   mkdir -p $HOME/.kube
	   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
	   sudo chown $(id -u):$(id -g) $HOME/.kube/config

> **Note:** In ~/.kube/config lies K8s cluster configuration file. This file will be neccessary later to add the K8s cluster to OSM

 - [ ] Apply Flannel CNI network overlay

	   kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

Since we want to follow an all-in-one node approach, we have to schedule pods in the master. 

 - [ ] Untaint the master:

	   kubectl taint nodes --all node-role.kubernetes.io/master-

## Cluster requirements for OSM integration
The K8s cluster to be added later on and integrates with OSM must fullfil the following requirements:

- installation and configuration of a load balancer for the cluster
- installation of a persistent volume storage (openebs) and define it as the default storageclass
- a Tiller permission, per the OSM documentation - but read the warning below before applying it

Metallb is a very powerful, easy to configure, load balancer for kubernetes. 

 - [ ] Apply the following k8s manifest to install it in the cluster:

	   kubectl apply -f https://raw.githubusercontent.com/google/metallb/v0.8.3/manifests/metallb.yaml

After the installation, metallb has to be configured. The configuration of metallb in layer2 is via a Configmap kind manifest. Thus a configuration_metallb.yaml file has to be created (e.g in an IDE program) and has to be applied in the cluster
The configmap kind manifest looks like this:
```

apiVersion: v1

kind: ConfigMap

metadata:

namespace: metallb-system

name: config

data:

config: |

address-pools:

- name: default

protocol: layer2

addresses:

- 172.21.248.20-172.21.248.250

```
> **Note:** Visual studio code is an efficient IDE to syntax yaml manifests

> **⚠️ This ConfigMap format no longer works on current MetalLB.** It was removed in **v0.13.0** (2022) and
> replaced by the `IPAddressPool` and `L2Advertisement` custom resources. Applying the ConfigMap to a modern
> MetalLB is silently ignored — the install looks fine and your `LoadBalancer` services simply stay `<pending>`.
> Use [`manifests/metallb/ipaddresspool.yaml`](../manifests/metallb/ipaddresspool.yaml) instead; the original
> ConfigMap is kept as [`configmap-legacy.yaml`](../manifests/metallb/configmap-legacy.yaml) for MetalLB ≤ 0.12.

 - [ ] Create the configuration_metallb.yaml file
 - [ ] Apply the file into the cluster:

	   kubectl apply -f configuration_metallb.yaml

> **Note:** We should ensure that the range of IP address defined in metallb are accessible from outside the cluster and is not overlapped with other devices in that network. Also this network should be reachable from OSM since OSM will need it to communicate with the cluster.

 - [ ] Next, apply a kubernetes persistent volume storage with the
       following manifest:

	   kubectl apply -f https://openebs.github.io/charts/openebs-operator.yaml

 - [ ] Check if there is a default storageclass in the cluster after
       the installation:

	   kubectl get storageclass
	   

 - [ ] Until now, there is not default storageclass defined.  Define
       openebs-hostpath as default storageclass with the command below:

       kubectl patch storageclass openebs-hostpath -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

 - [ ] Confrim the default starageclass and check the results:

	   kubectl get storageclass

 - [ ] For Kubernetes clusters > 1.15 the OSM documentation asks for a
       Tiller permission, added with:

	   kubectl create clusterrolebinding tiller-cluster-admin --clusterrole=cluster-admin --serviceaccount=kube-system:default

> **⚠️ Do not run this without understanding it.** This grants `cluster-admin` to the **default ServiceAccount in
> `kube-system`**. Every pod scheduled into `kube-system` that does not name its own ServiceAccount then runs with
> full cluster privileges. It was the shortcut Helm 2 deployments copy-pasted, and it is a privilege escalation
> waiting to happen.
>
> **It is also very likely unnecessary.** Tiller was Helm **v2**'s in-cluster component and was removed entirely
> in Helm v3 (November 2019). OSM Release ELEVEN — the release installed in
> [the OSM integration guide](05-osm-integration.md) — uses Helm v3, and this guide installs `helm-v3.6.2`
> further on. The requirement appears to be vestigial text carried forward in the OSM documentation, where it is
> still listed as of Release THIRTEEN.
>
> Try registering the cluster **without** it first. If `osm k8scluster-add` succeeds, you never needed it. If you
> do need to grant something, bind a dedicated ServiceAccount with the narrowest role that works rather than
> handing `cluster-admin` to `kube-system:default`.

## K8s cluster basic configuration

At this point we have a full-functioning K8s cluster. To obtain more information of the cluster, the running Nodes and Pods, we can execute the following commands. As we can see, all commands use kubectl, the command line communication tool for the K8s cluster.

 - [ ] Obtain information for the cluster

	   kubectl cluster-info

 - [ ] List the running Nodes (option `-o wide` gives more info)

	  `kubectl get nodes` or `kubectl get nodes -o wide`

 - [ ] List all the running Pods in all the Namespaces

	 `kubectl get pods --all-namespaces` or `kubectl get pods -A`

 - [ ] List the Namespaces of the cluster

	   kubectl get namespaces

 - [ ] Create a Namespace with a spesific name, for example bind5g

	   kubectl create namespace bind5g

 - [ ] Make a namespace the default working Namespace

	   kubectl config set-context --current --namespace=bind5g

 - [ ] By default the K8s cluster has already a Namespace called
       *default*. To return back to default Namespace we simply run again the same command:

	   kubectl config set-context --current --namespace=bind5g

 - [ ] Delete the Namespace bind5g

	   kubectl delete namespace bind5g

Additional docker related commands to obtain inormation for the containers running in the cluster (optional):

 - [ ] List the running containers

	   sudo docker ps

 - [ ] List the running and stopped containers

	   sudo docker ps -a

 - [ ] List containers filtered with a specific status

	   docker ps -f "status=exited"

