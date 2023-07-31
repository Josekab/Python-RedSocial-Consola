#librerias
import os
import sys
import time
import random

#variables
comentariosG = []#lista de comentarios globales

#clase Usurio
class Usuario:
    def __init__(self, nombre, apellido, edad, correo, estadoCivil,  ciudad ): #constructor
        self.nombre = nombre #atributos
        self.apellido = apellido #atributos
        self.edad = edad #atributos
        self.correo = correo #atributos
        self.estadoCivil = estadoCivil #atributos
        self.ciudad = ciudad #atributos
        self.amigos = [] #lista de amigos
        self.comentarios = [] #lista de comentarios
    
    #metodo de mostrar datos
    def mostrarInfo(self): 
        print("Nombre: ", self.nombre)
        print("Apellido: ", self.apellido)
        print("Edad: ", self.edad)
        print("Correo: ", self.correo)
        print("Estado civil: ", self.estadoCivil)
        print("Ciudad o direccion: ", self.ciudad)

    #metodo de agregar amigos
    def agregarAmigo(self, amigo): #recibe un objeto de tipo Usuario y lo agregamos a la lista de amigos
        self.amigos.append(amigo)  #agregamos el amigo a la lista de amigos
        amigo.amigos.append(self)  #agregamos a nosotros a la lista de amigos del amigo

    #agregar comentario al propio perfil
    def agregarComentario(self, comentario):
        global comentariosG #variable global
        self.comentarios.append(comentario) #agregamos el comentario a la lista de comentarios del usuario
        comentariosG = [f"{self.nombre} - {comentario}"] + comentariosG #agregamos el comentario a la lista de comentarios globales
    
    #mostrar Comentarios Globales incluyendo los mios
    def mostrarComentariosGlobales(self):
        for comentario in comentariosG: #recorremos la lista de comentarios globales
            print(comentario)   
    
    #mostrar comentarios de mis amigos
    def mostrarComentariosAmigos(self):
        for amigo in self.amigos: #recorremos la lista de amigos
            for comentario in amigo.comentarios[::-1]: #recorremos la lista de comentarios de los amigos en orden inverso
                print(amigo.nombre + " " + comentario) #mostramos el nombre del amigo y el comentario

    #mostrar los comentarios del propio perfil
    def mostrarComentarios(self):
        for comentario in self.comentarios[::-1]: #recorremos la lista de comentarios del usuario en orden inverso
            print(self.nombre + " " + comentario) #mostramos el comentario

    #metodo de mostrar amigos agregados
    def mostrarAmigos(self): 
        for amigo in self.amigos: #recorremos la lista de amigos
            print(amigo.nombre) #mostramos el nombre del amigo
    
    #Sugerencias de todos los amigos
    def mostrarSugerenciasTotales(self): 
        for amigo in self.amigos: #recorremos la lista de amigos
            for amigoAmigo in amigo.amigos: #recorremos la lista de amigos de los amigos
                if amigoAmigo not in self.amigos and amigoAmigo != self: #si el amigo no esta en la lista de amigos y no es el mismo
                    print(amigoAmigo.nombre) #mostramos el nombre del amigo del amigo

    #Sugerencias de amigos en comun de un solo amigo
    def mostrarSugerenciasAmigosComunes(self, amigo): #recibe un objeto de tipo Usuario
        for a in amigo.amigos: #recorremos la lista de amigos del amigo
            if a not in self.amigos and a != self: #si el amigo no esta en la lista de amigos y no es el mismo
                print(a.nombre) #mostramos el nombre del amigo
    #Sugerencias de amigos en comun de un solo amigo


#clase Red Social
class RedSocial:
    def __init__(self): #constructor
        self.usuarios = [] #lista de usuarios
    
    def crearUsuario(self): #crear usuario 
        nombre = input("Ingrese su nombre: ") 
        apellido = input("Ingrese su apellido: ")
        edad = input("Ingrese su edad: ")
        correo = input("Ingrese su correo: ")
        estadoCivil = input("Ingrese su estadoCivil: ")
        ciudad = input("Ingrese su ciudad o direccion: ")
        usuario = Usuario(nombre, apellido, edad, correo, estadoCivil,  ciudad ) #creamos un objeto de tipo Usuario
        self.usuarios.append(usuario) #agregamos el usuario a la lista de usuarios
    
    def ingresarUsuario(self): #ingresar usuario
        correo = input("Ingrese su correo: ") #ingresamos el correo del usuario
        for usuario in self.usuarios: #recorremos la lista de usuarios
            if usuario.correo == correo: #si el correo del usuario es igual al correo del usuario
                return usuario #retornamos el usuario
        return None #si no retornamos nada
    
    def buscarUsuario(self): #buscar usuario
        nombre = input("Ingrese el nombre del usuario: ") #ingresamos el nombre del usuario
        for usuario1 in self.usuarios: #recorremos la lista de usuarios
            if usuario1.nombre == nombre: #si el nombre del usuario es igual al nombre del usuario
                return usuario1 #retornamos el usuario
        return None #retornamos None

    def buscarAmigo(self): #buscar amigo
        nombre = input("Ingrese el nombre del Amigo: ") #ingresamos el nombre del amigo
        for usuario in self.usuarios: #recorremos la lista de usuarios
            if usuario.nombre == nombre: #si el nombre del usuario es igual al nombre del amigo
                return usuario #retornamos el usuario
        return None #si no lo encontramos retornamos None
    
    def mostrarMenu(self): #menu principal
        print("  ╔═══════════════════╗")
        print("  ║1. Crear usuario   ║")
        print("  ║2. Ingresar usuario║")
        print("  ║3. Buscar usuario  ║")
        print("  ║4. Salir           ║")
        print("  ╚═══════════════════╝") 
        try:
            opcion = int(input("Ingrese una opcion: "))
            return opcion
        except:
            return 0

