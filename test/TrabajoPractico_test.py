import sys
sys.path.append("../")
import unittest
from TrabajoPractico import leer_entrada, diccionario_localidades, separar_edad, separar_genero, descartar

class TestMatching (unittest.TestCase):
    def test_leer_entrada (self):
        with open("test_entrada/test_entrada.txt") as entradaFile:
            archivos = entradaFile.readlines()
        with open("test_entrada/res_entrada.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(archivos), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(archivos)):
            path = "test_entrada/" + archivos[idx].strip()
            self.assertEqual(leer_entrada(path), eval(res[idx]))
    
    def test_diccionario_localidades (self):
        with open("test_diccionario_localidades.txt") as entradaFile:
            tests = entradaFile.readlines()
        with open("res_diccionario_localidades.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(tests), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(tests)):
            self.assertEqual(diccionario_localidades(eval(tests[idx])), eval(res[idx]))
    
    def test_separar_edad (self):
        with open("test_separar_edad.txt") as entradaFile:
            tests = entradaFile.readlines()
        with open("res_separar_edad.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(tests), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(tests)):
            self.assertEqual(separar_edad(eval(tests[idx])), eval(res[idx]))
    
    def test_separar_genero (self):
        with open("test_separar_genero.txt") as entradaFile:
            tests = entradaFile.readlines()
        with open("res_separar_genero.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(tests), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(tests)):
            self.assertEqual(separar_genero(eval(tests[idx])), eval(res[idx]))
    
    def test_descartar (self):
        with open("test_descartar.txt") as entradaFile:
            tests = entradaFile.readlines()
        with open("res_descartar.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(tests), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(tests)):
            self.assertEqual(descartar(eval(tests[idx])), eval(res[idx]))

if __name__ == '__main__':
    unittest.main()
