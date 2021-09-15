# Importamos la librería datetime de python
from datetime import datetime

# Importamos el módulo que genera la conexión a la base de datos
from conexiones import conectar

# Generamos la conexión y extraemos los datos que nos retorna
conectar = conectar.conexion()
database = conectar[0]
cursor = conectar[1]

# Creación de la clase Usuarios
class Usuarios:
    def __init__(self, id, nombre, apellidos, email, constraseña):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.constraseña = constraseña

    def guardar(self):
        # Tomamos la fecha actual
        now = datetime.now()
        now = now.date()
        sql = "INSERT INTO usuarios VALUES (null, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellidos,
                   self.email, self.constraseña, now)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            print("El usuario ha sido creado correctamente!")
        except:
            print("Error en creación del usuario, verifique sus datos")

    # Método estático para validar el email
    @staticmethod
    def validar(email):
        if "@" in email:
            sql = f"SELECT * FROM usuarios where email = '{email}'"
            cursor.execute(sql)
            resultado = cursor.fetchall()
            if len(resultado) == 0:
                return True
            else:
                print("El correo ingresado ya existe!")
                return False
        else:
            print("Por favor ingrese un email válido")
