# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestIniciarSesion(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, contrasena: str=None, correo: str=None):  # noqa: E501
        """RequestIniciarSesion - a model defined in Swagger

        :param contrasena: The contrasena of this RequestIniciarSesion.  # noqa: E501
        :type contrasena: str
        :param correo: The correo of this RequestIniciarSesion.  # noqa: E501
        :type correo: str
        """
        self.swagger_types = {
            'contrasena': str,
            'correo': str
        }

        self.attribute_map = {
            'contrasena': 'contrasena',
            'correo': 'correo'
        }
        self._contrasena = contrasena
        self._correo = correo

    @classmethod
    def from_dict(cls, dikt) -> 'RequestIniciarSesion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request_IniciarSesion of this RequestIniciarSesion.  # noqa: E501
        :rtype: RequestIniciarSesion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def contrasena(self) -> str:
        """Gets the contrasena of this RequestIniciarSesion.


        :return: The contrasena of this RequestIniciarSesion.
        :rtype: str
        """
        return self._contrasena

    @contrasena.setter
    def contrasena(self, contrasena: str):
        """Sets the contrasena of this RequestIniciarSesion.


        :param contrasena: The contrasena of this RequestIniciarSesion.
        :type contrasena: str
        """
        if contrasena is None:
            raise ValueError("Invalid value for `contrasena`, must not be `None`")  # noqa: E501

        self._contrasena = contrasena

    @property
    def correo(self) -> str:
        """Gets the correo of this RequestIniciarSesion.


        :return: The correo of this RequestIniciarSesion.
        :rtype: str
        """
        return self._correo

    @correo.setter
    def correo(self, correo: str):
        """Sets the correo of this RequestIniciarSesion.


        :param correo: The correo of this RequestIniciarSesion.
        :type correo: str
        """
        if correo is None:
            raise ValueError("Invalid value for `correo`, must not be `None`")  # noqa: E501

        self._correo = correo
