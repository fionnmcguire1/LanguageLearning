class CalculatorError(Exception):
    """An exception class for calculator"""



class Calculator(object):
    '''This is a test object used for pytest exploration'''
    def add(self,a,b):
        try:
            return a+b
        except TypeError:
            raise CalculatorError()
        except ValueError:
            raise CalculatorError


    def subtract(self,a,b):
        return a-b
