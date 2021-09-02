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
def Crear_Diccionario_de_Localidades(ListaDePersonas):
    DiccionarioLocalidades = dict()
    for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:
        if Localidad in DiccionarioLocalidades.keys():
            DiccionarioLocalidades[Localidad] += [(NombreYApellido,Edad,Genero,Interes)]
        else:
            DiccionarioLocalidades[Localidad] = [(NombreYApellido,Edad,Genero,Interes)]
    return DiccionarioLocalidades
""" EscribirNoPareja: File List(Tuplas) String
    Toma un archivo, una lista de tuplas de personas y la razon de por qué no formaron pareja.
    Escribe sobre el archivo todos los datos de las persona de la lista
    Utilizamos format para que la funcion sea mas legible y amigable con la persona que vaya a leer el codigo"""
def EscribirNoPareja (Archivo_a_Escribir,ListaDePersonas,Razon):
    if Razon == "Menores":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif Razon == "Asexuales":
        Archivo_a_Escribir.write("Estas personas no formaron parejas por ser asexuales\n")
    elif Razon == "Solteros":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja en su localidad\n")
    elif Razon == "Unicos":
        Archivo_a_Escribir.write("Estas personas no pudieron formar pareja por ser las unicas en su localidad\n")
    for (NombreYApellido,Localidad,Edad,Genero,Interes) in ListaDePersonas:
        Archivo_a_Escribir.write("{0}, {1}, {2}, {3}, {4}\n".format(NombreYApellido,Edad,Genero,Interes,Localidad))

""" EscribirParejas: File Tupla(Persona) Tupla(Persona) String
    Recibe el archivo a escribir, dos personas que formaran pareja y su localidad.
    Escribe sobre el archivo la siguiente linea:
    NombreYApellido, Eddd, Genero, Interes -- NombreYApellido, Eddd, Genero, Interes -- Localidad"""
def EscribirParejas (Archivo,Persona1,Persona2,Localidad):
    Archivo.write("{0}, {1}, {2}, {3} -- {4}, {5}, {6}, {7} -- {8}\n".format(Persona1[0],Persona1[1],Persona1[2],Persona1[3], Persona2[0],Persona2[1],Persona2[2],Persona2[3],Localidad))


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
    resultado = [[],[]]
    for (nombreApellido, localidad, edad, genero, interes) in lista:      
        if int(edad) <= 10:
            resultado[0].append([nombreApellido,localidad, edad, genero, interes])
    eliminar_sublista (lista, resultado[0])
    for (nombreApellido, localidad, edad, genero, interes) in lista:
        if interes == "N":
            resultado[1].append([nombreApellido, localidad, edad, genero, interes])
    eliminar_sublista (lista, resultado[1])
    return resultado

""" MatchearHeterosexuales: File List(Tuplas) List(Tuplas) String
    Recibe un Archivo, dos listas de Genero e Interes y la localidad donde se encuentra.
    Empareja los primeros elementos de cada lista escribiendolos sobre el archivo y luego
    los elimina de las respectivas listas"""
def MatchearHeterosexuales (Archivo,lista1,lista2,localidad):
    while lista1!=[] and lista2!=[]:
        EscribirParejas(Archivo,lista1[0],lista2[0],localidad)
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])
""" MatchearHomosexuales: File List(Tuplas) String
    Recibe un archivo, una lista de Genero e Interes y la localidad donde se encuentra.
    Empareja el primer elemento con el siguiente escribiendolos sobre el archivo y luego
    los elimina de la lista"""
def MatchearHomosexuales (Archivo,lista, localidad):
    while lista != [] and len(lista)!= 1:
        EscribirParejas (Archivo,lista[0],lista[1],localidad)
        lista.remove(lista[0])
        lista.remove(lista[0])
""" Matching: Dictionary -> List(List(Tuplas))
    Recibe un diccionario de Localidades. Luego, por cada Localidad, separa por edades en 3 listas y a cada
    grupo etario en 6 listas de Genero e Interes. Despues, forma las parejas.
    Al mismo tiempo, forma una lista de dos listas donde la primera contiene todos los nombres de las personas
    que estan solas en su localidad y la otra, los nombres de las personas que no pudieron formar pareja.
    Retorna esa lista""" 
def matching(Diccionario):
    PersonasUnicas = []
    PersonasSolteras = []
    ParejasFile = open("SalidaParejas.txt","w")
    for Localidad in Diccionario.keys():
        if len(Diccionario[Localidad]) == 1:
            Persona = Diccionario[Localidad][0]
            PersonasUnicas += [(Persona[0],Localidad,Persona[1],Persona[2],Persona[3])]
        else:
            ListaPorEdades = SepararPor(Diccionario[Localidad],"Edad")
            ListaPorEdades_Y_Sexo = []
            for Edad in ListaPorEdades:
                ListaPorEdades_Y_Sexo += [SepararPor(Edad,"Genero")]
            for listaEdad in ListaPorEdades_Y_Sexo:
                MatchearHeterosexuales(ParejasFile,listaEdad[0],listaEdad[1],Localidad) #Primero matchea hombres hetero con mujeres hetero
                MatchearHomosexuales(ParejasFile,listaEdad[2],Localidad)                #Match de hombres homosexuales
                MatchearHomosexuales(ParejasFile,listaEdad[3],Localidad)                #Match de mujeres homosexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[0],listaEdad[5],Localidad) #Match de los hombres hetero que no pudieron formar pareja con mujeres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[1],listaEdad[4],Localidad) #Match de las mujeres hetero que no pudieron formar pareja con hombres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[2],listaEdad[4],Localidad) #Match de los hombres homosexuales que no pudieron formar pareja con hombres bisexuales
                MatchearHeterosexuales(ParejasFile,listaEdad[3],listaEdad[5],Localidad) #Match de los mujeres homosexuales que no pudieron formar pareja con mujeres bisexuales
                BisexualesRestantes = listaEdad[4] + listaEdad[5]                       #Bisexuales que todavia no formaron pareja
                MatchearHomosexuales(ParejasFile,BisexualesRestantes,Localidad)         #Match personas bisexuales
                for Persona in listaEdad[0] + listaEdad[1] + listaEdad[2] + listaEdad[3] + BisexualesRestantes:
                    PersonasSolteras += [(Persona[0],Localidad,Persona[1],Persona[2],Persona[3])]
                   
    ParejasFile.close()
    return [PersonasUnicas] + [PersonasSolteras]
                
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
    #localidades = Crear_Diccionario_de_Localidades(listaPersonas)
    #matching(localidades)



if __name__ == "__main__":
    main()
