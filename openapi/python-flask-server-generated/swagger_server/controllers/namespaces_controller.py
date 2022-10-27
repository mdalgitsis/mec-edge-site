import connexion
import six

from swagger_server.models.deployment import Deployment  # noqa: E501
from swagger_server.models.limit_range import LimitRange  # noqa: E501
from swagger_server.models.namespace import Namespace  # noqa: E501
from swagger_server.models.pod import Pod  # noqa: E501
from swagger_server.models.resource_quota import ResourceQuota  # noqa: E501
from swagger_server.models.scale_horizontal import ScaleHorizontal  # noqa: E501
from swagger_server.models.scale_vertical import ScaleVertical  # noqa: E501
from swagger_server.models.service import Service  # noqa: E501
from swagger_server.models.service_monitor import ServiceMonitor  # noqa: E501
from swagger_server import util


def add_namespace(body):  # noqa: E501
    """Create a Namespace

    Create a Namespace # noqa: E501

    :param body: Namespace object that contains the name to create a Namespace
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Namespace.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_deployment(body, namespace_name):  # noqa: E501
    """Create a Deployment in a specific namespace

    Create a namespaced Deployment Kubernetes-resource # noqa: E501

    :param body: Deployment object that needs to be added to create a Deployment-resource in the cluster. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.  Also, replicas_number must be &gt;&#x3D; 1 and deployment_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;.
    :type body: dict | bytes
    :param namespace_name: name of Namespace to create a Deployment
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Deployment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_limit_range(body, namespace_name):  # noqa: E501
    """Create a LimitRange in a specific namespace

    Create a namespaced LimitRange Kubernetes-resource # noqa: E501

    :param body: LimitRanges pose default cpu and memory resource reservation in the specified namespaces.
    :type body: dict | bytes
    :param namespace_name: name of namespace to create a LimitRange
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = LimitRange.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_pod(body, namespace_name):  # noqa: E501
    """Create a Pod in a Namespace

    Create a Pod in a specific Namespace # noqa: E501

    :param body: Pod object that contains the key-value pairs to create a pod. **Note:** pod_name for good practices should contain only lowercase alphanumeric characters with or without &#x27;-&#x27;
    :type body: dict | bytes
    :param namespace_name: name of Namespace to create a Pod
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Pod.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_resource_quota(body, namespace_name):  # noqa: E501
    """Create a ResourceQuota in a specific namespace

    Create a namespaced ResourceQuota Kubernetes-resource # noqa: E501

    :param body: Resourcequotas reserve cpu,memory and storage resources in the specified namespaces.
    :type body: dict | bytes
    :param namespace_name: name of namespace to create a ResourceQuota
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = ResourceQuota.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_service(body, namespace_name):  # noqa: E501
    """Create a Service in a specific namespace

    Create a namespaced Service Kubernetes-resource # noqa: E501

    :param body: Service object that needs to be added to expose Pod-resources in or out the cluster. **Note:** service_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;.  The Service selector should match the label of the pod. The Service targetPort should match the container_port of the container inside the Pod. If service_type is ClusterIP, nodePort value must be set null in the service_port variable. Finally port_name is also optional.
    :type body: dict | bytes
    :param namespace_name: name of namespace to create a Service
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = Service.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def add_namespaced_service_monitor(body, namespace_name):  # noqa: E501
    """Create a ServiceMonitor in a specific namespace

    Create a namespaced ServiceMonitor Custom Kubernetes-resource # noqa: E501

    :param body: ServiceMonitor Custom object that needs to be added to expose Pod-resources in the Prometheus server. **Note:** service_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;.  The Service selector should match the label of the pod. The endpoints should match the Service port names. A release label must exist wit the value of the Prometheus name. If Prometheus is installed by a helm chart, the release value is the helm release name.
    :type body: dict | bytes
    :param namespace_name: name of namespace to create a ServiceMonitor
    :type namespace_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = ServiceMonitor.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_namespace(namespace_name):  # noqa: E501
    """Delete a Namespace

    Delete a Namespace # noqa: E501

    :param namespace_name: name of Namespace to delete
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_deployment(namespace_name, deployment_name):  # noqa: E501
    """Delete a namespaced Deployment

    Delete a namespaced Deployment # noqa: E501

    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to delete
    :type deployment_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_limit_range(namespace_name, limitrange_name):  # noqa: E501
    """Delete a namespaced LimitRange

    Delete a namespaced LimitRange # noqa: E501

    :param namespace_name: name of namespace where the LimitRange lives
    :type namespace_name: str
    :param limitrange_name: name of LimitRange to delete
    :type limitrange_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_pod(namespace_name, pod_name):  # noqa: E501
    """Delete a Pod from a specific Namespace

    Delete a namespaced Pod # noqa: E501

    :param namespace_name: name of Namespace where the Pod lives
    :type namespace_name: str
    :param pod_name: name of Pod to delete
    :type pod_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_resource_quota(namespace_name, resourcequota_name):  # noqa: E501
    """Delete a namespaced ResourceQuota

    Delete a namespaced ResourceQuota # noqa: E501

    :param namespace_name: name of namespace where the ResourceQuota lives
    :type namespace_name: str
    :param resourcequota_name: name of ResourceQuota to delete
    :type resourcequota_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_service(namespace_name, service_name):  # noqa: E501
    """Delete a namespaced Service

    Delete a namespaced Service # noqa: E501

    :param namespace_name: name of namespace where the Service lives
    :type namespace_name: str
    :param service_name: name of Service to delete
    :type service_name: str

    :rtype: None
    """
    return 'do some magic!'


