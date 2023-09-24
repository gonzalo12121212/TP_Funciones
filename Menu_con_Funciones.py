import Funciones 
import Menu_de_Opciones

while True:

    print("T.P Funciones    ")
    print("")
    print("*** Menu de Opciones ***")
    print("")

    Menu_de_Opciones.mostrar_menu()

    try:
        opcion = input("Selecciona una opción: ")
    except:
        print("Reintente ingresando un valor numerico, porfavor")

    if opcion == '1':
        Menu_de_Opciones.opcion_1()
        break

    elif opcion == '2':
        Menu_de_Opciones.opcion_2()
        break

    elif opcion == '3':
        Menu_de_Opciones.opcion_3()
        break

    elif opcion == '4':
        Menu_de_Opciones.opcion_4()
        break

    elif opcion == '5':
        Menu_de_Opciones.opcion_5()
        break

    elif opcion == '6':
        Menu_de_Opciones.opcion_6()
        break

    elif opcion == '7':
        Menu_de_Opciones.opcion_7()
        break

    elif opcion == '8':
        Menu_de_Opciones.opcion_8()
        break

    elif opcion == '9':
        Menu_de_Opciones.opcion_9()
        break

    elif opcion == '10':
        Menu_de_Opciones.opcion_10()
        break

    elif opcion == '11':
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.") 
