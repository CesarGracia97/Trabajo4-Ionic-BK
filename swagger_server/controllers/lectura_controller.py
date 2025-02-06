import connexion
import six

from swagger_server.models.request_lista_contactos import RequestListaContactos  # noqa: E501
from swagger_server.models.request_lista_usuarios import RequestListaUsuarios  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util


def get_read_contactos(body=None):  # noqa: E501
    """get_read_contactos

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestListaContactos.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_read_usuarios(body=None):  # noqa: E501
    """get_read_usuarios

    Endpoint de Lectura de Datos # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestListaUsuarios.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
