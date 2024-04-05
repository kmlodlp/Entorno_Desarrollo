"""
Funcion: Ejercicio1
Recibe: Lee 6 numeros por teclados 
Retorna: Un vector donde se encuentran todos los numeros registrados
         y un vector con los multiplos de 2
Restricciones: No admite mas de 6 numeros y recibe datos int
"""

def Ejercicio1():
    try:
        V=[]
        Mul2=[]
        rango=6
        for i in range(rango):
            num= int(input("\nIngrese un numero "+str(i)+" de "+str(rango)+" "))
            V.append(num)
        for val in V:
            if(val%2==0):
                Mul2.append(val)
        if(len(Mul2)==0):
            Mul2="No se recibieron Multiplos de 2"

        return (V,Mul2)
    except: 
        print("El valor ingresado debe ser de numerico")

print(Ejercicio1())