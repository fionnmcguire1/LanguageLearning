'''
Pytest is an industry standard testing library.
Unittest is pythons simple builtin testing framework

With unittest you have to be much more explicit in your comparissons
eg. assertEqual
assertFalse
assertTrue

With Pytest you only have to remember assert as it has been overloaded with diagnostic response

'''
import sys
import pytest
from test_code import Calculator,CalculatorError

ENV = "PROD"

def test_calculator():
    calculator =  Calculator()
    result = calculator.add(2,3)
    assert 5 == result

def test_calculator_subtract():
    calculator =  Calculator()
    result = calculator.subtract(2,3)
    assert -1 == result

def test_calculator_add_string():
    calculator =  Calculator()
    with pytest.raises(CalculatorError) as context:
        result = calculator.add(2,"3")

#Testing approx functionality
#Test if the result is equal to another within a certain range, abs = range + or -
def test_approx():
    assert 0.1+0.2 == pytest.approx(0.4,abs=0.1)

#Skip tests based on version requirements of the system
@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python3.9 or higher")
def test_skip_test():
    assert 0.1+0.2 == pytest.approx(0.4,abs=0.1)

@pytest.mark.skipif(sys.version_info < (2, 7), reason="requires python3 or higher")
def test_skip_test_pass():
    assert 0.1+0.2 == pytest.approx(0.4,abs=0.1)

@pytest.mark.skipif(ENV != "TEST", reason="This test is not performed on Prod")
def test_skip_test_not_prod():
    assert 0.1+0.2 == pytest.approx(0.4,abs=0.1)

def test_skip_test_if_statement():
    if ENV != "TEST":
        pytest.skip("This test only runs on TEST system")
    assert 0.1+0.2 == pytest.approx(0.4,abs=0.1)
