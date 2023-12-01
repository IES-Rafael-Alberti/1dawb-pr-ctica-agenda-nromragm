"""
27/11/2023

Práctica del examen para realizar en casa
-----------------------------------------

* El programa debe estar correctamente documentado.

* Debes intentar ajustarte lo máximo que puedas a lo que se pide en los comentarios TODO.

* Tienes libertad para desarrollar los métodos o funciones que consideres, pero estás obligado a usar como mínimo todos los que se solicitan en los comentarios TODO.

* Además, tu programa deberá pasar correctamente las pruebas unitarias que se adjuntan en el fichero test_agenda.py, por lo que estás obligado a desarrollar los métodos que se importan y prueban en la misma: pedir_email(), validar_email() y validar_telefono()

"""

import os
import pathlib
from os import path

# Constantes globales
RUTA = pathlib.Path(__file__).parent.absolute() 

NOMBRE_FICHERO = 'contactos.csv'

RUTA_FICHERO = path.join(RUTA, NOMBRE_FICHERO)

#TODO: Crear un conjunto con las posibles opciones del menú de la agenda
OPCIONES_MENU = {1, 2, 3, 4, 5, 6, 7, 8}
#TODO: Utiliza este conjunto en las funciones agenda() y pedir_opcion()

CONTACTOS_PRUEBA = []
def borrar_consola():
    """ Limpia la consola
    """
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")


def cargar_contactos(contactos: list):
    """ Carga los contactos iniciales de la agenda desde un fichero
    Args:
        contactos (list): Lista de contactos.

    Returns:
        contactos (list): Lista de contactos actualizada

    Raises:
        FileNotFoundError: Se produce si el archivo especificado en RUTA_FICHERO no se encuentra.
        Exception: Se produce para otros errores durante la carga de contactos desde el archivo.
    """
    #TODO: Controlar los posibles problemas derivados del uso de ficheros...
    lista_contactos = dict()
    try:
        with open(RUTA_FICHERO, 'r') as fichero:

            for linea in fichero:
                    datos = linea.strip().split(";")
                    nombre = datos[0]
                    apellido = datos[1]
                    email = datos[2]
                    telefonos = datos[3:]

                    lista_contactos = {"nombre": nombre, "apellido": apellido, "email": email, "telefonos": telefonos}
                    if not any(contacto["email"].lower() == email.lower() for contacto in contactos):
                        contactos.append(lista_contactos)
    except FileNotFoundError:
        print("Fichero no encontrado")
    except Exception as e:
        print(f"Error al cargar contactos: {e}")
    
    return contactos


def pedir_nombre():
    """Solicita al usuario que introduzca un nombre.

    Returns:
        str: Nombre introducido por el usuario.

    Raises:
        ValueError: Se produce si el nombre es una cadena vacía.
    """    
    todo_ok = False
    while not todo_ok:
        try:
            nombre = input("Introduce un nombre: ").title()
            if nombre.strip() == "":
                raise ValueError
            else:
                todo_ok = True
        except ValueError:
            print("Error, introduce un nombre")
    return nombre        


def pedir_apellido():
    """Solicita al usuario que introduzca un napellido.

    Returns:
        str: Apellido introducido por el usuario.

    Raises:
        ValueError: Se produce si el apellido es una cadena vacía.
    """ 
    todo_ok = False
    while not todo_ok:
        try:
            apellido = input("Introduce el apellido: ").title()
            if  apellido.strip() == "":
                raise ValueError
            else:
                todo_ok = True
        except ValueError:
            print("Error, introduce un apellido")
    return apellido



def pedir_email(contactos: list):
    """Solicita al usuario que introduzca un email
    y llama a la función validar_email para validarlo.

    Args:
        contactos (list): Lista de contactos actualizada.

    Returns:
        str: Email introducido por el usuario.

    Raises:
        ValueError: Se produce si la función validar_email detecta un problema con el email introducido.
    """
    email = input("Introduce un email: ").strip()
    if validar_email(email, contactos):
        return email


def pedir_email_criterio():
    """Solicita al usuario que introduzca un email sin validar

    Returns:
        str: Email introducido por el usuario
    """
    email = input("Introduce un email: ").strip()
    return email


