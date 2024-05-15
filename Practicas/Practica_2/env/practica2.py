class persona:

    def __init__():
        pass

    def __init__(self,nombre,edad,dna):
        self.nombre = nombre
        self.edad = int(edad)
        self.dna = dna
    
    def mayor_edad(self):
        if(self.edad < 18):
            return False
        else:
            return True
        
matriz = [["Daniel",24,"28675203"],["Daniela",17,"32987103"],["Diego",21,"31987103"]]#matriz con los datos de prueba

def mostrar(matriz):
    for i in range(0,len(matriz)):
        objeto = persona(matriz[i][0],matriz[i][1],matriz[i][2])
        if(objeto.mayor_edad() and validar_letra(matriz[i][0]) and validar_edad(matriz[i][2])):
            print(f"{matriz[i][0]} ci {matriz[i][1]} de {matriz[i][2]} edad")

def validar_letra(cadena):
    cadena = str(cadena)
    if (cadena==""):
        return False
    for i in cadena:
        if(i in "1234567890" or i==""):
            return False
    return True

def validar_edad(edad):
    edad = int(edad)
    if edad < 0:
        return False
    elif edad < 18:
        return False
    return True
mostrar(matriz)