# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestClusterController(BaseTestCase):
    """ClusterController integration test stubs"""

    def test_get_all_deployments(self):
        """Test case for get_all_deployments

        List Deployments for all Namespaces
        """
        response = self.client.open(
            '/cluster/deployments',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_limit_ranges(self):
        """Test case for get_all_limit_ranges

        List LimitRanges for all Namespaces
        """
        response = self.client.open(
            '/cluster/limitranges',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_pods(self):
        """Test case for get_all_pods

        List Pods for all Namespaces
        """
        response = self.client.open(
            '/cluster/pods',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_resource_quotas(self):
        """Test case for get_all_resource_quotas

        List ResourceQuotas for all Namespaces
        """
        response = self.client.open(
            '/cluster/resourcequotas',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_service_monitors(self):
        """Test case for get_all_service_monitors

        List ServiceMonitors for all Namespaces
        """
        response = self.client.open(
            '/cluster/servicemonitors',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_services(self):
        """Test case for get_all_services

        List Services for all Namespaces
        """
        response = self.client.open(
            '/cluster/services',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_node_status(self):
        """Test case for get_node_status

        Get a specific Node
        """
        response = self.client.open(
            '/cluster/nodes/{node_name}/status'.format(node_name='node_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_nodes(self):
        """Test case for get_nodes

        List the existing Nodes of the cluster
        """
        response = self.client.open(
            '/cluster/nodes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
