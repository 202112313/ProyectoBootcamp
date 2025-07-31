import pandas as pd

#vamos a crear una variable que almacene los números del 1-5

numeros = [1,2,3,4,5]
estudiantes =[
    {"nombre": "jorge",
    "edad": "31",
    "genero": "m"},
   {"nombre": 'alejo',
    "edad": "21",
    "genero": "m"},
    {"nombre": 'maria',
    "edad": "11",
    "genero": "f",} 
  ]
print(estudiantes)
print(numeros)

estudiantesEstructura = {"nombre":["jorge","alejo","maria"], "edad":[31,21,11],"genero": ["m","m","f"]}

conjuntoDeDatos = pd.DataFrame(estudiantesEstructura)
print(conjuntoDeDatos)

promedioedades = conjuntoDeDatos["edad"].mean()
print("el promedio de las edades es: ", promedioedades)

conjuntoDeDatos.to_excel("archivonuevoexel2.xlsx")
conjuntoDeDatos.to_json("datosnuevos.json")
conjuntoDeDatos.to_csv("archivodedaros.csv")


def multiplicarElNumeroPorDos(listaNumeros):
    for numero in listaNumeros:
        print(numero*2)

#multiplicarElNumeroPorDos(numeros)

diasDeLaSemana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]


def leerDiasDeLaSemana(semana):
    for dia in semana:    
        if dia == "sabado": 
           print("es fin de semana, el dia actual es",dia)
        elif dia == "domingo":
           print("es fin de semana, el dia actual es",dia)
        else:
           print("el dia actual es:",dia)

MesesDelAño = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

        
#leerDiasDeLaSemana(diasDeLaSemana)


while True:

    print("bienvenido usuario")
    print("1. multiplicar lsta de numeros por 2")
    print("2. leer dias de la semana")
    print("3.agregar un elemento o una lista de numeros ")
    print("4.eliminar dia de la semana")
    print("5. eliminar mes del año")
    print("6. salir")

    opcion = input("seleccione una opcion: ")
    if opcion == "1":
       multiplicarElNumeroPorDos(numeros)

    elif opcion == "2":
       leerDiasDeLaSemana(diasDeLaSemana)

    elif opcion == "3":
       NumeroIngresado = int(input("Ingrese numero para agregar a la lista: "))
       numeros.append(NumeroIngresado)
       print(numeros)

    elif opcion =="4":
       diaIngresado = input("ingrese dia para elimnar de la lista: ")
       diasDeLaSemana.remove(diaIngresado)
       print(diasDeLaSemana)

    elif opcion =="5":
       MesDelAño = input("ingrese mes para elimnar de la lista: ")
       MesesDelAño.remove(MesDelAño)
       print(MesesDelAño)

    elif opcion == "6":
        print("gracias por todo")
        break   
    else: 
       print("opcion incorrecta, seleccione una opcion valida")


 
