import argparse

""" Diseño de datos:
    Para representar a las personas usamos una tupla de 5 elementos de la siguiente forma:
    (NombreYApellido,Localidad,Edad,Genero,Interes) donde todos los datos personal de cada persona
    son representados a traves de un string
    
    Luego,las localidades y las personas que residen en ella, las representamos con un diccionario donde las keys seran las distintas
    localidades y los valores asociados una lista de personas representadas por una tupla de 4 elementos que son sus datos en forma de string
    (NombreYApellido,Edad,Genero,Interes)"""

""" Pasar_a_tupla: Lista(Lista(Strings)) --> Lista(Tuplas)
    Recibe una lista de listas de strings, a cada lista de la lista la pasa a una tupla con sus strings
    sin los espacios o caracteres inncesarios, por eso utilizamos la funcion strip"""
def normalizar_lista(lista):
    nuevaLista = []
    for [nombre, apellido, localidad, edad, genero, interes] in lista:
        nuevaLista.append([nombre.strip() + " " + apellido.strip(), localidad.strip(), edad.strip(), genero.strip(), interes.strip()])
    return nuevaLista

""" EliminarDeLaLista: List List
    Toma una lista y una lista subconjunto de la primera, elimina de la primer lista todos los elementos de la segunda
    "difererencia de conjuntos".
    Utilizamos remove, el cual sirve para poder eliminar un objeto a seleccionar de una lista """
def eliminar_sublista (lista1, lista2):
    for elem in lista2:
            lista1.remove(elem) 

"""Crear_Diccionario_de_Localidades: Lista(Tuplas) --> Dictionary
   Toma una Lista de tuplas de personas, retorna un diccionario donde las keys son localidades y sus valores asociados una lista de
   tuplas de personas que son residentes de la localidad"""
def diccionario_localidades(lista):
    localidades = {}
    for (nombreApellido, localidad, edad, genero, interes) in lista:
        if localidad in localidades.keys():
            localidades[localidad].append([nombreApellido, edad, genero, interes])
        else:
            localidades[localidad] = [[nombreApellido, edad, genero, interes]]
    return localidades
""" EscribirNoPareja: File List(Tuplas) String
    Toma un archivo, una lista de tuplas de personas y la razon de por qué no formaron pareja.
    Escribe sobre el archivo todos los datos de las persona de la lista
    Utilizamos format para que la funcion sea mas legible y amigable con la persona que vaya a leer el codigo"""
def escrbir_razon (file, razon):
    if razon == 0:
        file.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif razon == 1:
        file.write("Estas personas no formaron parejas por ser asexuales\n")
    elif razon == 2:
        file.write("Estas personas no pudieron formar pareja por ser las unicas en su localidad\n")
    elif razon == 3:
        file.write("Estas personas no pudieron formar pareja en su localidad\n")


""" SepararPor: Lista(Tuplas) String ---> Lista(Listas(Tuplas))
    Recibe una lista de tuplas y forma una lista de lista de tuplas segun el Dato.
    Si el Dato es Edad, crea una lista de 3 listas donde cada una representa un grupo etario
    la primera de 11 a 14 años, la segunda de 15 a 17 años y la tercera de 18 años en adelante
    Si el Dato es Sexo, crea una lista de 6 listas donde cada representa a un genero y su interes
    La primera son Hombres Heterosexules, la segundd Mujeres Heterosexuales
    la tercera Hombres Homosexuales, la cuarta Mujeres Homosexuales
    la quinta Hombres Bisexuales, la sexta Mujeres Bisexuales"""
def SepararPor (Lista, Dato):
    if Dato == "Edad":
        Personas_11_y_14 = []
        Personas_15_y_17 = []
        Personas_18_mas = []
        for Persona in Lista:
            if int(Persona[1]) < 15:
                Personas_11_y_14 += [Persona]
            elif int(Persona[1]) < 18:
                Personas_15_y_17 += [Persona]
            else:
                Personas_18_mas += [Persona]
        ListaFinal = [Personas_11_y_14] + [Personas_15_y_17] + [Personas_18_mas]
    
    elif Dato == "Genero":
        HombresHetero = []
        MujeresHetero = []
        HombresHomo= []
        MujeresHomo = []
        HombresBi = []
        MujeresBi = []
        for Persona in Lista:
            if Persona[2] == "M" and Persona[3] == "F":
                HombresHetero += [Persona]
            elif Persona[2] == "F" and Persona[3] == "M":
                MujeresHetero += [Persona]
            elif Persona[2] == "M" and Persona[3] == "M":
                HombresHomo += [Persona]
            elif Persona[2] == "F" and Persona[3] == "F":
                MujeresHomo += [Persona]
            elif Persona[2] == "M" and Persona[3] == "A":
                HombresBi += [Persona]
            elif Persona[2] == "F" and Persona[3] == "A":
                MujeresBi += [Persona]
        ListaFinal = [HombresHetero] + [MujeresHetero] + [HombresHomo] + [MujeresHomo] + [HombresBi] + [MujeresBi]
    return ListaFinal

""" Descartados: Lista(Tuplas) String --> Lista(Tuplas)
    Recibe una lista de tuplas de personas y una condicion de descarte, si es la persona es menor de 10 años o si es asexual,
    devuelve una lista de tuplas de personas que cumplan con la condicion"""   
