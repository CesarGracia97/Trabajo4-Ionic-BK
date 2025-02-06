# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class RequestBloquearContacto(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: float=None):  # noqa: E501
        """RequestBloquearContacto - a model defined in Swagger

        :param id: The id of this RequestBloquearContacto.  # noqa: E501
        :type id: float
        """
        self.swagger_types = {
            'id': float
        }

        self.attribute_map = {
            'id': 'ID'
        }
        self._id = id

    @classmethod
    def from_dict(cls, dikt) -> 'RequestBloquearContacto':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request_BloquearContacto of this RequestBloquearContacto.  # noqa: E501
        :rtype: RequestBloquearContacto
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> float:
        """Gets the id of this RequestBloquearContacto.


        :return: The id of this RequestBloquearContacto.
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id: float):
        """Sets the id of this RequestBloquearContacto.


        :param id: The id of this RequestBloquearContacto.
        :type id: float
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id
