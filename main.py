'''1. Escribir una función que calcule el máximo común divisor entre dos números.'''
#usando el algoritmo de Euclides
def mcd(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2 
        num2 = r
    return num1

#print(mcd(6,28));

'''2. Escribir una función que calcule el mínimo común múltiplo entre dos números'''
def mcm(num1, num2):
    producto = num1 * num2
    mcd_resultado = mcd(num1,num2)
    mcm_resultado = producto // mcd_resultado #divicion entera
    return mcm_resultado

#print(mcm(6,28))

'''3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene y la cantidad de veces que aparece (frecuencia).'''


