# Importamos el modelo de usuarios
from usuarios import usuariosModel
from notas import notasModel

# Librería para ocultar la contraseña en consola
import getpass
# Encriptar la contraseña
import hashlib
# Importamos el módulo que genera la conexión a la base de datos
from conexiones import conectar
conectar = conectar.conexion()
cursor = conectar[1]

# Función para registrar usuarios
def registro():
    nombre = input("Ingrese su nombre: ")
    apellidos = input("Ingrese sus apellidos: ")
    email = input("Ingrese su email: ")
    verificarEmail = usuariosModel.Usuarios.validar(email)
    if verificarEmail:
      contrasena = getpass.getpass("Ingrese su contraseña: ")
      contrasenaCifrado = hashlib.sha256()
      contrasenaCifrado.update(contrasena.encode("utf8"))
      usuario = usuariosModel.Usuarios(
          None, nombre, apellidos, email, contrasenaCifrado.hexdigest())
      usuario.guardar()
      

# Función para loguearse en el sistema
def login():
    email = input("Ingrese su correo electrónico: ")
    contrasena = getpass.getpass("Ingrese su correo contraseña: ")
    contrasenaCifrado = hashlib.sha256()
    contrasenaCifrado.update(contrasena.encode("utf8"))
    usuarioLogin = (email, contrasenaCifrado.hexdigest())
    sql = 'SELECT * FROM usuarios WHERE email = %s AND password = %s'
    try:
        cursor.execute(sql, usuarioLogin)
        respuesta = cursor.fetchone()
        print("Usuario Logueado correctamente!")
        usuario = usuariosModel.Usuarios(
          respuesta[0], respuesta[1], respuesta[2], respuesta[3], respuesta[4])
        return usuario
    except:
        print("el correo y/o contraseña son incorrectos")
        return False
# Función para crear nota
def crearNota(usuario):
    bandera = True
    while bandera:
        titulo = input('Titulo: ')
        validacion = notasModel.Notas.validar(usuario.id, titulo) 
        if validacion :
            bandera = False
        else:
            print('este titutlo ya fue usado eliga otro')
    descripcion = input('Descripcion: ')
    nota = notasModel.Notas(titulo, usuario.id, descripcion)
    print(usuario.id)
    nota.guardar()

# Función para listar notas
def listarNotas(usuario):
    notas = notasModel.Notas.listar(usuario.id)
    for item in notas:
        print(f"\n{item[2]}:")
        print(f" {item[3]}")
        print("")
# Función para eliminar notas    
def eliminarNota(usuario):
    titulo = input('titulo: ')
    eliminado = notasModel.Notas.eliminar(usuario.id, titulo)
    if eliminado[0] == 0:
        print("no se en encontro ninguna Nota con ese titulo")
    else:
        print("su nota ha sido eliminada con exito")


