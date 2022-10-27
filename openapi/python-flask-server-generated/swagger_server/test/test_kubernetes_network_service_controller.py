# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.kns import KNS  # noqa: E501
from swagger_server.models.kns_day2_actions import KNSDay2Actions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestKubernetesNetworkServiceController(BaseTestCase):
    """KubernetesNetworkServiceController integration test stubs"""

    def test_add_kns(self):
        """Test case for add_kns

        Create a Kubernetes Network Service
        """
        body = KNS()
        response = self.client.open(
            '/kns',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_kns(self):
        """Test case for delete_kns

        Delete a Kubernetes Network Service
        """
        response = self.client.open(
            '/kns/{kns_name}'.format(kns_name='kns_name_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_all_kns(self):
        """Test case for get_all_kns

        List Kubernetes Network Services
        """
        response = self.client.open(
            '/kns',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_kns(self):
        """Test case for get_kns

        Get a Kubernetes Network Service
        """
        response = self.client.open(
            '/kns/{kns_name}'.format(kns_name='kns_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_kns(self):
        """Test case for update_kns

        Day2Actions in a Kubernetes Network Service
        """
        body = KNSDay2Actions()
        query_string = [('nsd_name', 'nsd_name_example'),
                        ('vim_name', 'vim_name_example'),
                        ('k8s_namespace', 'k8s_namespace_example')]
        response = self.client.open(
            '/kns/{kns_name}/day2actions'.format(kns_name='kns_name_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
