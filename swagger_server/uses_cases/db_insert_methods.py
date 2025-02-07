from swagger_server.utils.resource.mysql_configuration import MySQL_Configuration


class DB_Insert_Methods:
    @staticmethod
    def create_usuario(CORREO, CONTRASENA, NOMBRE, CEDULA, CONTACTO):
        """"""
        response = {}
        message = ''
        try:
            db_config = MySQL_Configuration()
            values = (CORREO, CONTRASENA, NOMBRE, CEDULA, CONTACTO, 'Y')
            query = """INSERT INTO USUARIO (CORREO, CONTRASENA, NOMBRE, CEDULA, CONTACTO, ISVALID)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            db_config.connect()
            result = db_config.execute_query(query, values)
            db_config.disconnect()
            if result:
                message = f"USUARIO: {NOMBRE} CREADO"
                response["message"] = message
                response["status"] = 200
                print(message)
            else:
                message = f"Cedula o Correo ya existentes"
                response["message"] = message
                print(message)
                response["status"] = 400
        except Exception as e:
            message = f"Algo interno fallo: {e}"
            response["message"] = message
            response["status"] = 400
        finally:
            return response


    @staticmethod
    def create_contacto(USUARIO_ID, NOMBRE, TELEFONO, CORREO, CEDULA):
        """"""
        response = {}
        message = ''
        try:
            db_config = MySQL_Configuration()
            values = (USUARIO_ID, NOMBRE, TELEFONO, CORREO, CEDULA, 'Y')
            query = """INSERT INTO CONTACTO (USUARIO_ID, NOMBRE, TELEFONO, CORREO, CEDULA, ISVALID)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            db_config.connect()
            result = db_config.execute_query(query, values)
            db_config.disconnect()
            if result:
                message = f"CONTACTO: {NOMBRE} CREADO"
                response["message"] = message
                response["status"] = 200
                print(message)
            else:
                message = f"Algo fallo en crear el contacto"
                response["message"] = message
                print(message)
                response["status"] = 400
        except Exception as e:
            message = f"Algo interno fallo: {e}"
            response["message"] = message
            response["status"] = 400
            print(message)
        finally:
            return response