def validar_email(email: str, contactos: list):
    """La función verifica si el email ya existe en la lista de contactos, si no está vacío y si contiene el carácter "@".

    Args:
        email str: Email a validar.
        contactos list: Lista de contactos actualizada.

    Returns:
        bool: True si el email cumple con los requisitos, False en caso contrario.

    Raises:
        ValueError: Se produce si el email ya existe en la agenda, si es una cadena vacía o si no contiene el carácter "@".
    """

    for contacto in contactos:
        if contacto["email"].lower() == email.lower():
            raise ValueError("el email ya existe en la agenda")
    
    if email.strip() == "":
        raise ValueError("el email no puede ser una cadena vacía")
    
    if "@" not in email:
        raise ValueError("el email no es un correo válido")
    
    return True



def agregar_contacto(contactos: list):
    """Agrega un nuevo contacto a la lista de contactos.

    La función utiliza las funciones pedir_nombre(), pedir_apellido(), pedir_email() y pedir_telefonos() 
    para solicitar al usuario la información para crear un nuevo contacto.

    Args:
        contactos (list): Lista de contactos actualizada.
    """
    try:
        nuevo_contacto = {
            "nombre": pedir_nombre(),
            "apellido": pedir_apellido(),
            "email": pedir_email(contactos),
            "telefonos": pedir_telefonos()
            }
        
        contactos.append(nuevo_contacto)
    except Exception:
        print("ERROR, accion cancelada")

    

def pedir_telefonos_criterio():
    """Solicita al usuario que introduzca un número de teléfono sin validar.

    Returns:
        str: Número de teléfono introducido por el usuario.
    """
    todo_ok = False
    while not todo_ok:
        telefono = input("Introduce telefono del contacto: ")

        if telefono != "":
            todo_ok = True
            return telefono
        

def pedir_telefonos():
    """Solicita al usuario que introduzca números de teléfono.

    y llama a la función validar_telefono para validarlo.

    Returns:
        list: Lista de números de teléfono introducidos por el usuario.
    """
    lista_telefonos = []    
    todo_ok = False
    while not todo_ok:

        telefono = input("Introduce telefonos (enter para terminar): ")

        if telefono == "":
            todo_ok = True
            return lista_telefonos
        
        if validar_telefono(telefono):
            lista_telefonos.append(telefono)



def validar_telefono(telefono):
    """La función verifica si el número de teléfono tiene 9 dígitos y es una cadena numérica, o si tiene 12 caracteres y comienza con "+34".

    Args:
        telefono str: Número de teléfono a validar.

    Returns:
        bool: True si el número de teléfono cumple con los requisitos, False en caso contrario.
    """    
    telefono = telefono.replace(" ", "")
    
    if len(telefono) == 9 and telefono.isdigit():
        return True
    
    elif len(telefono) == 12 and telefono[:3] == "+34" and telefono[3:].isdigit():
        return True
    
    else:
        return False


def buscar_contacto(contactos: list, email):
    """Busca la posición de un contacto en la lista por su dirección de correo electrónico.

    Args:
        contactos (list): Lista de contactos.
        email (str): Dirección de correo electrónico del contacto a buscar.

    Returns:
        int: Posición del contacto en la lista si se encuentra, None si no se encuentra.
    """

    for posicion in range(len(contactos)):
            if contactos[posicion]["email"] == email:
                return posicion
    return None


def eliminar_contacto(contactos: list, email: str):
    """ Elimina un contacto de la agenda
    ...
    """
    borrar_consola()
    if email == None:
        email = input("Introduce el email del contacto a eliminar: ")
    try:
        #TODO: Crear función buscar_contacto para recuperar la posición de un contacto con un email determinado
        pos = buscar_contacto(contactos, email)
        if pos != None:
            del contactos[pos]
            print("Se eliminó 1 contacto")
        else:
            print("No se encontró el contacto para eliminar")
    except Exception as e:
        print(f"**Error** {e}")
        print("No se eliminó ningún contacto")


def mostrar_contactos(contactos):
    """Muestra todos los contactos de la lista

    """
    borrar_consola()
    contactos = sorted(contactos, key=lambda x: x["nombre"])
    print(f"Agenda ({len(contactos)})")
    print("-" * 6)
    for contacto in contactos:
        print(f"Nombre: {contacto["nombre"]} {contacto["apellido"]} ({contacto["email"]})")
        if not contacto["telefonos"]:
            print("Teléfonos: ninguno")
        else:
            print(f"Teléfonos: {" / ".join(contacto["telefonos"])}")
        
        print("." * 6)


