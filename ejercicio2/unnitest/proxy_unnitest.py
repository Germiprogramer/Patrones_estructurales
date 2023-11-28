import sys
sys.path.append(r"C:\Users\Germán Llorente\Desktop\germiprogramer\Patrones_estructurales\ejercicio2.proxy\py")
import unittest
from unittest.mock import patch
from datetime import datetime
from proxy import Proxy

class TestProxy(unittest.TestCase):

    @patch('builtins.input', side_effect=['usuario_existente', 'contrasenia_correcta'])
    def test_acceso_exitoso(self, mock_input):
        carpeta_mock = Carpeta()  # Asegúrate de tener una clase Carpeta definida
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, True)

    @patch('builtins.input', side_effect=['usuario_existente', 'contrasenia_incorrecta', 'usuario_existente', 'contrasenia_correcta'])
    def test_acceso_fallido_y_luego_exitoso(self, mock_input):
        carpeta_mock = Carpeta()
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, True)

    @patch('builtins.input', side_effect=['usuario_no_existente', 'usuario_existente', 'contrasenia_correcta'])
    def test_usuario_no_encontrado_y_luego_acceso_exitoso(self, mock_input):
        carpeta_mock = Carpeta()
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, True)

    @patch('builtins.input', side_effect=['usuario_existente', 'contrasenia_correcta', 'crear documento', 'documento1', '10.0', 'pdf'])
    def test_crear_documento(self, mock_input):
        carpeta_mock = Carpeta()
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, True)

    @patch('builtins.input', side_effect=['usuario_existente', 'contrasenia_correcta', 'operacion_invalida'])
    def test_operacion_invalida(self, mock_input):
        carpeta_mock = Carpeta()
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, False)

    @patch('builtins.input', side_effect=['usuario_existente', 'contrasenia_correcta', 'acceder', 'carpeta1'])
    def test_acceder_a_carpeta(self, mock_input):
        carpeta_mock = Carpeta()
        proxy = Proxy(carpeta_mock)
        self.assertEqual(proxy.operacion_realizada, True)

if __name__ == '__main__':
    unittest.main()
