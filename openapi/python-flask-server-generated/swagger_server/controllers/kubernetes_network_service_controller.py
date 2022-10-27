import connexion
import six

from swagger_server.models.kns import KNS  # noqa: E501
from swagger_server.models.kns_day2_actions import KNSDay2Actions  # noqa: E501
from swagger_server import util


def add_kns(body):  # noqa: E501
    """Create a Kubernetes Network Service

    Create a KNS in OSM # noqa: E501

    :param body: Body request that contains the key-value pairs to create a KNS. **Note:** a note comes here
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = KNS.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_kns(kns_name):  # noqa: E501
    """Delete a Kubernetes Network Service

    Delete a KNS in OSM # noqa: E501

    :param kns_name: Name of the KNS
    :type kns_name: str

    :rtype: None
    """
    return 'do some magic!'


def get_all_kns():  # noqa: E501
    """List Kubernetes Network Services

    Returns a list with all the KNS running in OSM # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_kns(kns_name):  # noqa: E501
    """Get a Kubernetes Network Service

    Returns a KNS running in OSM # noqa: E501

    :param kns_name: Name of the KNS
    :type kns_name: str

    :rtype: None
    """
    return 'do some magic!'


def update_kns(body, nsd_name, vim_name, k8s_namespace, kns_name):  # noqa: E501
    """Day2Actions in a Kubernetes Network Service

    Performs Day2Actions in a KNS in OSM # noqa: E501

    :param body: Body request that contains the key-value pairs to update a KNS. **Note:** a note comes here
    :type body: dict | bytes
    :param nsd_name: Name of the ND Descriptor
    :type nsd_name: str
    :param vim_name: Name of the VIM
    :type vim_name: str
    :param k8s_namespace: Name of the Namespace in Kubernetes (K8s)
    :type k8s_namespace: str
    :param kns_name: Name of the KNS
    :type kns_name: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = KNSDay2Actions.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
