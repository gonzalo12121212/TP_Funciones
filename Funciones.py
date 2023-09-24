
def area_de_un_circulo (radio:float)->float:
    """ Calculo del area de un circulo

    Args:
        PI(float) : valor de pi
        area(float): valor de pi por radio al cuadrado

    Returns:
        area(float): devuelve el valor del area del circulo solicitado 
    """
    PI = 3.1416
    area = PI * radio**2
    return area

def verificar_par_impar (numero: int)->int:
    """ Verificacion de si un numero es par o impar

    Args:
        numero (int): recibe un entero par o impar

    Returns:
        numero (int):  devuelve un entero par o impar
    """
    mensaje = f"El número {numero} es {'par' if numero % 2 == 0 else 'impar'}."
    return print(mensaje)

def sumar_elementos(numeros:int)->int:
    """Sumas entre elementos(int)

    Args:
        numeros (int): recibe un entero

    Returns:
        numeors(int): duelve la suma de los enteros ingresados
    """
    suma = 0
    for elemento in numeros:
        suma += elemento
    return suma

def numero_max (numero1: int, numero2: int, numero3:int)->int:
    """Encuentra el numero mas grande entres elementos ingresados

    Args:
        numero1 (int): Valor numerico de la primera variable
        numero2 (int): Valor numerico de la segunda variable
        numero3 (int): Valor numerico de la tercera variable

    Returns:
        int: Devuelve el valor numerico mas grande
    """
    if numero1 > numero2 and numero1 > numero3:
        print(f"El numero mas grande es: {numero1}")
        return numero1
    elif numero2 > numero1 and numero2 > numero3:
        print(f"El numero mas grande es: {numero2}")
        return numero2
    else:
        print(f"El numero mas grande es: {numero3}")
        return numero3

def invertir_cadena(cadena:str)->str:
    """Invierte la cadena de texto ingresado

    Args:
        cadena (str): recibe un objeto tipo str

    Returns:
        str: devuelve la cadena de tecto invertido
    """
    cadena_invertida = ""
    for caracter in cadena:
        cadena_invertida = caracter + cadena_invertida
    return cadena_invertida

def ordenar_lista (lista_palabras:str)->str:
    """Recibe una lista de palabras y la ordena de forma alfabetica

    Args:
        lista_palabras (str): recibe la cadena de texto 

    Returns:
        str: devuele la lista con la cadena de texto ordenada
    """
    n = len(lista_palabras)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lista_palabras[j].lower() > lista_palabras[j+1].lower():
                lista_palabras[j], lista_palabras[j+1] = lista_palabras[j+1], lista_palabras[j]
    return lista_palabras

def calculo_de_potencia(base:float, exponente:float)->float:
    """Calcula la potencia de un numero

    Args:
        base (float): Valor numerico de la base
        exponente (float): Valor numerico de la potencia

    Returns:
        float: Devuelve la potencia del numero ingresado
    """
    resultado = base ** exponente
    return resultado

def lista_num_pares(lista_par:int)->int:
    """Crea una lista con solo numeros pares

    Args:
        lista_par (int): recibe una lista con enteros

    Returns:
        int: devuelve una lista con solo numeros pares
    """
    numeros_pares = [numero for numero in lista_par if numero % 2 == 0]
    numeros_pares.sort()
    return numeros_pares

def lista_producto (lista:int)->int:
    """Calcula el producto de todos los numeros dentro de la lista

    Args:
        lista (int): recibe una lista con solo numeros enteros

    Returns:
        int: devuelve el producto de todos los elementos
    """
    producto = 1
    for numero in lista:
        producto *= numero
    return producto

def cadena_palindromo(cadena_texto:str)->str:
    """Verifica si una cadena de texto es palindromo

    Args:
        cadena_texto (str): Recibe una cadena de stexto(str)

    Returns:
        bool: devuelve true si verdadero o false si es negativo 
    """
    cadena = ''.join(e.lower() for e in cadena_texto if e.isalnum())
    return cadena == cadena[::-1]



























    