def pedir_criterio():
    """Solicita al usuraio el criterio

    Raises:
        ValueError: Se produce si el critrerio introducido no es valido

    Returns:
        criterio (int): criterio introducido por el usuario
    """
    print("Criterios")
    print("-" * 9)
    todo_ok = False
    while not todo_ok:
        print("1. Nombre")
        print("2. Apellido")
        print("3. Email")
        print("4. Telefono")

        try:
            criterio = int(input("Introduzca el criterio (1-4): "))
            if criterio < 0 or criterio > 4:
                raise ValueError
            else:
                todo_ok = True
        except ValueError:
            print("Introduce un criterio valido")

    return criterio
        

def modificar_contacto(contactos:list):
    """Modifica el contacto elegido segun el criterio

    Args:
        contactos (list): lista de contactos actualizada.
    """
    email_modificar = input("Introduce el email del contacto a modificar: ")
    posicion = buscar_contacto(contactos, email_modificar)
    criterio = pedir_criterio()
    
    if criterio == 1:
        nombre = pedir_nombre()
        contactos[posicion]["nombre"] = nombre
    elif criterio == 2:
        apellido = pedir_apellido()
        contactos[posicion]["apellido"] = apellido
    elif criterio == 3:
        email = pedir_email(contactos)
        contactos[posicion]["email"] = email
    elif criterio == 4:
        telefono = pedir_telefonos()
        contactos[posicion["telefonos"]] = telefono 


def mostrar_contactos_criterio(contactos: list):
    """Solicita un criterio y muestra el contacto segun el criterio solicitado
    Args:
        contactos (list): lista de contactos actualizada.
    """
    criterio = pedir_criterio()

    if criterio == 1:
        nombre = pedir_nombre()
        for contacto in contactos:
            if contacto["nombre"] == nombre:
                print_contacto(contacto)

    elif criterio == 2:
        apellido = pedir_apellido()
        for contacto in contactos:
            if contacto["apellido"] == apellido:
                print_contacto(contacto)

    elif criterio == 3:
        email = pedir_email_criterio(contactos)
        for contacto in contactos:
            if contacto["email"] == email:
                print_contacto(contacto)

    elif criterio == 4:
        telefono = pedir_telefonos_criterio()
        for contacto in contactos:
            if telefono in contacto["telefonos"]:
                print_contacto(contacto)


def print_contacto(contacto):
    """Print del contacto 

    Args:
        
    """
    print(f"Nombre: {contacto["nombre"]} {contacto["apellido"]} ({contacto["email"]})")
    if not contacto["telefonos"]:
        print("Teléfonos: ninguno")
    else:
        print(f"Teléfonos: {" / ".join(contacto["telefonos"])}")
    print("." * 6)


