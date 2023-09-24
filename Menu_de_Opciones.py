import Funciones 
 
def mostrar_menu():
    
    print("1. Calcular el area de un circulo")
    print("2. Verificar si el numero es par o impar")
    print("3. Sumas de elementos ingresados")
    print("4. Identificar el numero mas grande entre tres elementos")
    print("5. Invertir cadena ingresada")
    print("6. Ordenar alfabeticamente una lista de palabras")
    print("7. Calcular la potencia de un numero")
    print("8. Lista de numeros solo pares")
    print("9. Lista de numeros con el producto de todos los elementos hecho")
    print("10. Verificar si su cadena de texto es palindromo")
    print("11. Cerrar menu de opciones")
    print("")

def opcion_1():
    try:
        radio =float(input("Ingresar valor para calcular el area del circulo: "))
        print("")
        print(f"El valor del area del circulo es: {Funciones.area_de_un_circulo(radio)} ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")
    

def opcion_2():
    try:
        numero = int(input("Ingrese un valor numerico: "))
        print("")
        print(f"{Funciones.verificar_par_impar(numero)} ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")

def opcion_3():
    lista_numeros = []
    try:
        numero = input("Ingrese los elementos que quiera sumar: ")
        numero_ingresado = int(numero)
        while True:
            mas_elementos = input("Quiere ingresar otro elemento? S/N: ")
            if not ( mas_elementos == "S" or mas_elementos == "s"):
                break
            else:
                cant_numero = input("Ingrese los elementos que quiera sumar: ")
                cant_numero_ingresado = int(cant_numero)
                lista_numeros.append(cant_numero_ingresado)
    except:
        print("Ingrese un numero digito valido")

    lista_numeros.append(numero_ingresado)
    resultado = Funciones.sumar_elementos(lista_numeros)
    print("")
    print(f"La suma de los elementos es: {Funciones.sumar_elementos(lista_numeros)}")

def opcion_4 ():
    try:
        numero1 = int(input("Ingrese el primer valor numerico: "))
        numero2 = int(input("Ingrese el segundo valor numerico: "))
        numero3 = int(input("Ingrese el tercer valor numerico: "))
        print("")
        print(f"{Funciones.numero_max(numero1 , numero2 , numero3)} ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")

def opcion_5 ():
    try:
        cadena = input("Ingrese la cadena que desea invertir: ")
        print(f"Aca esta la cadena invertida:  {Funciones.invertir_cadena(cadena)}")
    except:
        print("Ingrese una cadena de texto valida")

def opcion_6 ():
    palabras_ordenadas = []
    try:
        palabras_ingresadas = input("Ingrese las palabras que desea ordenar alfabeticamente: ")
        while True:
            mas_elementos = input("Quiere ingresar mas palabras? S/N: ")
            if not (mas_elementos == "S" or mas_elementos == "s"):
                break
            else:
                mas_listas_palabras = input("Ingrese las palabras que desea ordenar alfabeticamente: ")
                palabras_ordenadas.append(mas_listas_palabras)
    except:
        print("Ingrese una cadena de texto valida")

    palabras_ordenadas.append(palabras_ingresadas)
    lista_palabras = Funciones.ordenar_lista(palabras_ordenadas)
    print("")
    print(f"{Funciones.ordenar_lista(lista_palabras)}")

def opcion_7 ():
    try:
        base = float(input("Ingrese el valor de base: "))
        exponente = float(input("Ingrese el valor del exponente: "))
        print("")
        print(f"Aca esta la potencia pedida:  {Funciones.calculo_de_potencia(base, exponente)}")
    except:
        print("Reintente ingresando un valor numerico, porfavor")    

def opcion_8 ():
    lista_num_pares = []
    try:
        numeros_pares= int(input("Ingrese el numero que desee: "))
        while True:
            mas_elementos = input("Quiere ingresar mas palabras? S/N: ")
            if not (mas_elementos == "S" or mas_elementos == "s"):
                break
            else:
                mas_numeros_pares = int(input("Ingrese el numero que desee: "))
                lista_num_pares.append(mas_numeros_pares)
        lista_num_pares.append(numeros_pares)
        lista_pares = Funciones.lista_num_pares(lista_num_pares)
        print("")
        print(f"Aca esta la lista con solo numeros pares:  {Funciones.lista_num_pares(lista_pares)}")
    except:
        print("Reintente ingresando un valor numerico, porfavor")

def opcion_9 ():
    lista_num_producto = []
    try:
        numeros = int(input("Ingrese el numero que desee: "))
        while True:
            mas_elementos = input("Quiere ingresar mas palabras? S/N: ")
            if not (mas_elementos == "S" or mas_elementos == "s"):
                break
            else:
                mas_numeros = int(input("Ingrese el numero que desee: "))
                lista_num_producto.append(mas_numeros)
        lista_num_producto.append(numeros)
        lista_final = Funciones.lista_producto(lista_num_producto)
        print("")
        print(f"Aca esta la lista con el producto ya calculado:  {lista_final}")
    except:
        print("Error: Reintente ingresando un valor numerico, porfavor.")

def opcion_10 ():
    try:
        cadena = input("Ingrese la cadena de texto: ")
        print("")
        print(f"Aca esta la cadena de texto verificada:  {Funciones.cadena_palindromo(cadena)}")
    except:
        print("Reintente ingresando una cadena de texto valido, porfavor") 





