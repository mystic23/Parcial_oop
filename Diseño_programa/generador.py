import random
import string
from VALID import ver
import subprocess

class Contraseña:
    def __init__(self, longitud : int,numeros :int, minusculas: str, mayusculas : str) :
        self.longitud = 100
        self.minusculas = " "
        self.mayusculas = " "
        self.numeros = 0
       
    def escoger(self): 
        self.longitud = ver (input("Introduzca la longitud de la contraseña: "))
        self.minusculas =  ver (input("Introduzca el numero minimo de minusculas que quiere en la contraseña: "))
        self.mayusculas =  ver (input("Introduzca el numero minimo de mayusculas que quiere en la contraseña: "))
        self.numeros = ver (input("Introduzca la cantidad de numeros que quiere en la contraseña"))
        caracteres = string.ascii_letters + string.digits

class generarcontraseña(Contraseña):
        def __init__(self, longitud: int, numeros: int, contraseña: str, minusculas: str, mayusculas: str, contraseña : str):
            super().__init__(longitud, numeros, contraseña, minusculas, mayusculas)
            self.contraseña = ""

        def generador(self, esocger):
            longitud = self.longitud
            caracteres = string.ascii_letters + string.digits
            while True:
                contraseña = (" ").join(random.choice(caracteres) for i in range(longitud))
                if(sum(c.islower()for c in contraseña)) >= minusculas
                    and sum (c.isupper() for c in contraseña) >= mayusculas
                    and sum(c.isdigit() for c in contraseña) >= numeros:
                    break

            print('La clave generada de acuerdo a sus indicaciones es ', contraseña)