redSocial = RedSocial() #creamos un objeto de tipo RedSocial
while True:
    os.system("cls")
    opcion = redSocial.mostrarMenu() #mostramos el menu principal
    if opcion == 1: #crear usuario
        redSocial.crearUsuario()
    
    elif opcion == 2: #ingresar usuario y al menu de usuario
        usuario = redSocial.ingresarUsuario()
        if usuario != None:
            while True:
                os.system("cls")
                print("  ╔═════════════════════════════════════════════════════════╗")
                print("                   USUARIO:  " +usuario.nombre,"           ")
                print("  ║ 1. Datos personales                                     ║")
                print("  ║ 2. Agregar amigo                                        ║")
                print("  ║ 3. Mostrar sugerencias                                  ║")
                print("  ║ 4. Buscar amigos                                        ║")
                print("  ║ 5. Mostrar amigos                                       ║")
                print("  ║ 6. Agregar comentario a mi perfil                       ║")
                print("  ║ 7. Mostrar comentarios de mi perfil                     ║")
                print("  ║ 8. Mostrar comentarios de mis amigos                    ║")
                print("  ║ 9. Mostrar comentarios globales                         ║")
                print("  ║ 10. Salir                                               ║")
                print("                                                             ")
                print("  ╚═════════════════════════════════════════════════════════╝")
                try:
                    opcion = int(input("Ingrese una opcion: "))
                except:
                    continue
                if opcion == 1: #mostrar datos personales
                    usuario.mostrarInfo()
                    input("Presione una tecla para continuar...")
                elif opcion == 2: #agregar amigo
                    amigo = redSocial.buscarUsuario()
                    if amigo != None:
                        usuario.agregarAmigo(amigo)
                elif opcion == 3: #mostrar sugerencias
                    usuario.mostrarSugerenciasTotales()
                    input("Presione una tecla para continuar...")
                elif opcion == 4: #menu de busqueda de amigos
                    usuario1 = redSocial.buscarAmigo()
                    if usuario1 != None:
                        while True:
                            os.system("cls")
                            print("╔═════════════════════════════════════════════════════════╗")
                            print("                   Amigo:  " +usuario1.nombre,"            ")
                            print("║  1-Ver datos de este amigo                              ║")
                            print("║  2-Ver sugerencias de este amigo                        ║")
                            print("║  3-Ver comentarios de este amigo                        ║")
                            print("║  4-Salir                                                ║")
                            print("                                                           ")
                            print("╚═════════════════════════════════════════════════════════╝")
                            try:
                                opcion = int(input("Ingrese una opcion: "))
                            except:
                                continue
                            if opcion == 1: #mostrar datos de este amigo
                                usuario1.mostrarInfo()
                                input("Presione una tecla para continuar...")
                            elif opcion == 2: #mostrar sugerencias de este amigo
                                usuario.mostrarSugerenciasAmigosComunes(usuario1)
                                input("Presione una tecla para continuar...")
                            elif opcion == 3: #mostrar comentarios de este amigo
                                usuario1.mostrarComentarios()
                                input("Presione una tecla para continuar...")
                            elif opcion == 4: #salir
                                break
                elif opcion == 5: #mostrar amigos
                    usuario.mostrarAmigos()
                    input("Presione una tecla para continuar...")
                elif opcion == 6: #agregar comentario a mi perfil
                    comentario = input("Ingrese un comentario: ")
                    usuario.agregarComentario(comentario)
                elif opcion == 7: #mostrar comentarios de mi perfil
                    usuario.mostrarComentarios()
                    input("Presione una tecla para continuar...")
                elif opcion == 8: #mostrar comentarios de mis amigos
                    usuario.mostrarComentariosAmigos()
                    input("Presione una tecla para continuar...")
                elif opcion == 9: #mostrar comentarios globales
                    usuario.mostrarComentariosGlobales()
                    input("Presione una tecla para continuar...")
                elif opcion == 10: #salir
                    break
                else:
                    print("Opcion incorrecta")
                    input("Pulse enter para continuar...")
    elif opcion == 3: #buscar usuario
        usuario = redSocial.buscarUsuario()
        if usuario != None:
            print("Nombre: " + usuario.nombre)
            print("Apellido: " + usuario.apellido)
            print("Edad: " + usuario.edad)
            print("Correo: " + usuario.correo)
            print("estadoCivil: " + usuario.estadoCivil)
            print("Ciudad o Direccion: " + usuario.ciudad)
            input("Presione una tecla para continuar...")
    elif opcion == 4: #salir
        break
    else:
        print("Opcion incorrecta")
    input("Pulse enter para continuar...")


