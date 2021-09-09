import argparse

def leer_entrada(fEntrada):
    with open(fEntrada, "r", encoding="utf-8") as entradaFile:
        lista = entradaFile.readlines()
    lista = list(map(lambda cadena: cadena.split(","), lista))
    listaPersonas = []
    for persona in lista:
        persona = list(map(lambda cadena: cadena.strip(), persona))
        listaPersonas.append(persona)
    return listaPersonas

def eliminar_sublista (lista1, lista2):
    for elem in lista2:
        lista1.remove(elem) 

def diccionario_localidades(lista):
    localidades = {}
    for persona in lista:
        if persona[2] in localidades.keys():
            localidades[persona[2]].append(persona)
        else:
            localidades[persona[2]] = [persona]
    return localidades

def escrbir_razon (file, razon):
    if razon == 0:
        file.write("Estas personas no formaron parejas por ser menores de 10 años\n")
    elif razon == 1:
        file.write("\nEstas personas no formaron parejas por ser asexuales\n")
    elif razon == 2:
        file.write("\nEstas personas no pudieron formar pareja por ser las unicas en su localidad\n")
    elif razon == 3:
        file.write("\nEstas personas no pudieron formar pareja en su localidad\n")

def separar_edad (lista):
    personas11_14 = []
    personas15_17 = []
    personas18 = []
    for persona in lista:
        if int(persona[3]) < 15:
            personas11_14 += [persona]
        elif int(persona[3]) < 18:
            personas15_17 += [persona]
        else:
            personas18 += [persona]
    return [personas11_14] + [personas15_17] + [personas18]

def separar_genero (lista):
    heteroM = []
    heteroF = []
    homoM= []
    homoF = []
    biM = []
    biF = []
    for persona in lista:
        if persona[4] == "M":
            if persona[5] == "F":
                heteroM += [persona]
            elif persona[5] == "M":
                homoM += [persona]
            else:
                biM += [persona]
        else:
            if persona[5] == "M":
                heteroF += [persona]
            elif persona[5] == "F":
                homoF += [persona]
            else:
                biF += [persona]
    return [heteroM] + [heteroF] + [homoM] + [homoF] + [biM] + [biF]

def descartar (lista):
    resultado = [[],[],[],[]]
    for persona in lista:      
        if int(persona[3]) <= 10:
            resultado[0].append(persona)
    eliminar_sublista (lista, resultado[0])
    for persona in lista:
        if persona[5] == "N":
            resultado[1].append(persona)
    eliminar_sublista (lista, resultado[1])
    return resultado

def matchHetero (parejas, lista1, lista2):
    while lista1!=[] and lista2!=[]:
        parejas.append([lista1[0],lista2[0]])
        lista1.remove(lista1[0])
        lista2.remove(lista2[0])

def matchHomo (parejas, lista):
    while lista != [] and len(lista)!= 1:
        parejas.append([lista[0],lista[1]])
        lista.remove(lista[0])
        lista.remove(lista[0])

def escribir_parejas (parejas, fParejas):
    with open(fParejas, "w", encoding="utf-8") as fileParejas:
        for [persona1, persona2] in parejas:
            nombre1, apellido1, localidad1, edad1, genero1, interes1 = persona1
            nombre2, apellido2, localidad2, edad2, genero2, interes2 = persona2
            fileParejas.write(f"{nombre1}, {apellido1}, {edad1}, {genero1}, {interes1} -- {nombre2}, {apellido2}, {edad2}, {genero2}, {interes2} -- {localidad1}\n")

def escrbir_no_parejas(noParejas, fNoParejas):
    with open(fNoParejas, "w", encoding="utf-8") as fileNoParejas:
        for index in range(4):
            escrbir_razon (fileNoParejas, index)
            for [nombre, apellido, localidad, edad, genero, interes] in noParejas[index]:
                fileNoParejas.write(f"{nombre}, {apellido}, {localidad}, {edad}, {genero}, {interes}\n")

def matching(listaPersonas, fParejas, fNoParejas):
    noParejas = descartar(listaPersonas)
    localidades = diccionario_localidades(listaPersonas)
    parejas = []
    for localidad in localidades.keys():
        if len(localidades[localidad]) == 1:
            persona = localidades[localidad][0]
            noParejas[2].append(persona)
        else:
            listaEdades = separar_edad(localidades[localidad])
            listaEdades_Sexo = []
            for edad in listaEdades:
                listaEdades_Sexo += [separar_genero(edad)]
            for grupo in listaEdades_Sexo:
                matchHetero(parejas,grupo[0],grupo[1])           #Primero matchea hombres hetero con mujeres hetero
                matchHomo(parejas, grupo[2])                     #Match de hombres homosexuales
                matchHomo(parejas, grupo[3])                     #Match de mujeres homosexuales
                matchHetero(parejas, grupo[0], grupo[5])         #Match de los hombres hetero que no pudieron formar pareja con mujeres bisexuales
                matchHetero(parejas, grupo[1], grupo[4])         #Match de las mujeres hetero que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, grupo[2], grupo[4])         #Match de los hombres homosexuales que no pudieron formar pareja con hombres bisexuales
                matchHetero(parejas, grupo[3], grupo[5])         #Match de los mujeres homosexuales que no pudieron formar pareja con mujeres bisexuales
                bisexuales = grupo[4] + grupo[5]                 #Bisexuales que todavia no formaron pareja
                matchHomo(parejas, bisexuales)                   #Match personas bisexuales
                noParejas[3] += grupo[0] + grupo[1] + grupo[2] + grupo[3] + bisexuales
    escribir_parejas (parejas, fParejas)
    escrbir_no_parejas (noParejas, fNoParejas)
                
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

    listaPersonas = leer_entrada(args.entrada)       
    matching(listaPersonas, args.parejas, args.noParejas)

if __name__ == "__main__":
    main()
