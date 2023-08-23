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
cada palabra que contieen y la cantidad de veces que aparece (frecuencia).'''


def convertir_a_dic(cadena):
    palabras= cadena.split() #divido la cadena en palabras
    frecuencia_palabras = {} #dicionario para guardar la cadena y su frecuencia
    #conntar frecuencia
    for palabra in palabras:
        palabra.strip(".,!?") #elimino los signos en la cadena
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] +=1
        else:
            frecuencia_palabras[palabra] = 1              
    return frecuencia_palabras

# cadena = input("Ingrese una frase: ")
cadena = '''Estoy usando Python para hacer funciones. 
            Python es facil de entender, por que fue creado con ese proposito. 
            Python en los ultimos tiempos se volvio muy popular'''
diccionario_frecuencias = convertir_a_dic(cadena)
#print("Frecuencia de palabras")
#print(diccionario_frecuencias)

'''4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia.'''

def convertir_dic_a_tupla(dic):
    frecuencia_max= 0
    palabra_max= ""
    
    for palabra,frecuencia in dic.items():
        if frecuencia>frecuencia_max:
            frecuencia_max = frecuencia
            palabra_max=palabra
            
    tupla_frecuencia = (palabra_max,frecuencia_max)
    return tupla_frecuencia

#print("Tupla de Frecuencia de palabras")
#print(convertir_dic_a_tupla(diccionario_frecuencias))

'''5. Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una
cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero
del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el
ejercicio tanto de manera iterativa como recursiva'''
#recursiva
def get_int():
    try:
        valor = int(input("Ingrese un entero: "))
        return valor
    except ValueError:
        print("Invalido, intente de nuevo...")
        return get_int()

#iterativa
def get_int_iterativa():
    while True:
        try:
            num = int(input("Ingrese un entero: "))
            return num
        except ValueError:
            print("Invalido, intente de nuevo...")

    
#llamada a funcion recursiva   
#num = get_int()

#llamada a funcion iterativa   
#num = get_int_iterativa()

# print (num)
# print("El entero es:", num)

'''6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los
siguientes métodos para la clase:
- Un constructor, donde los datos pueden estar vacíos.
- Los setters y getters para cada uno de los atributos. Hay que validar las entradas de
datos.
- mostrar(): Muestra los datos de la persona.
- Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.'''

class Persona:
    
    _nombre = None
    _edad = None
    _DNI = None

    #constructor de la clase
    def __init__(self,nombre,edad,DNI):
        self._nombre= nombre
        self._edad= edad
        self._DNI= DNI
    
    
    #getters y setters
    #El guion bajo antes de nombre en self._nombre es una convención en Python que se utiliza para indicar que el atributo es de carácter privado. 
    def set_nombre(self,nombre):
        if isinstance(nombre,str):
            self._nombre = nombre
        else:
            print("Error: el nombre debe ser en formato texto")
    
    
    def get_nombre(self):
        return self._nombre
    
    
    def set_edad(self,edad):
        if isinstance(edad,int) and edad >= 0:
            self._edad = edad
        else:
            print("Eroor: la edad deber un entero positivo")
    
    
    def get_edad(self):
        return self._edad
    
    
    def set_DNI(self,DNI):
        if isinstance(DNI,str) and DNI.isdigit():
            self._DNI = DNI.replace(".", "").replace(" ", "")
        else:
            print("Error: El DNI debe ser ingresado en formato de dígitos.")
    
    def get_DNI(self):
        return self._DNI
    
    def mostrar(self):
        print("Nombre: ", self._nombre)
        print("Edad: ", self._edad)
        print("DNI: ", self._DNI)
    
    def es_mayor_de_edad(self):
        return self._edad >=18
        
persona1 = Persona(nombre="Roxana",edad=22,DNI=40558202)
#print(persona1.get_nombre())
#print(persona1.get_edad())
#print(persona1.get_DNI())
#persona1.mostrar()
#print(persona1.Es_mayor_de_edad())

'''7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
 mostrar(): Muestra los datos de la cuenta.
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.'''

class Cuenta:
    #properties
    _titular = ""
    _cantidad = 0.0
    #constructor
    def __init__(self,titular,cantidad=None):
        self._titular = titular
        self._cantidad = cantidad
    
    #getters y setters
    
    def get_titular(self):
        return self._titular
    
    def set_titular(self,nuevo_titular):
        self._titular = nuevo_titular
    
    def get_cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print("Titular:",self._titular.get_nombre())
        print("Cantidad:",self._cantidad)
    
    def ingresar(self,cantidad):
        if cantidad > 0:
            self._cantidad += cantidad 
    
    def retirar(self,cantidad):
        self._cantidad -= cantidad
    

cuenta1 = Cuenta(titular=persona1,cantidad=500)
cuenta1.ingresar(100)
cuenta1.retirar(700)
#cuenta1.mostrar()
# print("cuenta1:",cuenta1.get_titular())
# print("cuenta1:",cuenta1.get_cantidad())

'''8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 Un constructor.
 Los setters y getters para el nuevo atributo.
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.'''

class CuentaJoven(Cuenta):
    
    def __init__(self,titular,cantidad,bonificacion=0):
        super().__init__(titular,cantidad)
        self.bonificacion = bonificacion
    def get_bonificacion(self):
        return self._bonificacion 

    def set_bonificacion(self, bonificacion):
        self._bonificacion = bonificacion 
    
    def es_titular_valido(self):
        return self._titular.es_mayor_de_edad() and self._titular.get_edad() < 25
    
    def retirar(self,cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)
        else:
            print("Error: no se puede retirar, titular no valido")
    
    def mostrar(self):
        print("Cuenta Joven")
        super().mostrar()
        print("Bonificacion:", self.bonificacion, "%")

cuenta2 = CuentaJoven(persona1,1000,bonificacion=30)

cuenta2.mostrar()
cuenta2.retirar(200)
cuenta2.mostrar()
        
    






        
        
