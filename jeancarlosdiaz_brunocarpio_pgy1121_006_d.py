# -*- coding: utf-8 -*-
"""JeanCarlosDiaz_BrunoCarpio_PGY1121_006_D.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BBdyFB5KeeyOU8EErnvNMus_OAkAvl9y
"""

print_certificado = ""
agregar_informacion = ""
inf_estado_conyugal = ""
estado_conyugal = ""
fecha_actual = 2023
fecha_de_nacimiento = 0
inf_union_europea = ""
union_europea = ""
bandera = True
edad = 0
nombre = ""
cantidad_nombre = 0
list_inf = {"99999999-RTX": "NIF: "  + "99999999-RTX" + "\n" + "Nombre persona: "+ "Michael Tulio Saldaña" + "\n" + "Estado conyugal: " + " ESTADO CONYUGAL-Soltero/a," + "\n" + "Fecha de nacimiento: " + "2000" + "\n" + "Union europea: " + "NO Pertenece a la Union Europea" + "."}
nif_completo = ""
nif_primera_parte = 0
cantidad_segunda_parte = 0
verificacion_segunda_parte_nif = True
nif_segunda_parte = ""
verificacion_nif = True
opc_menu = 0
print_agregado = ""
menu_principal = f'''
{"-"*40}
{"-NIF-".center(40)}
{"-"*40}

Opcion De Menu:

1) 	Grabar nif
2)	Buscar nif
3)	Imprimir certificado
4)	Salir

{"_"*40}
{"-"*40}
{"-"*40}
{"_"*40}
'''


