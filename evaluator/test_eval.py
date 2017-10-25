import unittest
from .eval import *


class TestEval(unittest.TestCase):
    """
    Tests the eval function
    """
    def test_peek_1(self):
        a = peek('1+2+3', 1)
        self.assertEqual(a, '+')

    def test_peek_2(self):
        a = peek('1+2+3', 2)
        self.assertEqual(a, '2')

    def test_peek_out_of_bound(self):
        a = peek('1+2+3', 22)
        self.assertEqual(a, '')

    def test_hasNext(self):
        r = hasNext('1+5-22', 4)
        self.assertTrue(r)

    def test_hasNext_no_more_characters(self):
        r = hasNext('1+5-22', 6)
        self.assertFalse(r)

    def test_parseNumber(self):
        r, i = parseNumber('12', 0)
        self.assertEqual(r.nominator, 12)
        self.assertEqual(r.denominator, 1)
        self.assertEqual(i, 2)

    def test_parseNumber_2_longer_expression(self):
        r, i = parseNumber('12+84/25', 3)
        self.assertEqual(r.nominator, 84)
        self.assertEqual(r.denominator, 1)
        self.assertEqual(i, 5)

    def test_parseNumber_3_long_exression(self):
        r, i = parseNumber('12+84/25', 6)
        self.assertEqual(r.nominator, 25)
        self.assertEqual(i, 8)

    def test_parseNegative_1_positive_number(self):
        r, i = parseNegative('12+55/44', 3)
        self.assertEqual(r.nominator, 55)

    def test_parseNegative_2_negative_number(self):
        r, i = parseNegative('12-55/44', 2)
        self.assertEqual(r.nominator, -55)

    def test_parseParanthesis(self):
        num, i = parseParenthesis('8+(10+12)', 2)
        self.assertEqual(num.nominator, 22)

    def test_parseParanthesis_2(self):
        num, i = parseParenthesis('(10+12)', 0)
        self.assertEqual(num.nominator, 22)

    def test_parseMultiplication(self):
        num, i = parseMultiplication('10*5', 0)
        self.assertEqual(num.nominator, 50)

    def test_parseDivision(self):
        num, i = parseMultiplication('10/5*2', 0)
        self.assertEqual(num.get_value(), '4')

    def test_parseAddition(self):
        num, i = parseAddition('10+5', 0)
        self.assertEqual(num.nominator, 15)

    def test_parseAddition_subtraction(self):
        num, i = parseAddition('10-5', 0)
        self.assertEqual(num.nominator, 5)

    def test_parseAddition_subtraction_2(self):
        num, i = parseAddition('10-5-88', 0)
        self.assertEqual(num.nominator, -83)

    def test_parseExpression_simple(self):
        num, i = parseExpression('1+2', 0)
        self.assertEqual(num.nominator, 3)

    def test_parseExpression_simple_2(self):
        num, i = parseExpression('1+2+8', 0)
        self.assertEqual(num.nominator, 11)

    def test_parseExpression_simple_3(self):
        num, i = parseExpression('1+2*8', 0)
        self.assertEqual(num.nominator, 17)

    def test_parseExpression_0(self):
        num, i = parseExpression('1+(8/2)-1', 0)
        self.assertEqual(num.get_value(), '4')

    def test_parseExpression_1(self):
        num, i = parseExpression('1+2*(8/2)-1', 0)
        self.assertEqual(num.nominator, 16)
        self.assertEqual(num.denominator, 2)
        self.assertEqual(num.get_value(), '8')

    def test_parseExpression_2(self):
        num, i = parseExpression('1*2*3*4/24', 0)
        self.assertEqual(num.get_value(), '1')

    def test_1_plus_2(self):
        r = eval('1+2')
        self.assertEqual(r, '3')

    def test_1_plus_2_with_parantes(self):
        r = eval('(1+2)')
        self.assertEqual(r, '3')

    def test_1_div_2(self):
        r = eval('1/2')
        self.assertEqual(r, '1/2')

    def test_1_div_3(self):
        r = eval('1/3')
        self.assertEqual(r, '1/3')

    def test_1_multiply_5(self):
        r = eval('1*5')
        self.assertEqual(r, '5')

    def test_eval_official_1(self):
        r = eval("1/(1/(3+4))")
        self.assertEqual(r, '7')

    def test_eval_official_2(self):
        r = eval("9999999999/10000000000")
        self.assertEqual(r, '9999999999/10000000000')

    def test_eval_official_3(self):
        r = eval("1/7+1/7+1/7+1/7+1/7+1/7+1/7")
        self.assertEqual(r, '1')

    def test_eval_input_validation_1_isNumber(self):
        with self.assertRaises(AssertionError) as context:
            eval(25)

        self.assertTrue('Input not string' in str(context.exception))

    def test_eval_input_validation_2_contains_whitespace(self):
        with self.assertRaises(AssertionError) as context:
            eval('2 + 3')

        self.assertTrue('Input expression contains whitespace' in str(context.exception))

    def test_eval_input_validation_3_empty_string_input(self):
        with self.assertRaises(AssertionError) as context:
            eval("")

        self.assertTrue('Input is empty' in str(context.exception))

    def test_eval_complexExpression_1(self):
        r = eval("(1/6)*3/1+10-4*5-(8/4+32)")
        self.assertEqual(r, '-1044/24')

    def test_eval_divByZero(self):
        with self.assertRaises(ZeroDivisionError) as context:
            eval("1/0")
