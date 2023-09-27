from Funciones import*
from Menu_de_Opciones import*

while True:

    print("T.P Funciones    ")
    print("")
    print("*** Menu de Opciones ***")
    print("")

    mostrar_menu()

    try:
        opcion = input("Selecciona una opción: ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")

    if opcion == '1':
        opcion_1()
        break

    elif opcion == '2':
        opcion_2()
        break

    elif opcion == '3':
        opcion_3()
        break

    elif opcion == '4':
        opcion_4()
        break

    elif opcion == '5':
        opcion_5()
        break

    elif opcion == '6':
        opcion_6()
        break

    elif opcion == '7':
        opcion_7()
        break

    elif opcion == '8':
        opcion_8()
        break

    elif opcion == '9':
        opcion_9()
        break

    elif opcion == '10':
        opcion_10()
        break

    elif opcion == '11':
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.") 
