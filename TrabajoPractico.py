import argparse

def normalizar_lista(lista):
    nuevaLista = []
    for [nombre, apellido, localidad, edad, genero, interes] in lista:
        nuevaLista.append([nombre.strip() + " " + apellido.strip(), localidad.strip(), edad.strip(), genero.strip(), interes.strip()])
    return nuevaLista

def eliminar_sublista (lista1, lista2):
    for elem in lista2:
            lista1.remove(elem) 

def diccionario_localidades(lista):
    localidades = {}
    for (nombreApellido, localidad, edad, genero, interes) in lista:
        if localidad in localidades.keys():
            localidades[localidad].append([nombreApellido, edad, genero, interes])
        else:
            localidades[localidad] = [[nombreApellido, edad, genero, interes]]
    return localidades

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
def separar_por (lista, dato):
    if dato == "Edad":
        personas11_14 = []
        personas15_17 = []
        personas18 = []
        for persona in lista:
            if int(persona[1]) < 15:
                personas11_14 += [persona]
            elif int(persona[1]) < 18:
                personas15_17 += [persona]
            else:
                personas18 += [persona]
        listaFinal = [personas11_14] + [personas15_17] + [personas18]
    
    elif dato == "Genero":
        heteroM = []
        heteroF = []
        homoM= []
        homoF = []
        biM = []
        biF = []
        for persona in lista:
            if persona[2] == "M" and persona[3] == "F":
                heteroM += [persona]
            elif persona[2] == "F" and persona[3] == "M":
                heteroF += [persona]
            elif persona[2] == "M" and persona[3] == "M":
                homoM += [persona]
            elif persona[2] == "F" and persona[3] == "F":
                homoF += [persona]
            elif persona[2] == "M" and persona[3] == "A":
                biM += [persona]
            elif persona[2] == "F" and persona[3] == "A":
                biF += [persona]
        listaFinal = [heteroM] + [heteroF] + [homoM] + [homoF] + [biM] + [biF]
    return listaFinal
  
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

def matchHetero (parejas, lista1, lista2, localidad):
    while lista1!=[] and lista2!=[]:
        parejas.append([lista1[0],lista2[0],localidad])
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])

def matchHomo (parejas, lista, localidad):
    while lista != [] and len(lista)!= 1:
        parejas.append([lista[0],lista[1],localidad])
        lista.remove(lista[0])
        lista.remove(lista[0])

def matching(listaPersonas, noParejas, fParejas, fNoParejas):
    localidades = diccionario_localidades(listaPersonas)
    listaPersonas.clear()
    parejas = []
    for localidad in localidades.keys():
        if len(localidades[localidad]) == 1:
            persona = localidades[localidad][0]
            noParejas[2].append([persona[0],localidad,persona[1],persona[2],persona[3]])
        else:
            listaEdades = separar_por(localidades[localidad],"Edad")
            listaEdades_Sexo = []
            for edad in listaEdades:
                listaEdades_Sexo += [separar_por(edad,"Genero")]
            for grupo in listaEdades_Sexo:
                matchHetero(parejas,grupo[0],grupo[1], localidad)   #Primero matchea hombres hetero con mujeres hetero
                matchHomo(parejas, grupo[2], localidad)                 #Match de hombres homosexuales
                matchHomo(parejas, grupo[3], localidad)                 #Match de mujeres homosexuales
                matchHetero(parejas, grupo[0], grupo[5], localidad) #Match de los hombres hetero que no pudieron formar pareja con mujeres bisexuales
                matchHetero(parejas, grupo[1], grupo[4], localidad) #Match de las mujeres hetero que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, grupo[2], grupo[4], localidad) #Match de los hombres homosexuales que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, grupo[3], grupo[5], localidad) #Match de los mujeres homosexuales que no pudieron formar pareja con mujeres bisexuales
                bisexuales = grupo[4] + grupo[5]                    #Bisexuales que todavia no formaron pareja
                matchHomo(parejas, bisexuales, localidad)                   #Match personas bisexuales
                for persona in grupo[0] + grupo[1] + grupo[2] + grupo[3] + bisexuales:
                    noParejas[3].append([persona[0], localidad, persona[1], persona[2], persona[3]])
    
    with open(fParejas, "w") as fileParejas:
        for [persona1, persona2, localidad] in parejas:
            fileParejas.write("{0}, {1}, {2}, {3} -- {4}, {5}, {6}, {7} -- {8}\n".format(persona1[0],persona1[1],persona1[2],persona1[3],
                                                                                         persona2[0],persona2[1],persona2[2],persona2[3],localidad))
    with open(fNoParejas, "w") as fileNoParejas:
        for index in range(4):
            escrbir_razon (fileNoParejas, index)
            for [nombreApellido, localidad, edad, genero, interes] in noParejas[index]:
                fileNoParejas.write("{0}, {1}, {2}, {3}, {4}\n".format(nombreApellido, localidad, edad, genero, interes))     
                
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
