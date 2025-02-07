import smtplib
from datetime import datetime, timedelta
import calendar
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from swagger_server.utils.resource.mysql_configuration import MySQL_Configuration

class DB_Queries_Methods:
    @staticmethod
    def query_iniciar_sesion(correo, contrasena):
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT CORREO, CONTRASENA, NOMBRE, CEDULA, CONTACTO, ID FROM USUARIO WHERE CORREO = %s"""
            db_config.connect()
            result = db_config.fetch_results(query, (correo,))
            db_config.disconnect()

            if result:
                user_data = result[0]  # Extraemos la primera fila devuelta por la consulta
                db_password = user_data[1]  # Contraseña almacenada en la BD
                if db_password == contrasena:
                    response['status'] = 200
                    response['message'] = "Inicio de sesión exitoso"
                    response['usuario'] = {
                        "id": user_data[5],
                        "correo": user_data[0],
                        "nombre": user_data[2],
                        "cedula": user_data[3],
                        "contacto": user_data[4]
                    }
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
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT  NOMBRE, TELEFONO, CORREO, CEDULA, ISVALID FROM CONTACTO WHERE USUARIO_ID = %s"""
            db_config.connect()
            result = db_config.fetch_results(query, (usuario_id,))
            db_config.disconnect()
            if result:
                response['contactos'] = [{'NOMBRE': row[0], 'TELEFONO': row[1], 'CORREO': row[2], 'CEDULA': row[3], 'ISVALID': row[4]}
                                         for row in result]
                response['status'] = 200
                response['message'] = "Lista de contactos exitoso"
            else:
                response['status'] = 400
                response['message'] = "Lista de contactos no encontrado"
        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error desde el servidor: {str(e)}"
        return response

    @staticmethod
    def query_Lista_usuario():
        """"""
        response = {}
        try:
            db_config = MySQL_Configuration()
            query = """SELECT  ID, NOMBRE, TELEFONO, CORREO, CEDULA, ISVALID FROM USUARIO"""
            db_config.connect()
            result = db_config.fetch_results(query)
            db_config.disconnect()
            if result:
                response['message'] = "Exitoso"
                response['usuario'] = [{'ID': row[0], 'NOMBRE': row[1], 'TELEFONO': row[2], 'CORREO': row[3], 'CEDULA': row[4],
                                        'ISVALID': row[4]}for row in result]
            else:
                response['status'] = 400
                response['message'] = "Algo ocurrio"
        except Exception as e:
            response['status'] = 500
            response['message'] = f"Error desde el servidor: {str(e)}"
        return response
