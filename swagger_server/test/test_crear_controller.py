# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_crear_contacto import RequestCrearContacto  # noqa: E501
from swagger_server.models.request_crear_usuario import RequestCrearUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCrearController(BaseTestCase):
    """CrearController integration test stubs"""

    def test_post_createcontacto(self):
        """Test case for post_createcontacto

        
        """
        body = RequestCrearContacto()
        response = self.client.open(
            '/post/create/contactos',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_post_createusuario(self):
        """Test case for post_createusuario

        
        """
        body = RequestCrearUsuario()
        response = self.client.open(
            '/post/create/usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
