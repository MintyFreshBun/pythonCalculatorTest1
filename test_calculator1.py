import unittest
from calculator1 import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calc=Calculator()
        
    def test_add(self):        
        res=self.calc.add(2,3)
        self.assertEqual(res,5)
    
    def test_add_neg1(self):        
        self.assertEqual(self.calc.add(4,7),-3)
    
    def test_add_null(self):        
        self.assertEqual(self.calc.add(3,0),3)
    
    def test_mul(self):
        self.assertEqual(self.calc.mul(2,3),8) ### made it wrong so we can test the error

    def test_div_zero(self):        
        self.assertRaises(ZeroDivisionError(),self.calc,1,0)  


if __name__ == '__main__':
    unittest.main()