import unittest

def fatorial(n):
    if(n==0):
        return 1
    return n * fatorial(n-1)


def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n-2)


def pot(base, exp):
    if( exp == 0):
        return 1
    
    return base * pot(base, exp - 1)


class TestMathMethods(unittest.TestCase):
    
    
    def test_pot(self):
        self.assertEqual(1024, pot(2,10))
        
    def test_fat(self):
        self.assertEqual(24, fatorial(4))
        
        
        
unittest.main()