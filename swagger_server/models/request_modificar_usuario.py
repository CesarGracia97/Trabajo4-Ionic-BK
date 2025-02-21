# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestModificarUsuario(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: float=None, nombre: str=None, contacto: str=None):  # noqa: E501
        """RequestModificarUsuario - a model defined in Swagger

        :param id: The id of this RequestModificarUsuario.  # noqa: E501
        :type id: float
        :param nombre: The nombre of this RequestModificarUsuario.  # noqa: E501
        :type nombre: str
        :param contacto: The contacto of this RequestModificarUsuario.  # noqa: E501
        :type contacto: str
        """
        self.swagger_types = {
            'id': float,
            'nombre': str,
            'contacto': str
        }

        self.attribute_map = {
            'id': 'id',
            'nombre': 'nombre',
            'contacto': 'contacto'
        }
        self._id = id
        self._nombre = nombre
        self._contacto = contacto

    @classmethod
    def from_dict(cls, dikt) -> 'RequestModificarUsuario':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request_ModificarUsuario of this RequestModificarUsuario.  # noqa: E501
        :rtype: RequestModificarUsuario
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> float:
        """Gets the id of this RequestModificarUsuario.


        :return: The id of this RequestModificarUsuario.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id: float):
        """Sets the id of this RequestModificarUsuario.


        :param id: The id of this RequestModificarUsuario.
        :type id: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def nombre(self) -> str:
        """Gets the nombre of this RequestModificarUsuario.


        :return: The nombre of this RequestModificarUsuario.
        :rtype: str
        """
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """Sets the nombre of this RequestModificarUsuario.


        :param nombre: The nombre of this RequestModificarUsuario.
        :type nombre: str
        """
        if nombre is None:
            raise ValueError("Invalid value for `nombre`, must not be `None`")  # noqa: E501

        self._nombre = nombre

    @property
    def contacto(self) -> str:
        """Gets the contacto of this RequestModificarUsuario.


        :return: The contacto of this RequestModificarUsuario.
        :rtype: str
        """
        return self._contacto

    @contacto.setter
    def contacto(self, contacto: str):
        """Sets the contacto of this RequestModificarUsuario.


        :param contacto: The contacto of this RequestModificarUsuario.
        :type contacto: str
        """
        if contacto is None:
            raise ValueError("Invalid value for `contacto`, must not be `None`")  # noqa: E501

        self._contacto = contacto