def delete_namespaced_service_monitor(namespace_name, servicemonitor_name):  # noqa: E501
    """Delete a namespaced ServiceMonitor

    Delete a namespaced ServiceMonitor # noqa: E501

    :param namespace_name: name of namespace where the ServiceMonitor lives
    :type namespace_name: str
    :param servicemonitor_name: name of ServiceMonitor to delete
    :type servicemonitor_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_deployment(namespace_name, deployment_name):  # noqa: E501
    """Read a namespaced Deployment definition

    Returns the definition of a single Deployment by deployment_name in a specific namespace # noqa: E501

    :param namespace_name: name of Namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to retrieve
    :type deployment_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_deployment_resources(namespace_name, deployment_name):  # noqa: E501
    """Read namespaced Deployment resources

    Read resources in terms of CPU and memory of the specified Deployment # noqa: E501

    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to show the resources
    :type deployment_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_deployment_scale_replicas(namespace_name, deployment_name):  # noqa: E501
    """Read namespaced Deployment Scale replicas

    Read replicas of the Scale definition of the specified Deployment # noqa: E501

    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to show the number of replicas
    :type deployment_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_deployment_status(namespace_name, deployment_name):  # noqa: E501
    """Read namespaced Deployment status

    Read status of the specified Deployment # noqa: E501

    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to show its status
    :type deployment_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_deployments(namespace_name):  # noqa: E501
    """List Deployments of a specific Namespace

    Returns a list with the names of the Deployments of a specific namespace # noqa: E501

    :param namespace_name: name of Namespace to retrieve the Deployment-resources
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_limit_range(namespace_name, limitrange_name):  # noqa: E501
    """Read a namespaced LimitRange definition

    Returns the definition of a single LimitRange by limitrange_name in a specific namespace # noqa: E501

    :param namespace_name: name of namespace where the LimitRange lives
    :type namespace_name: str
    :param limitrange_name: name of LimitRange to retrieve
    :type limitrange_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_limit_ranges(namespace_name):  # noqa: E501
    """List LimitRanges by namespace

    Returns a list with all the LimitRanges in a specific namespace # noqa: E501

    :param namespace_name: name of namespace to retrieve the LimitRanges
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_pod_logs(namespace_name, pod_name):  # noqa: E501
    """Get logs of a namespaced Pod

    Get logs of a namespaced Pod # noqa: E501

    :param namespace_name: name of Namespace where the pod lives
    :type namespace_name: str
    :param pod_name: name of Pod to return the logs
    :type pod_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_pods(namespace_name):  # noqa: E501
    """List Pods by Namespace

    Returns a list with all the Pods in a specific Namespace # noqa: E501

    :param namespace_name: name of Namespace to retrieve the Pods
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_resource_quota(namespace_name, resourcequota_name):  # noqa: E501
    """Read a namespaced ResourceQuota definition

    Returns the definition of a single ResourceQuota by resourcequota_name in a specific namespace # noqa: E501

    :param namespace_name: name of namespace where the ResourceQuota lives
    :type namespace_name: str
    :param resourcequota_name: name of ResourceQuota to retrieve
    :type resourcequota_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_resource_quotas(namespace_name):  # noqa: E501
    """List ResourceQuotas by namespace

    Returns a list with all the ResourceQuotas in a specific namespace # noqa: E501

    :param namespace_name: name of namespace to retrieve the ResourceQuotas
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_service(namespace_name, service_name):  # noqa: E501
    """Read a namespaced Service definition

    Returns the definition of a single Service by service_name in a specific namespace # noqa: E501

    :param namespace_name: name of namespace where the Service lives
    :type namespace_name: str
    :param service_name: name of Service to retrieve
    :type service_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_service_monitor(namespace_name, servicemonitor_name):  # noqa: E501
    """Read a namespaced ServiceMonitor definition

    Returns the definition of a single ServiceMonitor by servicemonitor_name in a specific namespace # noqa: E501

    :param namespace_name: name of namespace where the ServiceMonitor lives
    :type namespace_name: str
    :param servicemonitor_name: name of ServiceMonitor to retrieve
    :type servicemonitor_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_service_monitors(namespace_name):  # noqa: E501
    """List ServiceMonitors by namespace

    Returns a list with all the ServiceMonitors in a specific namespace # noqa: E501

    :param namespace_name: name of namespace to retrieve the ServiceMonitors
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_service_status(namespace_name, service_name):  # noqa: E501
    """Read namespaced Service status

    Read the status of the specified Service, like the Internal service IP, the External Service IP, the service ports and the service type. # noqa: E501

    :param namespace_name: name of namespace where the Service lives
    :type namespace_name: str
    :param service_name: name of Service to show its status
    :type service_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaced_services(namespace_name):  # noqa: E501
    """List Services by namespace

    Returns a list with all the Services in a specific namespace # noqa: E501

    :param namespace_name: name of namespace to retrieve the Services
    :type namespace_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_namespaces():  # noqa: E501
    """List all Namespaces

    Returns a list of all Namespaces in the cluster # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def scale_horizontal_namespaced_deployment(body, namespace_name, deployment_name):  # noqa: E501
    """Scale Horizontal a namespaced Deployment

    Scale either up or down the pods of a namespaced Deployment # noqa: E501

    :param body: Scale Horizontal object that needs to be added to a namespaced Deployment in order to scale up or down the pods (containers) it contains. **Note:** if replicas_number &#x3D; 0, then we kill all the pods of the Deployment.
    :type body: dict | bytes
    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to scale horizontically
    :type deployment_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScaleHorizontal.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def scale_vertical_namespaced_deployment(body, namespace_name, deployment_name, container_name):  # noqa: E501
    """Scale Vertical a namespaced Deployment

    Partialy update a namespaced Deployment - Vertical scaling. The update affects the pod-container resources such as CPU and memory. # noqa: E501

    :param body: ScaleVertical object that needs to be added to a namespaced Deployment in the cluster to perform vertical scaling. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.
    :type body: dict | bytes
    :param namespace_name: name of namespace where the Deployment lives
    :type namespace_name: str
    :param deployment_name: name of Deployment to scale vertically
    :type deployment_name: str
    :param container_name: name of container of the Deployment to scale vertically
    :type container_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = ScaleVertical.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
