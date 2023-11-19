import unittest
from Director import Director
from Pizza_CuatroQuesos import ConstructorPizzaCuatroQuesos, PizzaCuatroQuesos
from Pizza_Barbacoa import ConstructorPizzaBarbacoa, PizzaBarbacoa
from Pizza_Hawaiana import ConstructorPizzaHawaiana, PizzaHawaiana
from Pizza_Margherita import ConstructorPizzaMargherita, PizzaMargherita
from Pizza_Personalizada import ConstructorPizzaPersonalizada, PizzaPersonalizada

class TestPizzaBuilder(unittest.TestCase):

    def test_build_cuatro_quesos_pizza(self):
        director = Director()
        builder = ConstructorPizzaCuatroQuesos()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.parts["Nombre"], "Pizza Cuatro Quesos")
        # Add more assertions for other attributes if needed

    def test_build_barbacoa_pizza(self):
        director = Director()
        builder = ConstructorPizzaBarbacoa()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.parts["Nombre"], "Pizza Barbacoa")
        # Add more assertions for other attributes if needed

    def test_build_hawaiana_pizza(self):
        director = Director()
        builder = ConstructorPizzaHawaiana()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.parts["Nombre"], "Pizza Hawaiana")
        # Add more assertions for other attributes if needed

    def test_build_margherita_pizza(self):
        director = Director()
        builder = ConstructorPizzaMargherita()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.parts["Nombre"], "Pizza Margherita")
        # Add more assertions for other attributes if needed
'''
    def test_build_personalizada_pizza(self):
        director = Director()
        builder = ConstructorPizzaPersonalizada()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Personalizada")
        # Add more assertions for other attributes if needed
'''
if __name__ == '__main__':
    unittest.main()
