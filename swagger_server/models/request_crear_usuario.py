# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestCrearUsuario(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, contrasena: str=None, correo: str=None, name: str=None, cedula: str=None, contacto: str=None):  # noqa: E501
        """RequestCrearUsuario - a model defined in Swagger

        :param contrasena: The contrasena of this RequestCrearUsuario.  # noqa: E501
        :type contrasena: str
        :param correo: The correo of this RequestCrearUsuario.  # noqa: E501
        :type correo: str
        :param name: The name of this RequestCrearUsuario.  # noqa: E501
        :type name: str
        :param cedula: The cedula of this RequestCrearUsuario.  # noqa: E501
        :type cedula: str
        :param contacto: The contacto of this RequestCrearUsuario.  # noqa: E501
        :type contacto: str
        """
        self.swagger_types = {
            'contrasena': str,
            'correo': str,
            'name': str,
            'cedula': str,
            'contacto': str
        }

        self.attribute_map = {
            'contrasena': 'contrasena',
            'correo': 'correo',
            'name': 'name',
            'cedula': 'cedula',
            'contacto': 'contacto'
        }
        self._contrasena = contrasena
        self._correo = correo
        self._name = name
        self._cedula = cedula
        self._contacto = contacto

    @classmethod
    def from_dict(cls, dikt) -> 'RequestCrearUsuario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request_CrearUsuario of this RequestCrearUsuario.  # noqa: E501
        :rtype: RequestCrearUsuario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contrasena(self) -> str:
        """Gets the contrasena of this RequestCrearUsuario.


        :return: The contrasena of this RequestCrearUsuario.
        :rtype: str
        """
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str):
        """Sets the contrasena of this RequestCrearUsuario.


        :param contrasena: The contrasena of this RequestCrearUsuario.
        :type contrasena: str
        """
        if contrasena is None:
            raise ValueError("Invalid value for `contrasena`, must not be `None`")  # noqa: E501

        self._contrasena = contrasena

    @property
    def correo(self) -> str:
        """Gets the correo of this RequestCrearUsuario.


        :return: The correo of this RequestCrearUsuario.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """Sets the correo of this RequestCrearUsuario.


        :param correo: The correo of this RequestCrearUsuario.
        :type correo: str
        """
        if correo is None:
            raise ValueError("Invalid value for `correo`, must not be `None`")  # noqa: E501

        self._correo = correo

    @property
    def name(self) -> str:
        """Gets the name of this RequestCrearUsuario.


        :return: The name of this RequestCrearUsuario.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this RequestCrearUsuario.


        :param name: The name of this RequestCrearUsuario.
        :type name: str
        """

        self._name = name

    @property
    def cedula(self) -> str:
        """Gets the cedula of this RequestCrearUsuario.


        :return: The cedula of this RequestCrearUsuario.
        :rtype: str
        """
        return self._cedula

    @cedula.setter
    def cedula(self, cedula: str):
        """Sets the cedula of this RequestCrearUsuario.


        :param cedula: The cedula of this RequestCrearUsuario.
        :type cedula: str
        """
        if cedula is None:
            raise ValueError("Invalid value for `cedula`, must not be `None`")  # noqa: E501

        self._cedula = cedula

    @property
    def contacto(self) -> str:
        """Gets the contacto of this RequestCrearUsuario.


        :return: The contacto of this RequestCrearUsuario.
        :rtype: str
        """
        return self._contacto

    @contacto.setter
    def contacto(self, contacto: str):
        """Sets the contacto of this RequestCrearUsuario.


        :param contacto: The contacto of this RequestCrearUsuario.
        :type contacto: str
        """
        if contacto is None:
            raise ValueError("Invalid value for `contacto`, must not be `None`")  # noqa: E501

        self._contacto = contacto
