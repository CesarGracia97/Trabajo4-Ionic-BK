# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.request_iniciar_sesion import RequestIniciarSesion  # noqa: E501
from swagger_server.models.request_recuperar_clave import RequestRecuperarClave  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSistemaController(BaseTestCase):
    """SistemaController integration test stubs"""

    def test_iniciar_sesion(self):
        """Test case for iniciar_sesion

        
        """
        body = RequestIniciarSesion()
        response = self.client.open(
            '/post/iniciar_sesion',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_recuperar_contrasena(self):
        """Test case for recuperar_contrasena

        
        """
        body = RequestRecuperarClave()
        response = self.client.open(
            '/post/recuperar_correo',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
