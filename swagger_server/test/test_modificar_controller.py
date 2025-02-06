# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_bloquear_contacto import RequestBloquearContacto  # noqa: E501
from swagger_server.models.request_bloquear_usuario import RequestBloquearUsuario  # noqa: E501
from swagger_server.models.request_modificar_contacto import RequestModificarContacto  # noqa: E501
from swagger_server.models.request_modificar_usuario import RequestModificarUsuario  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server.test import BaseTestCase


class TestModificarController(BaseTestCase):
    """ModificarController integration test stubs"""

    def test_put_bloqcontact(self):
        """Test case for put_bloqcontact

        
        """
        body = RequestBloquearContacto()
        response = self.client.open(
            '/put/modify/bloquear_contacto',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_bloqusuario(self):
        """Test case for put_bloqusuario

        
        """
        body = RequestBloquearUsuario()
        response = self.client.open(
            '/put/modify/bloquear_usuario',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_contacto(self):
        """Test case for put_contacto

        
        """
        body = RequestModificarContacto()
        response = self.client.open(
            '/put/modify/contacto',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_usuario(self):
        """Test case for put_usuario

        
        """
        body = RequestModificarUsuario()
        response = self.client.open(
            '/put/modify/usuarios',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
