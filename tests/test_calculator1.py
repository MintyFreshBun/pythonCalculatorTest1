import unittest
from calculator1 import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calc=Calculator()
        
    def test_add(self):        
        valor, numeral, textual = self.calc.add(2, 3, 'a')
        self.assertEqual(valor, 5)
        self.assertEqual(numeral, "2+3 = 5")
        self.assertEqual(textual, 'dois mais três é igual a cinco')

    def test_mul(self):
        self.assertEqual(self.calc.mul(2,3),8) ### made it wrong so we can test the error

    def test_div_zero(self):        
        self.assertRaises(ZeroDivisionError(), self.calc, 1, 0)


if __name__ == '__main__':
    unittest.main()