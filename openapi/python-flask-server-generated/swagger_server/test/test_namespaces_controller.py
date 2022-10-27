# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.deployment import Deployment  # noqa: E501
from swagger_server.models.limit_range import LimitRange  # noqa: E501
from swagger_server.models.namespace import Namespace  # noqa: E501
from swagger_server.models.pod import Pod  # noqa: E501
from swagger_server.models.resource_quota import ResourceQuota  # noqa: E501
from swagger_server.models.scale_horizontal import ScaleHorizontal  # noqa: E501
from swagger_server.models.scale_vertical import ScaleVertical  # noqa: E501
from swagger_server.models.service import Service  # noqa: E501
from swagger_server.models.service_monitor import ServiceMonitor  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNamespacesController(BaseTestCase):
    """NamespacesController integration test stubs"""

    def test_add_namespace(self):
        """Test case for add_namespace

        Create a Namespace
        """
        body = Namespace()
        response = self.client.open(
            '/namespaces',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_deployment(self):
        """Test case for add_namespaced_deployment

        Create a Deployment in a specific namespace
        """
        body = Deployment()
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_limit_range(self):
        """Test case for add_namespaced_limit_range

        Create a LimitRange in a specific namespace
        """
        body = LimitRange()
        response = self.client.open(
            '/namespaces/{namespace_name}/limitranges'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_pod(self):
        """Test case for add_namespaced_pod

        Create a Pod in a Namespace
        """
        body = Pod()
        response = self.client.open(
            '/namespaces/{namespace_name}/pods'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_resource_quota(self):
        """Test case for add_namespaced_resource_quota

        Create a ResourceQuota in a specific namespace
        """
        body = ResourceQuota()
        response = self.client.open(
            '/namespaces/{namespace_name}/resourcequotas'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_service(self):
        """Test case for add_namespaced_service

        Create a Service in a specific namespace
        """
        body = Service()
        response = self.client.open(
            '/namespaces/{namespace_name}/services'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_add_namespaced_service_monitor(self):
        """Test case for add_namespaced_service_monitor

        Create a ServiceMonitor in a specific namespace
        """
        body = ServiceMonitor()
        response = self.client.open(
            '/namespaces/{namespace_name}/servicemonitors'.format(namespace_name='namespace_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespace(self):
        """Test case for delete_namespace

        Delete a Namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}'.format(namespace_name='namespace_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_deployment(self):
        """Test case for delete_namespaced_deployment

        Delete a namespaced Deployment
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_limit_range(self):
        """Test case for delete_namespaced_limit_range

        Delete a namespaced LimitRange
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/limitranges/{limitrange_name}'.format(namespace_name='namespace_name_example', limitrange_name='limitrange_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_pod(self):
        """Test case for delete_namespaced_pod

        Delete a Pod from a specific Namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/pods/{pod_name}'.format(namespace_name='namespace_name_example', pod_name='pod_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_resource_quota(self):
        """Test case for delete_namespaced_resource_quota

        Delete a namespaced ResourceQuota
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/resourcequotas/{resourcequota_name}'.format(namespace_name='namespace_name_example', resourcequota_name='resourcequota_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_service(self):
        """Test case for delete_namespaced_service

        Delete a namespaced Service
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/services/{service_name}'.format(namespace_name='namespace_name_example', service_name='service_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_namespaced_service_monitor(self):
        """Test case for delete_namespaced_service_monitor

        Delete a namespaced ServiceMonitor
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/servicemonitors/{servicemonitor_name}'.format(namespace_name='namespace_name_example', servicemonitor_name='servicemonitor_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_deployment(self):
        """Test case for get_namespaced_deployment

        Read a namespaced Deployment definition
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_deployment_resources(self):
        """Test case for get_namespaced_deployment_resources

        Read namespaced Deployment resources
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}/resources'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_deployment_scale_replicas(self):
        """Test case for get_namespaced_deployment_scale_replicas

        Read namespaced Deployment Scale replicas
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}/replicas'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_deployment_status(self):
        """Test case for get_namespaced_deployment_status

        Read namespaced Deployment status
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}/status'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_deployments(self):
        """Test case for get_namespaced_deployments

        List Deployments of a specific Namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_limit_range(self):
        """Test case for get_namespaced_limit_range

        Read a namespaced LimitRange definition
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/limitranges/{limitrange_name}'.format(namespace_name='namespace_name_example', limitrange_name='limitrange_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_limit_ranges(self):
        """Test case for get_namespaced_limit_ranges

        List LimitRanges by namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/limitranges'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_pod_logs(self):
        """Test case for get_namespaced_pod_logs

        Get logs of a namespaced Pod
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/pods/{pod_name}/logs'.format(namespace_name='namespace_name_example', pod_name='pod_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_pods(self):
        """Test case for get_namespaced_pods

        List Pods by Namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/pods'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_resource_quota(self):
        """Test case for get_namespaced_resource_quota

        Read a namespaced ResourceQuota definition
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/resourcequotas/{resourcequota_name}'.format(namespace_name='namespace_name_example', resourcequota_name='resourcequota_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_resource_quotas(self):
        """Test case for get_namespaced_resource_quotas

        List ResourceQuotas by namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/resourcequotas'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_service(self):
        """Test case for get_namespaced_service

        Read a namespaced Service definition
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/services/{service_name}'.format(namespace_name='namespace_name_example', service_name='service_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_service_monitor(self):
        """Test case for get_namespaced_service_monitor

        Read a namespaced ServiceMonitor definition
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/servicemonitors/{servicemonitor_name}'.format(namespace_name='namespace_name_example', servicemonitor_name='servicemonitor_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_service_monitors(self):
        """Test case for get_namespaced_service_monitors

        List ServiceMonitors by namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/servicemonitors'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_service_status(self):
        """Test case for get_namespaced_service_status

        Read namespaced Service status
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/services/{service_name}/status'.format(namespace_name='namespace_name_example', service_name='service_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaced_services(self):
        """Test case for get_namespaced_services

        List Services by namespace
        """
        response = self.client.open(
            '/namespaces/{namespace_name}/services'.format(namespace_name='namespace_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_namespaces(self):
        """Test case for get_namespaces

        List all Namespaces
        """
        response = self.client.open(
            '/namespaces',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scale_horizontal_namespaced_deployment(self):
        """Test case for scale_horizontal_namespaced_deployment

        Scale Horizontal a namespaced Deployment
        """
        body = ScaleHorizontal()
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}/scaleHorizontal'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_scale_vertical_namespaced_deployment(self):
        """Test case for scale_vertical_namespaced_deployment

        Scale Vertical a namespaced Deployment
        """
        body = ScaleVertical()
        response = self.client.open(
            '/namespaces/{namespace_name}/deployments/{deployment_name}/{container_name}/scaleVertical'.format(namespace_name='namespace_name_example', deployment_name='deployment_name_example', container_name='container_name_example'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
