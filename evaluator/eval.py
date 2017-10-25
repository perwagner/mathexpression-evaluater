'''Contains the eval function which evaluates mathematical expressions
containing +, -, *, /, (, ).

Inspired by: http://www.nerdparadise.com/programming/parsemathexpr
'''
from .Nom import Nom


def parseExpression(expr, i):
    '''Parses the entire expression and returns the value as num'''
    num, i = parseAddition(expr, i)
    return num, i


def parseAddition(expr, i):
    '''Parses additions'''
    num, i = parseMultiplication(expr, i)
    values = [num]
    while True:
        char = peek(expr, i)
        if char == "+":
            i += 1
            num, i = parseMultiplication(expr, i)
            values.append(num)
        elif char == '-':
            i += 1
            num, i = parseMultiplication(expr, i)
            num.multi(Nom(-1))
            values.append(num)
        else:
            break

    base = values[0]
    for elem in range(1, len(values)):
        base.add(values[elem])

    return base, i


def parseMultiplication(expr, i):
    '''Parses multiplications and divisions'''
    num, i = parseParenthesis(expr, i)
    values = [num]
    while True:
        char = peek(expr, i)
        if char == "*":
            i += 1
            num, i = parseParenthesis(expr, i)
            values.append(num)
        elif char == "/":
            i += 1
            num, i = parseParenthesis(expr, i)
            denominator = num
            if denominator.denominator == 0:
                raise ZeroDivisionError()

            denominator.flip()
            values.append(denominator)
            # values.append(1.0 / denominator)
        else:
            break

    base = values[0]
    for elem in range(1, len(values)):
        base.multi(values[elem])

    return base, i


def parseParenthesis(expr, i):
    '''If expr has an opening paranthesis, parse the entire expression within
    this paranthesis until a closing paranthesis is reached.

    if expr is not a opening paranthesis, then assume it is a number or
    negative, and parse the number accordingly'''
    char = peek(expr, i)
    if char == '(':
        i += 1
        value, i = parseExpression(expr, i)
        if peek(expr, i) != ')':
            raise Exception("No closing parenthesis")
        i += 1
        return value, i
    else:
        num, i = parseNegative(expr, i)
        return num, i


def parseNegative(expr, i):
    '''If expr is a number, returns that number and the new index for the
    next character to explore.
    If expr is a minus, return the negative multiplicum of the expression
    coming after the minus and the index for the next char to explore'''
    char = peek(expr, i)
    if char == '-':
        i += 1
        num, i = parseParenthesis(expr, i)
        num.multi(Nom(-1))
        return num, i
    else:
        num, i = parseNumber(expr, i)
        return num, i


def parseNumber(expr, i):
    '''Returns a Nom rep. of the str rep passed in from the given index
    also returns the new index value (next charactor to examine)

    ex.:>> parseNumber('3+5*(11-2)', 0)
        returns: Nom(3)

        >> parseNumber('3+5*(11-2)', 5)
        returns: Nom(11)
    '''
    str_value = ''

    while hasNext(expr, i):
        char = peek(expr, i)
        if char in '0123456789':
            str_value += char
        else:
            break
        i += 1

    nom = Nom(int(str_value))

    return nom, i


def peek(expr, index):
    '''returns the character in the expression given by the index'''
    a = expr[index:index + 1]
    return a


def hasNext(expr, index):
    '''Returns True if there are more characters in the expression. False
    otherwise'''
    return index < len(expr)


def eval(expr):
    ''' eval takes a mathematical expression and evaluates and returns
    its result.

    Ex. eval("1/(1/(3+4))")
    >> 7

    :param (string) The math. expression to be evaluated:
    :return: (string) The result of the evaluation
    '''
    assert type(expr) is str, "Input not string"
    assert ' ' not in expr, "Input expression contains whitespace"
    assert len(expr) > 0, "Input is empty"
    index = 0
    value, i = parseExpression(expr, index)
    # print(value.get_value())

    return value.get_value()


if __name__ == '__main__':
    pass