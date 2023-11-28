import unittest
from unittest.mock import patch
from componentes import Pizza_Component, Pizza_Personalizada_Component, Entrante_Component, Bebida_Component, Postre_Component

class TestPizzaComponent(unittest.TestCase):

    def test_decir_precio(self):
        pizza_component = Pizza_Component("Pizza Barbacoa")
        self.assertEqual(pizza_component.decir_precio(), 12.99)

    @patch('builtins.print')
    def test_tipo_de_pizza_no_reconocido(self, mock_print):
        pizza_component = Pizza_Component("Pizza No Existente")
        mock_print.assert_called_with("Tipo de pizza no reconocido")
        self.assertIsNone(pizza_component.tipo_de_pizza("Pizza No Existente"))

class TestPizzaPersonalizadaComponent(unittest.TestCase):

    def test_decir_precio(self):
        pizza_personalizada_component = Pizza_Personalizada_Component("Personalizada", "Masa", "Tomate", ["Queso"], "Horno", "Tradicional", "Vino", ["Aceitunas"])
        self.assertEqual(pizza_personalizada_component.decir_precio(), 14.99)

    @patch('builtins.print')
    def test_tipo_de_pizza_no_reconocido(self, mock_print):
        pizza_personalizada_component = Pizza_Personalizada_Component("Pizza Personalizada", "Masa", "Tomate", ["Queso"], "Horno", "Tradicional", "Vino", ["Aceitunas"])
        mock_print.assert_called_with("Tipo de pizza no reconocido")
        self.assertIsNone(pizza_personalizada_component.tipo_de_pizza("Pizza No Existente"))

class TestEntranteComponent(unittest.TestCase):

    def test_decir_precio(self):
        entrante_component = Entrante_Component("Entrante", 5.99)
        self.assertEqual(entrante_component.decir_precio(), 5.99)

class TestBebidaComponent(unittest.TestCase):

    def test_decir_precio(self):
        bebida_component = Bebida_Component("Coca-Cola", 1.99)
        self.assertEqual(bebida_component.decir_precio(), 1.99)

class TestPostreComponent(unittest.TestCase):

    def test_decir_precio(self):
        postre_component = Postre_Component("Tarta de Chocolate", 4.99)
        self.assertEqual(postre_component.decir_precio(), 4.99)

if __name__ == '__main__':
    unittest.main()
