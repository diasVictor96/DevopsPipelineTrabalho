import unittest  
from unittest.mock import patch  
from io import StringIO  
import Calculadora  
  
class TestCalculator(unittest.TestCase):  
    def test_addition(self):  
        with patch('builtins.input', side_effect=['2', '3', '+']):  
            expected_output = "O resultado é: 5.0\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
    def test_subtraction(self):  
        with patch('builtins.input', side_effect=['5', '2', '-']):  
            expected_output = "O resultado é: 3.0\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
    def test_multiplication(self):  
        with patch('builtins.input', side_effect=['4', '2', '*']):  
            expected_output = "O resultado é: 8.0\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
    def test_division(self):  
        with patch('builtins.input', side_effect=['6', '3', '/']):  
            expected_output = "O resultado é: 2.0\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
    def test_invalid_operation(self):  
        with patch('builtins.input', side_effect=['2', '3', '%']):  
            expected_output = "Operação inválida\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
    def test_invalid_input(self):  
        with patch('builtins.input', side_effect=['a', '3', '+']):  
            expected_output = "Entrada inválida. Certifique-se de digitar números válidos.\n"  
            with patch('sys.stdout', new=StringIO()) as fake_out:  
                Calculadora.main()  
                self.assertEqual(fake_out.getvalue(), expected_output)  
  
if __name__ == '__main__':  
    unittest.main()  
