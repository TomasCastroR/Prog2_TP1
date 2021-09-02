from TrabajoPractico import *

""" El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de una lista de listas de 6 strings con los datos de una persona
    de la forma [Nombre, Apellido, Localidad, Edad, Genero, Interes] y pueden tener espacios al principio o final de cada string
    El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de una lista de personas en quintuplas de strings
    (NombreyApellido, Localidad, Edad, Genero, Interes) """
def test_Pasar_a_Tupla ():
    EjemplosFile = open("Pasar_a_TuplasEjemplos.txt","r")
    ResultadosFile = open("Pasar_a_TuplasResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    ResultadosFile.close()
    listaejemplo1 = eval(LineasEjemplo[0])
    listaejemplo2 = eval(LineasEjemplo[1])
    listaejemplo3 = eval(LineasEjemplo[2])
    listaresultado1 = eval(LineasResultados[0])
    listaresultado2 = eval(LineasResultados[1])
    listaresultado3 = eval(LineasResultados[2])
    assert Pasar_a_Tupla(listaejemplo1) == listaresultado1
    assert Pasar_a_Tupla(listaejemplo2) == listaresultado2
    assert Pasar_a_Tupla(listaejemplo3) == listaresultado3
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de una lista de personas en quintuplas con nombre y apellido, localidad, edad, genero e interes.
   El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de diccionario donde cada key es una localidad y su valor
   asociado es una lista de personas en cuatruplas con nombre y apellido, edad, genero e interes."""
def test_Crear_Diccionario_de_Localidades ():
    EjemplosFile = open("Crear_Diccionario_de_LocalidadesEjemplos.txt","r")
    ResultadosFile = open("Crear_Diccionario_de_LocalidadesResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    ResultadosFile.close()
    ListaTuplaEjemplo1 = eval(LineasEjemplo[0])
    ListaTuplaEjemplo2 = eval(LineasEjemplo[1])
    DiccionarioResultado1 = eval(LineasResultados[0])
    DiccionarioResultado2 = eval(LineasResultados[1])
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo1) == DiccionarioResultado1
    assert Crear_Diccionario_de_Localidades(ListaTuplaEjemplo2) == DiccionarioResultado2
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de lista de personas en cuatruplas con nombre y apellido, edad, genero e interes.
   El archivo de resultados tiene un resultado por linea, dependiendo del segundo argumento que puede ser "Edad" o "Genero" el resultado debe estar:
   En el primer caso, una lista de 3 listas de personas en cuatruplas con nombre y apellido, edad, genero e interes.
   En el segundo, una lista de 6 listas de personas en cuatruplas con nombre y apellido, edad, genero e interes.
   """
def test_SepararPor ():
    EjemplosFile = open("SepararPorEjemplos.txt","r")
    ResultadosFile = open("SepararPorResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    ResultadosFile.close()
    ListaEdadesEjemplo1 = eval(LineasEjemplo[0])
    ListaEdadesEjemplo2 = eval(LineasEjemplo[1])
    ListaGeneroInteresEjemplo1 = eval(LineasEjemplo[2])
    ListaGeneroInteresEjemplo2 = eval(LineasEjemplo[3])
    ListaDeEdadesEsperada1 = eval(LineasResultados[0])
    ListaDeEdadesEsperada2 = eval(LineasResultados[1])
    ListaGeneroInteresEsperada1 = eval(LineasResultados[2])
    ListaGeneroInteresEsperada2 = eval(LineasResultados[3])
    assert SepararPor(ListaEdadesEjemplo1,"Edad") == ListaDeEdadesEsperada1
    assert SepararPor(ListaEdadesEjemplo2,"Edad") == ListaDeEdadesEsperada2
    assert SepararPor(ListaGeneroInteresEjemplo1,"Genero") == ListaGeneroInteresEsperada1
    assert SepararPor(ListaGeneroInteresEjemplo2,"Genero") == ListaGeneroInteresEsperada2
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de lista de personas en quintuplas de strings con nombre y apellido, localidad, edad, genero e interes.
   El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de una lista de personas en quintuplas de strings
   (NombreyApellido, Localidad, Edad, Genero, Interes)"""
def test_Descartados ():
    EjemplosFile = open("DescartadosEjemplos.txt","r")
    ResultadosFile = open("DescartadosResultados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    ResultadosFile.close()
    ListaPersonasEjemplo1 = eval(LineasEjemplo[0])
    ListaPersonasEjemplo2 = eval(LineasEjemplo[1])
    ListaDescartadosEsperada1 = eval(LineasResultados[0])
    ListaDescartadosEsperada2 = eval(LineasResultados[1])
    assert Descartados(ListaPersonasEjemplo1,"Menores") == ListaDescartadosEsperada1
    assert Descartados(ListaPersonasEjemplo2,"Menores") == []
    assert Descartados(ListaPersonasEjemplo1,"Asexuales") == ListaDescartadosEsperada2
    assert Descartados(ListaPersonasEjemplo2,"Asexuales") == []
"""El archivo de ejemplos tiene un ejemplo por linea, y tiene que estar expresado en forma de un diccionario donde las keys son localidades y sus valores asociados
   lista de personas en cuatruplas de strings con nombre y apellido, edad, genero e interes.
   El archivo de resultados tiene un resultado por linea, y tiene que estar expresado en forma de una lista de personas en quintuplas de strings
   (NombreyApellido, Localidad, Edad, Genero, Interes)"""
def test_Matching ():
    EjemplosFile = open("MatchingEjemplos.txt","r")
    ResultadosFile = open("MatchingResultadados.txt","r")
    LineasEjemplo = EjemplosFile.readlines()
    LineasResultados = ResultadosFile.readlines()
    EjemplosFile.close()
    ResultadosFile.close()
    DiccionarioEjemplo1 = eval(LineasEjemplo[0])
    DiccionarioEjemplo2 = eval(LineasEjemplo[1])
    ListaResultado1 = eval(LineasResultados[0])
    ListaResultado2 = eval(LineasResultados[1])
    assert Matching(DiccionarioEjemplo1) == ListaResultado1
    assert Matching(DiccionarioEjemplo2) == ListaResultado2
