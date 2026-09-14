# OSM integration


## Installing OSM

[OSM installation](https://osm.etsi.org/docs/user-guide/03-installing-osm.html) is based on a K8s cluster deployment. OSM installer creates by default a K8s cluster and inside of it creates a Namespace *osm*. Under the Namespace *osm* lies OSM with its elements. Some of these elements are OSM CLI, OSM GUI, MON, Prometheus, and Grafana.

 - [ ] Commands for installing OSM:

	   wget https://osm-download.etsi.org/ftp/osm-11.0-eleven/install_osm.sh
	   chmod +x install_osm.sh
	   ./install_osm.sh

 - [ ] After the installation is finished, list all the OSM elements
       with:
   
	   kubectl get all -n osm

 - [ ] To browse into the OSM GUI with your preferred browser, use the
       IP of the output of the following command:

	   kubectl get service/ng-ui -n osm 

> **Note:** The credentials for the OSM GUI are username: admin, password: admin

## Monitoring an OSM installation

MON is an element to monitor VMs in NFVI and VNFs. The metrics from NFVI are collected through the VIM and the metrics from NFVs are collected through VCA (VNF Configuration and Abstraction). Metrics need to be defined on VNF descriptors for MON to collect them.

OSM installation can include add-ons (extra components), if options are added on the installation command. For example, to install OSM with the k8s_monitor add-on use the command  `./install_osm.sh --k8s_monitor`

> **Note:** It is suggested though by OSM community not to follow an OSM installation with the k8s_monitor add-on. It is advised users to follow the method that is described below

 - [ ] Install OSM without the monitoring option
 - [ ] Clone the master branch of the OSM devops repo

	   git clone http://osm.etsi.org/gerrit/osm/devops.git

 - [ ] Install the monitoring component

	   devops/installers/k8s/install_osm_k8s_monitoring.sh

 - [ ] Update the OSM Grafana configuration (name of a datasource)

       kubectl -n osm apply -f devops/installers/docker/osm_pods/grafana.yaml

 - [ ] Restart the Grafana pod to take changes

       export GRAFANA_POD=$(kubectl get pods -n osm -l "app=grafana" -o jsonpath="{.items[0].metadata.name}")
       kubectl -n osm delete pod $GRAFANA_POD

k8s_monitor add-on is for adding some components to monitor the K8s cluster hosting OSM, not VNFs or KNFs. You'll get those additional components in the *monitoring* Namespace, and not in the *osm* Namespace. It uses Prometheus operator, node exporter and other exporters for mysql and mongo. OSM without add-ons installation comes by default with another Prometheus server, and a Grafana instance (as pods) in the *osm* Namespace.

 - [ ] Check where Prometheus of *osm* Namespace is listening to and
       browse the GUI with your preferred browser

	   kubctl get service -n osm

 - [ ] Check where Grafana of *osm* Namespace is listening to and browse
       the GUI with your preferred browser

	   kubctl get service -n osm
	   
> **Note:** The credentials for Grafana GUI are username: admin, password: admin

 - [ ] Check where Prometheus of *monitoring* Namespace is listening to
       and browse the GUI with your preferred browser

	   kubctl get service -n monitoring

> **Note:** --k8s_monitor add-on installs another Prometheus server to monitor the cluster that hosts OSM in the *monitoring* namespace

## OSM configuration & integration with the K8s cluster

OSM ETSI framework can orchestrate virtual, containerized and hybrid network services. To achieve this VNFs and KNFs are needed. VNFs are running on VMs (or Virtual Deployment Units) and KNFs are running on containers (or Kubernetes Deployment Units). VMs are hosted/running in an NFVI and are managed by a virtual orchestration tool like Openstack (to be noted Openstack is more than that as it is a cloud operating system). Containers are hosted/running in a cloud native infrastructure (CNI) and are managed by a container orchestration tool like Kubernetes.

OSM ETSI framework interact with NVFI-VNFs and/or CNI-KNFs through another entity called VIM. Openstack itself can be considered as a VIM and can be added in the VIM list. Although Openstack itself can be considered as a VIM and can be added in the VIM list, a K8s cluster cannot. Thus, and to comply with OSM, a “Dummy” VIM must be created and listed. Therefore, an OSM-VIM(Dummy)-K8s connection is established with the following command on the OSM client: 

    osm vim-create --name bind5g-vim --user u --password p --tenant p --account_type dummy --auth_url http://localhost/dummy

where the options:
- -- name: Vim´s name, any name can be given
- --user: user´s name, any name can be given 
- --password: password´s name, any name can be given
- --tenant: tenant´s name, any name can be given
- --account_type: vim type, dummy name must be given
- --auth_url: vim´s url, a url has to be given even if it doesnt exist since dummy vim is not a phisical vim 

As a result, a K8s cluster can be deployed under or outside the VIM´s network. 

Under a VIM´s network the cluster is connected to OSM through the hosted VIM and is deployed following the instructions of Method 1 and 2 of [ANNEX 7: Kubernetes installation and requirements](https://osm.etsi.org/docs/user-guide/15-k8s-installation.html) of OSM´s official documentation.

Outside of the VIM´s network the cluster is connected to OSM through the Dummy VIM and is deployed as Annex 7, [Method 3: Manual cluster installation steps for Ubuntu](https://osm.etsi.org/docs/user-guide/15-k8s-installation.html).

Since, the K8s cluster of the MEC site is implemented following the Method 3, we can add the MEC/K8s cluster by executing the following command:

    osm k8scluster-add bind5g-cluster --creds /home/ubuntu/bind5g/k8s_cluster/config --vim bind5g-vim --k8s-nets '{k8s_net1: null }' --version 'v1.20.11' --description='K8s baremetal cluster’

where the options:
- --creds: path  to  k8s  config  file, the  /.kube/config file must be copied and pasted from the machine running the K8s cluster to the machine that runs OSM
- --vim: dummy vim´s name
- --k8s-nets: k8s_net1 is the name of K8s network and null is the nam eof the VIM´s network
- --version: verison of the K8s cluster, version of kubelet,kubectl,kubeadm
- --description: description of the K8s cluster

> **Note:** MEC/K8s cluster is where OSM will deploy KNFs, and it is NOT the K8s cluster on which OSM is installed

