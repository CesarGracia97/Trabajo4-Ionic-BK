import pandas as pd
from datetime import datetime
import calendar
from swagger_server.utils.resource.mysql_configuration import MySQL_Configuration
from swagger_server.uses_cases.db_queries_methods import DB_Queries_Methods

class DB_Update_Method:

    @staticmethod
    def update_usuario(CONTACTO, NOMBRE, ID):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """ UPDATE USUARIO SET CONTACTO = %s, NOMBRE= %s WHERE ID = %s"""
            params = (CONTACTO, NOMBRE, ID)
            db_config.connect()
            result = db_config.execute_query(query, params)
            db_config.disconnect()
            if result:
                response['message']= 'Actualizacion de Usuario Completada'
                response['status']= 200

            else:
                response['message']= 'Algo ocurrio en la actualizacion'
                response['status']= 400
        except Exception as e:
            message = f"Algo interno fallo: {str(e)}"
            response["message"] = message
            response["status"] = 500
            print(message)
        return response

    @staticmethod
    def update_contact(NOMBRE, CORREO, TELEFONO, ID):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """ UPDATE CONTACTO SET NOMBRE = %s, CORREO = %s, TELEFONO = %s WHERE ID = %s"""
            params = (NOMBRE, CORREO, TELEFONO, ID)
            db_config.connect()
            result = db_config.execute_query(query, params)
            db_config.disconnect()
            if result:
                response['message']= 'Actualizacion de Contacto Completada'
                response['status']= 200
            else:
                response['message']= 'Algo ocurrio en la actualizacion de Contacto'
                response['status']= 404
        except Exception as e:
            message = f"Algo interno fallo: {str(e)}"
            response["message"] = message
            response["status"] = 500
            print(message)
        return response

    @staticmethod
    def bloquear_contact(ID):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """ UPDATE CONTACTO SET ISVALID = 'N' WHERE ID = %s"""
            db_config.connect()
            result = db_config.execute_query(query, (ID,))
            db_config.disconnect()
            if result:
                response['message']= 'SE HA BLOQUEADO SU CUENTA'
                response['status']= 200
            else:
                response['message']= 'ERROR EN BLOQUEO (SUERTUDO)'
                response['status']= 400
        except Exception as e:
            message = f"Algo interno fallo: {str(e)}"
            response["message"] = message
            response["status"] = 500
            print(message)
        return response

    @staticmethod
    def bloquear_usuario(ID):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """ UPDATE USUARIO SET ISVALID = 'N' WHERE ID = %s"""
            db_config.connect()
            result = db_config.execute_query(query, (ID,))
            db_config.disconnect()
            if result:
                response['message']= 'SE HA BLOQUEADO SU CUENTA'
                response['status']= 200
            else:
                response['message']= 'ERROR EN BLOQUEO (SUERTUDO)'
                response['status']= 400
        except Exception as e:
            message = f"Algo interno fallo: {str(e)}"
            response["message"] = message
            response["status"] = 500
            print(message)
        return response