def descartar (lista):
    resultado = [[],[],[],[]]
    for (nombreApellido, localidad, edad, genero, interes) in lista:      
        if int(edad) <= 10:
            resultado[0].append([nombreApellido,localidad, edad, genero, interes])
    eliminar_sublista (lista, resultado[0])
    for (nombreApellido, localidad, edad, genero, interes) in lista:
        if interes == "N":
            resultado[1].append([nombreApellido, localidad, edad, genero, interes])
    eliminar_sublista (lista, resultado[1])
    return resultado

""" matchHetero: File List(Tuplas) List(Tuplas) String
    Recibe un Archivo, dos listas de Genero e Interes y la localidad donde se encuentra.
    Empareja los primeros elementos de cada lista escribiendolos sobre el archivo y luego
    los elimina de las respectivas listas"""
def matchHetero (parejas, lista1, lista2, localidad):
    while lista1!=[] and lista2!=[]:
        parejas.append([lista1[0],lista2[0],localidad])
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
""" matchHomo: File List(Tuplas) String
    Recibe un archivo, una lista de Genero e Interes y la localidad donde se encuentra.
    Empareja el primer elemento con el siguiente escribiendolos sobre el archivo y luego
    los elimina de la lista"""
def matchHomo (parejas, lista, localidad):
    while lista != [] and len(lista)!= 1:
        parejas.append([lista[0],lista[1],localidad])
        lista.remove(lista[0])
        lista.remove(lista[0])
""" Matching: Dictionary -> List(List(Tuplas))
    Recibe un diccionario de Localidades. Luego, por cada Localidad, separa por edades en 3 listas y a cada
    grupo etario en 6 listas de Genero e Interes. Despues, forma las parejas.
    Al mismo tiempo, forma una lista de dos listas donde la primera contiene todos los nombres de las personas
    que estan solas en su localidad y la otra, los nombres de las personas que no pudieron formar pareja.
    Retorna esa lista""" 
def matching(listaPersonas, noParejas, fParejas, fNoParejas):
    localidades = diccionario_localidades(listaPersonas)
    listaPersonas.clear()
    parejas = []
    for localidad in localidades.keys():
        if len(localidades[localidad]) == 1:
            persona = localidades[localidad][0]
            noParejas[2].append([persona[0],localidad,persona[1],persona[2],persona[3]])
        else:
            ListaPorEdades = SepararPor(localidades[localidad],"Edad")
            ListaPorEdades_Y_Sexo = []
            for Edad in ListaPorEdades:
                ListaPorEdades_Y_Sexo += [SepararPor(Edad,"Genero")]
            for listaEdad in ListaPorEdades_Y_Sexo:
                matchHetero(parejas,listaEdad[0],listaEdad[1], localidad) #Primero matchea hombres hetero con mujeres hetero
                matchHomo(parejas, listaEdad[2], localidad)                #Match de hombres homosexuales
                matchHomo(parejas, listaEdad[3], localidad)                #Match de mujeres homosexuales
                matchHetero(parejas, listaEdad[0], listaEdad[5], localidad) #Match de los hombres hetero que no pudieron formar pareja con mujeres bisexuales
                matchHetero(parejas, listaEdad[1], listaEdad[4], localidad) #Match de las mujeres hetero que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, listaEdad[2], listaEdad[4], localidad) #Match de los hombres homosexuales que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, listaEdad[3], listaEdad[5], localidad) #Match de los mujeres homosexuales que no pudieron formar pareja con mujeres bisexuales
                bisexuales = listaEdad[4] + listaEdad[5]                       #Bisexuales que todavia no formaron pareja
                matchHomo(parejas, bisexuales, localidad)         #Match personas bisexuales
                for persona in listaEdad[0] + listaEdad[1] + listaEdad[2] + listaEdad[3] + bisexuales:
                    noParejas[3].append([persona[0], localidad, persona[1], persona[2], persona[3]])
    
    with open(fParejas, "w") as fileParejas:
        for [persona1, persona2, localidad] in parejas:
            fileParejas.write("{0}, {1}, {2}, {3} -- {4}, {5}, {6}, {7} -- {8}\n".format(persona1[0],persona1[1],persona1[2],persona1[3],
                                                                                         persona2[0],persona2[1],persona2[2],persona2[3],localidad))
    with open(fNoParejas, "w") as fileNoParejas:
        for index in range(0,3):
            escrbir_razon (fileNoParejas, index)
            for [nombreApellido, localidad, edad, genero, interes] in noParejas[index]:
                fileNoParejas.write("{0}, {1}, {2}, {3}, {4}\n".format(nombreApellido, localidad, edad, genero, interes))     
                
#FUNCION PRINCIPAL
"""dado que en el archivo de entrada, cada linea representa los datos de una persona, los mismos estan separados por una coma, y al leer el archivo se obtiene un string de la linea entera,
para obtener una lista de sus datos aislados en forma de string, utilizamos la funcion split(,) para que los separe"""
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "entrada",
        help= "Nombre archivo de entrada"
    )
    parser.add_argument(
        "parejas",
        help="Nombre archivo de salida con parejas"
    )
    parser.add_argument(
        "noParejas",
        help="Nombre archivo de salida con quienes no formaron pareja"
    )

    args = parser.parse_args()

    with open(args.entrada, "r", encoding="utf-8") as entradaFile:
        listaPersonas = list(map(lambda string: string.split(","), entradaFile.readlines()))

    listaPersonas = normalizar_lista(listaPersonas)       
    noParejas = descartar(listaPersonas)
    matching(listaPersonas, noParejas, args.parejas, args.noParejas)

if __name__ == "__main__":
    main()
