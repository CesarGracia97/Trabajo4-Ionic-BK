# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_lista_contactos import RequestListaContactos  # noqa: E501
from swagger_server.models.request_lista_usuarios import RequestListaUsuarios  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server.test import BaseTestCase


class TestLecturaController(BaseTestCase):
    """LecturaController integration test stubs"""

    def test_get_read_contactos(self):
        """Test case for get_read_contactos

        
        """
        body = RequestListaContactos()
        response = self.client.open(
            '/get/queries/listar_contactos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_read_usuarios(self):
        """Test case for get_read_usuarios

        
        """
        body = RequestListaUsuarios()
        response = self.client.open(
            '/get/queries/listar_usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
