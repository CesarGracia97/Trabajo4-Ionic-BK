import connexion
import six

from swagger_server.models.request_iniciar_sesion import RequestIniciarSesion  # noqa: E501
from swagger_server.models.request_recuperar_clave import RequestRecuperarClave  # noqa: E501
from swagger_server.models.response import Response  # noqa: E501
from swagger_server import util


def iniciar_sesion(body=None):  # noqa: E501
    """iniciar_sesion

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestIniciarSesion.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def recuperar_contrasena(body=None):  # noqa: E501
    """recuperar_contrasena

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        body = RequestRecuperarClave.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
