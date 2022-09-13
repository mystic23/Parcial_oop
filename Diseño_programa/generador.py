import random
import string

class generadorContraseña:
    def __init__(self, longitud : int, contraseña : str, minusculas: str, mayusculas : str) :
        self.contraseña = " "
        self.longitud = 100
        self.minusculas = " "
        self.mayusculas = " "
       

    def escogerLongitud(self):
        self.longitud = int(input("Introduzca la longitud de la contraseña: "))
        

    def generarcontraseña(self):
        contraseña = " "
        ##declaracion de la contraseña

        for num in range(lMaxima):
          password = password + chr(int(random.randint(32, 126))) 

        print('Clave Generada: ', contraseña)

