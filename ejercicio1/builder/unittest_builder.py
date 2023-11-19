import unittest
from Director import Director
from Pizza_CuatroQuesos import ConstructorPizzaCuatroQuesos
from Pizza_Barbacoa import ConstructorPizzaBarbacoa
from Pizza_Hawaiana import ConstructorPizzaHawaiana
from Pizza_Margherita import ConstructorPizzaMargherita
from Pizza_Personalizada import ConstructorPizzaPersonalizada

class TestPizzaBuilder(unittest.TestCase):

    def test_build_cuatro_quesos_pizza(self):
        director = Director()
        builder = ConstructorPizzaCuatroQuesos()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Pizza Cuatro Quesos")
        # Add more assertions for other attributes if needed

    def test_build_barbacoa_pizza(self):
        director = Director()
        builder = ConstructorPizzaBarbacoa()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Pizza Barbacoa")
        # Add more assertions for other attributes if needed

    def test_build_hawaiana_pizza(self):
        director = Director()
        builder = ConstructorPizzaHawaiana()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Hawaiana")
        # Add more assertions for other attributes if needed

    def test_build_margherita_pizza(self):
        director = Director()
        builder = ConstructorPizzaMargherita()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Margherita")
        # Add more assertions for other attributes if needed

    def test_build_personalizada_pizza(self):
        director = Director()
        builder = ConstructorPizzaPersonalizada()
        director.builder = builder

        director.build()
        product = builder.product

        self.assertEqual(product.nombre, "Personalizada")
        # Add more assertions for other attributes if needed

if __name__ == '__main__':
    unittest.main()
