import unittest
from area_calculations import calculate_area_cafe, calculate_area_cana

class TestAreaCalculations(unittest.TestCase):

    def test_calculate_area_cafe(self):
        # Dados fictícios para testes
        area_cafe = calculate_area_cafe(hectares=100)
        self.assertEqual(area_cafe, 10000)  # Exemplo de cálculo

    def test_calculate_area_cana(self):
        # Dados fictícios para testes
        area_cana = calculate_area_cana(hectares=150)
        self.assertEqual(area_cana, 15000)  # Exemplo de cálculo

if __name__ == '__main__':
    unittest.main()
