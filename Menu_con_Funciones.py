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
    try:
        match opcion :
            case '1':
                opcion_1()
                break

            case '2':
                opcion_2()
                break

            case '3':
                opcion_3()
                break

            case '4':
                opcion_4()
                break

            case '5':
                opcion_5()
                break

            case '6':
                opcion_6()
                break

            case '7':
                opcion_7()
                break

            case '8':
                opcion_8()
                break

            case '9':
                opcion_9()
                break

            case '10':
                opcion_10()
                break

            case '11':    
                break

    except:
        print("Opción inválida. Inténtalo de nuevo.") 
