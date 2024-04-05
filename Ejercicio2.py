"""
Funcion: Ejercicio2
Recibe: El valor que va a tomar un numerado y el valor que va a tomar un denominador
Retorna: La division de estos valores si la division es posible
"""

def Ejercicio2():
    try:
        condicion=True
        while(condicion):
            Numerador= int(input("\nIngrese un valor para el numerador: "))
            Denominador= int(input("\nIngrese un valor para el denominador: "))
            Resultado=Numerador/Denominador
            print(str(Numerador)+"/"+str(Denominador)+"= "+str(Resultado)+"\n")
            
    except ZeroDivisionError:
        print("No se admite division ya que no esta definida")
    except ValueError:
        print("El Valor ingresado debe ser numerico")
    

    