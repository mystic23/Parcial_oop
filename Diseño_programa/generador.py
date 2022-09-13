
import random
import string
from VALID import ver


class Contraseña:
    def __init__(self, longitud : int,numeros :int, minusculas: int, mayusculas : int) :
        self.longitud = longitud
        self.minusculas =  minusculas
        self.mayusculas =  mayusculas
        self.numeros = numeros
       
    # def escoger(self): 
    #     self.longitud = ver (input("Introduzca la longitud de la contraseña: "))
    #     self.minusculas =  ver (input("Introduzca el numero minimo de minusculas que quiere en la contraseña: "))
    #     self.mayusculas =  ver (input("Introduzca el numero minimo de mayusculas que quiere en la contraseña: "))
    #     self.numeros = ver (input("Introduzca la cantidad de numeros que quiere en la contraseña"))
        

class generarcontraseña(Contraseña):
        def __init__(self, longitud: int, numeros: int,  minusculas: int, mayusculas: int):
            super().__init__(longitud, numeros, minusculas, mayusculas)
            

        def generador(self):
            longitud = self.longitud
            caracteres = string.ascii_letters + string.digits
            while True:
                contraseña = (" ").join(random.choice(caracteres) for i in range(longitud))
                if(sum(c.islower() for c in contraseña)) >= self.minusculas and sum (c.isupper() for c in contraseña) >= self.mayusculas and sum(c.isdigit() for c in contraseña) >= self.numeros:
                    break

            print('La clave generada de acuerdo a sus indicaciones es ', contraseña)



