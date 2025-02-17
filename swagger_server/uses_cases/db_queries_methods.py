import smtplib
from datetime import datetime, timedelta
import calendar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from swagger_server.utils.resource.mysql_configuration import MySQL_Configuration

class DB_Queries_Methods:

    @staticmethod
    def query_usuarios(idUsuario):
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT ID, CORREO, NOMBRE, CEDULA, CONTACTO FROM USUARIO WHERE ID = %s"""
            db_config.connect()
            result = db_config.fetch_results(query, (idUsuario,))
            db_config.disconnect()

            if result:
                fila = result[0]  # Extraer la primera fila (tupla)
                response['ID'] = fila[0]
                response['CORREO'] = fila[1]
                response['NOMBRE'] = fila[2]
                response['CEDULA'] = fila[3]
                response['CONTACTO'] = fila[4]
                response['status'] = 200
            else:
                response['status'] = 400
                response['message'] = "error en la consulta"
        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error desde el servidor: {str(e)}"
        return response

    @staticmethod
    def query_iniciar_sesion(correo, contrasena):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT CORREO, CONTRASENA, ID FROM USUARIO WHERE CORREO = %s"""
            db_config.connect()
            result = db_config.fetch_results(query, (correo,))
            db_config.disconnect()

            if result:
                user_data = result[0]  # Extraemos la primera fila devuelta por la consulta
                db_password = user_data[1]  # Contraseña almacenada en la BD
                if db_password == contrasena:
                    response['status'] = 200
                    response['message'] = "Inicio de sesión exitoso"
                    response['ID'] = user_data[2]
                else:
                    response['status'] = 400
                    response['message'] = "Credenciales incorrectas"
            else:
                response['status'] = 400
                response['message'] = "Usuario no encontrado"

        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error desde el servidor: {str(e)}"
        return response

    @staticmethod
    def query_recuperar_cuenta(correo):
        """Método para recuperar la contraseña de un usuario mediante un correo de recuperación."""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = "SELECT CONTRASENA FROM USUARIO WHERE CORREO = %s"
            db_config.connect()
            result = db_config.fetch_results(query, (correo,))
            db_config.disconnect()

            if result:
                password = result[0][0]  # Obtener la contraseña

                sender_email = "axl.lejo@gmail.com"
                sender_password = "jxqknxihcvlrrwkb"
                subject = "Recuperación de Cuenta"
                body = f"Su contraseña es: {password}"

                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = correo
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, correo, msg.as_string())
                server.quit()

                response['status'] = 200
                response['message'] = "Correo de recuperación enviado exitosamente"
            else:
                response['status'] = 400
                response['message'] = "Usuario no encontrado"

        except Exception as e:
            response['status'] = 400
            response['message'] = f"Error desde el servidor: {str(e)}"

        return response

    @staticmethod
    def query_lista_contactos(usuario_id):
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT NOMBRE, TELEFONO, CORREO, CEDULA, ISVALID, ID FROM CONTACTO WHERE USUARIO_ID = %s"""
            db_config.connect()
            result = db_config.fetch_results(query, (usuario_id,))
            db_config.disconnect()

            if result is None:  # Si la consulta falla o hay un problema con la base de datos
                response['status'] = 400
                response['message'] = "Error en la consulta o parámetros incorrectos"

            elif isinstance(result, list) and len(result) > 0:  # Si hay datos en la consulta
                response['contactos'] = []
                for row in result:
                    if len(row) >= 5:  # Asegurar que tenga las 5 columnas esperadas
                        response['contactos'].append({
                            'NOMBRE': row[0],
                            'TELEFONO': row[1],
                            'CORREO': row[2],
                            'CEDULA': row[3],
                            'ISVALID': row[4],
                            'ID': row[5]
                        })
                    else:
                        print(f"Advertencia: Fila incompleta encontrada -> {row}")

                response['status'] = 200
                response['message'] = "Lista de contactos obtenida exitosamente"

            else:  # Si la consulta se ejecutó correctamente pero no hay datos
                response['status'] = 200
                response['message'] = "No hay contactos disponibles para este usuario"
                response['contactos'] = []

        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error en el servidor: {str(e)}"

        return response

    @staticmethod
    def query_Lista_usuario():
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT  ID, NOMBRE FROM USUARIO"""
            db_config.connect()
            result = db_config.fetch_results(query)
            db_config.disconnect()
            if result is None: # Si la consulta falla o hay un problema con la base de datos
                response['status'] = 400
                response['message'] = "Error en la consulta o parámetros incorrectos"
            elif isinstance(result, list) and len(result) > 0:
                response['usuarios'] = []
                for row in result:
                    if len(row) >= 2: response['usuarios'].append({
                        'ID': row[0], 'NOMBRE': row[1]
                    })

                response['status'] = 200
                response['message'] = "Lista de contactos obtenida exitosamente"
            else:  # Si la consulta se ejecutó correctamente pero no hay datos
                response['status'] = 200
                response['message'] = "No hay Usuarios en Lista"
                response['usuarios'] = []
        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error desde el servidor: {str(e)}"
        return response
