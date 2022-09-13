def ver(n):
    try:
        n=int(n)
    except:
        n= ver(input("Caracter no valido"))
        return n