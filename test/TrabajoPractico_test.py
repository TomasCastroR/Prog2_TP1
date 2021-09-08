import sys
sys.path.append("../")
import unittest
from TrabajoPractico import leer_entrada, diccionario_localidades, separar_por, descartar

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
    def test_separar_por (self):
        with open("test_separar.txt") as entradaFile:
            tests = entradaFile.readlines()
        with open("res_separar.txt") as resFile:
            res = resFile.readlines()
        self.assertEqual(len(tests), len(res), "Cantidad de ejemplos y resultados no coincide")
        for idx in range(len(tests)):
            if idx % 2 == 0:
                self.assertEqual(separar_por(eval(tests[idx]), "Edad"), eval(res[idx]))
            else:
                self.assertEqual(separar_por(eval(tests[idx]), "Genero"), eval(res[idx]))
    def test_descartar (self):
        pass

if __name__ == '__main__':
    unittest.main()
