# -*- coding: utf-8 -*-
"""Te damos la bienvenida a Colaboratory

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/intro.ipynb
"""

#registro de usuario Yeison
n=str(input("Escribe tu Nombre: "))
cu=int(input("cuantos años tienes: "))
g=int(input("Que sexo eres: 1)Masculino 2)Femenino: "))
c=str(input("Escriba su direccion de correo electronico: "))
co=int(input("digite una cotraseña (SOLO NUMEROS): "))
te=int(input("Aceptas terminos y condiciones: 1)SI 2)NO: "))


if cu>=18:
  if te==1:
    if g==1:
      print("Bienvenido, ",n,"Espero que disfrutes de los productos que vendemos.")
elif cu<18 and cu>0:
  print("!ERROR¡ TIENES QUE SER MAYOR DE EDAD PARA REGISTRARSE.")

if g==2:
  print("Bienvenida, ",n,"Espero que disfrutes de los productos que vendemos.")

if te==2:
    print("!ERROR¡ NO ACPTASTE LOS TERMINOS Y CONDICIONES.")