while bandera:
  def print_menu_principal():
    print(menu_principal)
  print_menu_principal()

  opc_menu = input("Seleccione una opcion del menu: ")
  while opc_menu == "" or not opc_menu.isnumeric():
    opc_menu = input("Seleccione una opcion del menu VALIDA: ")

  if int(opc_menu) == 1:

    nif_primera_parte = input("Ingrese la primera parte del nif antes del (-): ")
    while not nif_primera_parte.isdigit() or int(nif_primera_parte) <= 9999999 or int(nif_primera_parte) > 99999999:
      nif_primera_parte = input("Ingrese NIF valido primera parte del nif ANTES del (-): ")

    nif_segunda_parte = input("Ingrese segunda parte del nif despues del (-): ").upper().strip()
    cantidad_segunda_parte = len(nif_segunda_parte)
    if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
      verificacion_segunda_parte_nif = False
    else:
      verificacion_segunda_parte_nif = True

    while verificacion_segunda_parte_nif == False:
      nif_segunda_parte = input("Ingrese NIF valido segunda parte del nif despues del (-): ").upper().strip()
      cantidad_segunda_parte = len(nif_segunda_parte)

      if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
        verificacion_segunda_parte_nif = False

      else:
        verificacion_segunda_parte_nif = True
    nif_completo = nif_primera_parte + "-" + nif_segunda_parte
    if nif_completo in list_inf:
      agregar_informacion = input("Este nif ya se encuentra en el sistema, desea editarlo (1)si (2)no:")
      while not agregar_informacion == "1" and not agregar_informacion == "2":
        agregar_informacion = input("Este nif ya se encuentra en el sistema, desea editarlo (1)SI o (2)NO: ")

      if int(agregar_informacion) == 1:
        pass

      elif int(agregar_informacion) == 2:
        break

    nombre = input("Ingrese nombre: ").capitalize().strip()
    cantidad_nombre = len(nombre)
    while nombre.isalnum() or nombre == "" or cantidad_nombre < 8:
      nombre = input("Ingrese nombre VALIDO: ").capitalize().strip()
      cantidad_nombre = len(nombre)
    nombre = nombre + ", "
    edad = input("Ingrese edad: ")
    while not edad.isnumeric() or int(edad) < 0:
      edad = input("Ingrese edad VALIDA: ")
    fecha_de_nacimiento = fecha_actual - int(edad)
    if int(edad) >= 16:
      estado_conyugal = input("Ingresar estado conyugal (1)Soltero (2)Casado (3)Divorciado: ")
      while not estado_conyugal == "1" and not estado_conyugal == "2" and not estado_conyugal == "3":
        estado_conyugal = input("Ingresar ESTADO CONYUGAL (1)Soltero (2)Casado (3)Divorciado: ")
      if int(estado_conyugal) == 1:
        inf_estado_conyugal = " ESTADO CONYUGAL-Soltero/a,"
      elif int(estado_conyugal) == 2:
        inf_estado_conyugal = " ESTADO CONYUGAL-Casado/a,"
      elif int(estado_conyugal) == 3:
        inf_estado_conyugal = " ESTADO CONYUGAL-Divorciado/a,"
    else:
      inf_estado_conyugal = " ESTADO CONYUGAL-Soltero/a,"
    union_europea = input("Pertenece a la Union Europea (1)si o (2)no: ")
    while not union_europea == "1" and not union_europea == "2":
      union_europea = input("Pertenece a la Union Europea (1)SI o (2)NO: ")
    if union_europea == "1":
      inf_union_europea = "Pertenece a la Union Europea"
    elif union_europea == "2":
      inf_union_europea = "NO Pertenece a la Union Europea"

    list_inf.update({nif_completo : "NIF: "  + nif_completo + "\n" + "Nombre persona: "+ nombre + "\n" + "Estado conyugal: " + inf_estado_conyugal + "\n" + "Fecha de nacimiento: " + str(fecha_de_nacimiento) + "\n" + "Union europea: " + inf_union_europea + "."})
    print_agregado = ("Se agrego al sistema -  NIF: "  + nif_completo + ", Nombre persona: "+ nombre + "Estado conyugal: " + inf_estado_conyugal + " Fecha de nacimiento: " + str(fecha_de_nacimiento) + ", Union europea: " + inf_union_europea + ".")
    print("\n" + print_agregado)
    input("presione enter para continuar....")

  elif int(opc_menu) == 2:

    nif_primera_parte = input("Ingrese la primera parte del nif antes del (-): ")
    while not nif_primera_parte.isdigit() or int(nif_primera_parte) <= 9999999 or int(nif_primera_parte) > 99999999:
      nif_primera_parte = input("Ingrese NIF valido primera parte del nif ANTES del (-): ")

    nif_segunda_parte = input("Ingrese segunda parte del nif despues del (-): ").upper().strip()
    cantidad_segunda_parte = len(nif_segunda_parte)
    if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
      verificacion_segunda_parte_nif = False
    else:
      verificacion_segunda_parte_nif = True

    while verificacion_segunda_parte_nif == False:
      nif_segunda_parte = input("Ingrese NIF valido segunda parte del nif despues del (-): ").upper().strip()
      cantidad_segunda_parte = len(nif_segunda_parte)

      if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
        verificacion_segunda_parte_nif = False

      else:
        verificacion_segunda_parte_nif = True
    nif_completo = nif_primera_parte + "-" + nif_segunda_parte

    if nif_completo in list_inf:
      print_busqueda = list_inf.get(nif_completo)
      print("Informacion de nif: ".center(40) + "\n"*(2) + print_busqueda)
      input("presiona enter para continuar...")

    if not nif_completo in list_inf :
      print(f"{nif_completo} Este nif no se encuentra en el sistema")
      input("No se pudo encontar el nif verifique que sea correcto e intentelo de nuevo....")

  elif int(opc_menu) == 3:

    nif_primera_parte = input("Ingrese la primera parte del nif antes del (-): ")
    while not nif_primera_parte.isdigit() or int(nif_primera_parte) <= 9999999 or int(nif_primera_parte) > 99999999:
      nif_primera_parte = input("Ingrese NIF valido primera parte del nif ANTES del (-): ")

    nif_segunda_parte = input("Ingrese segunda parte del nif despues del (-): ").upper().strip()
    cantidad_segunda_parte = len(nif_segunda_parte)
    if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
      verificacion_segunda_parte_nif = False
    else:
      verificacion_segunda_parte_nif = True

    while verificacion_segunda_parte_nif == False:
      nif_segunda_parte = input("Ingrese NIF valido segunda parte del nif despues del (-): ").upper().strip()
      cantidad_segunda_parte = len(nif_segunda_parte)

      if not cantidad_segunda_parte == 3 or nif_segunda_parte == "":
        verificacion_segunda_parte_nif = False

      else:
        verificacion_segunda_parte_nif = True
    nif_completo = nif_primera_parte + "-" + nif_segunda_parte

    if nif_completo in list_inf:
      print_certificado = list_inf.get(nif_completo)
      print("_"*40 + "\n" + "-"*40 + "\n" + "-"*40 + "\n" + "_"*40+ "\n" +  "CERTIFICADO DE NACIMIENTO".center(40) + "\n"*(2) + f"Certificado para nif: {nif_completo}".center(5) +"\n" + print_certificado + "\n" +"_"*40 + "\n" + "-"*40 + "\n" + "-"*40 + "\n" + "_"*40+ "\n")
      input("presiona enter para continuar...")

    if not nif_completo in list_inf :
      print(f"{nif_completo} Este nif no se encuentra en el sistema")
      input("No se pudo encontar el nif verifique que sea correcto e intentelo de nuevo....")

  elif int(opc_menu) == 4:
    print("Saliendo del sistema, que tenga un lindo dia \n Product by Jean Carlos Diaz Perez y Bruno Carpio v1.0")
    bandera = False