def agenda(contactos: list):
    """ Ejecuta el menú de la agenda con varias opciones
    ...
    """
    #TODO: Crear un bucle para mostrar el menú y ejecutar las funciones necesarias según la opción seleccionada...
    opcion = -1
    while opcion != 8:
        mostrar_menu()
        opcion = pedir_opcion()

        #TODO: Se valorará que utilices la diferencia simétrica de conjuntos para comprobar que la opción es un número entero del 1 al 7
        if opcion in OPCIONES_MENU - {8}:
        
            if opcion == 1:
                agregar_contacto(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 2:
                modificar_contacto(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 3:
                eliminar_contacto(contactos, None)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 4:
                vaciar_agenda(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 5:
                cargar_contactos(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 6:    
                mostrar_contactos_criterio(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()
            elif opcion == 7:          
                mostrar_contactos(contactos)
                pulse_tecla_para_continuar()
                borrar_consola()

def vaciar_agenda(contactos: list):
    """Borra la lista de contactos
    Args:
        contactos (list): lista de contactos actualizada

    Returns:
        contactos (list): lista de cobntactos vacia
    """
    contactos = contactos.clear()
    return contactos


def pulse_tecla_para_continuar():
    """ Muestra un mensaje y realiza una pausa hasta que se pulse una tecla
    """
    print("\n")

    os.system("pause")


def mostrar_menu():
    """Muestra el menu
    """
    print("AGENDA")
    print("-" * 5)
    print("1. Nuevo contacto")
    print("2. Modificar contacto")
    print("3. Eliminar contacto")
    print("4. Vaciar agenda")
    print("5. Cargar agenda inicial")
    print("6. Mostrar contactos por criterio")
    print("7. Mostrar la agenda completa")
    print("8. Salir")


def pedir_opcion():
    """Solicita al usuario una opcion

    Returns:
        opcion (int): opcion introducida por el usuario
    """

    try:
        opcion = int(input(">> Seleccione una opción: "))
        if opcion in OPCIONES_MENU:
            return opcion 
        else:
            raise ValueError
            
    except ValueError:
        print("Error introduce una opcion valida")
        return -1

def main():
    """ Función principal del programa
    """
    borrar_consola()

    #TODO: Asignar una estructura de datos vacía para trabajar con la agenda
    contactos = []

    #TODO: Modificar la función cargar_contactos para que almacene todos los contactos del fichero en una lista con un diccionario por contacto (claves: nombre, apellido, email y telefonos)
    #TODO: Realizar una llamada a la función cargar_contacto con todo lo necesario para que funcione correctamente.
    cargar_contactos(contactos)

    #TODO: Crear función para agregar un contacto. Debes tener en cuenta lo siguiente:
    # - El nombre y apellido no pueden ser una cadena vacía o solo espacios y se guardarán con la primera letra mayúscula y el resto minúsculas (ojo a los nombre compuestos)
    # - El email debe ser único en la lista de contactos, no puede ser una cadena vacía y debe contener el carácter @.
    # - El email se guardará tal cuál el usuario lo introduzca, con las mayúsculas y minúsculas que escriba. 
    #  (CORREO@gmail.com se considera el mismo email que correo@gmail.com)
    # - Pedir teléfonos hasta que el usuario introduzca una cadena vacía, es decir, que pulse la tecla <ENTER> sin introducir nada.
    # - Un teléfono debe estar compuesto solo por 9 números, aunque debe permitirse que se introduzcan espacios entre los números.
    # - Además, un número de teléfono puede incluir de manera opcional un prefijo +34.
    # - De igual manera, aunque existan espacios entre el prefijo y los 9 números al introducirlo, debe almacenarse sin espacios.
    # - Por ejemplo, será posible introducir el número +34 600 100 100, pero guardará +34600100100 y cuando se muestren los contactófono se mostrará como +34-600100100. 
    #TODO: Realizar una llamada a la función agregar_contacto con todo lo necesario para que funcione correctamente.os, el tel
    agregar_contacto(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Realizar una llamada a la función eliminar_contacto con todo lo necesario para que funcione correctamente, eliminando el contacto con el email rciruelo@gmail.com
    eliminar_contacto(contactos, "rciruelo@gmail.com")

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear función mostrar_contactos para que muestre todos los contactos de la agenda con el siguiente formato:
    # ** IMPORTANTE: debe mostrarlos ordenados según el nombre, pero no modificar la lista de contactos de la agenda original **
    #
    # AGENDA (6)
    # ------
    # Nombre: Antonio Amargo (aamargo@gmail.com)
    # Teléfonos: niguno
    # ......
    # Nombre: Daniela Alba (danalba@gmail.com)
    # Teléfonos: +34-600606060 / +34-670898934
    # ......
    # Nombre: Laura Iglesias (liglesias@gmail.com)
    # Teléfonos: 666777333 / 666888555 / 607889988
    # ......
    # ** resto de contactos **
    #
    #TODO: Realizar una llamada a la función mostrar_contactos con todo lo necesario para que funcione correctamente.
    mostrar_contactos(contactos)

    pulse_tecla_para_continuar()
    borrar_consola()

    #TODO: Crear un menú para gestionar la agenda con las funciones previamente desarrolladas y las nuevas que necesitéis:
    # AGENDA
    # ------
    # 1. Nuevo contacto
    # 2. Modificar contacto
    # 3. Eliminar contacto
    # 4. Vaciar agenda
    # 5. Cargar agenda inicial
    # 6. Mostrar contactos por criterio
    # 7. Mostrar la agenda completa
    # 8. Salir
    #
    # >> Seleccione una opción: 
    #
    #TODO: Para la opción 3, modificar un contacto, deberás desarrollar las funciones necesarias para actualizar la información de un contacto.
    #TODO: También deberás desarrollar la opción 6 que deberá preguntar por el criterio de búsqueda (nombre, apellido, email o telefono) y el valor a buscar para mostrar los contactos que encuentre en la agenda.
    agenda(contactos)


if __name__ == "__main__":
    main()