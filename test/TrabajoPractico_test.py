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
        pass
    def test_separar_por (self):
        pass
    def test_descartar (self):
        pass

if __name__ == '__main__':
    unittest.main()
