from shapes.detect import Detect
from shapes.calc import Calc
import pytest
from dotenv import load_dotenv
from service import Service
import os

load_dotenv()
log = Service()

rectangle=os.getenv('RECTANGLE')
rectangle_area=int(os.getenv('RECTANGLE_AREA'))
rectangle_parimiter=int(os.getenv('RECTANGLE_PARIMITER'))

square=os.getenv('SQURE')


triangle=os.getenv('TRIANGLE')
triangle_area=int(os.getenv('TRIANGLE_AREA'))
triangle_parimiter=int(os.getenv('TRIANGLE_PARIMITER'))

shape_test=os.getenv('SHAPE_EXCEPTION')

exception_pass=os.getenv('EXCEPTION_PASS')
exception_fail=os.getenv('EXCEPTION_FAIL')

test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')


# @pytest.fixture()
# def calc():
#    return Calc(rectangle)
# @pytest.fixture()
# def calc_squre():
#    return Calc(square)

@pytest.fixture()
def calc():
    return Calc(triangle)

@pytest.fixture()
def calc_rectangle():
    return Calc(rectangle)

def test_triangle_area(calc):
   try:
       assert calc.triangle_area()==triangle_area
       log.testwriteToFile(f'triangle area {test_pass} expected {triangle_area} actual {calc.triangle_area()}')
   except:
       log.testwriteToFile(f'triangle area {test_fail} expected {triangle_area} actual {calc.triangle_area()}')


def test_triangle_perimeter(calc):
    try:
        assert calc.triangle_perimeter() ==triangle_parimiter
        log.testwriteToFile(f'triangle parimiter {test_pass} expected {triangle_parimiter} actual {calc.triangle_perimeter()}')
    except:
        log.testwriteToFile(f'triangle parimiter {test_fail} expected {triangle_parimiter} actual {calc.triangle_perimeter()} ')

def test_rectangle_area(calc_rectangle):
    try:
        assert calc_rectangle.rectangle_area() ==rectangle_area
        log.testwriteToFile(f'triangle parimiter {test_pass} expected {rectangle_area} actual {calc_rectangle.rectangle_area()}')
    except:
        log.testwriteToFile(f'triangle parimiter {test_fail} expected {rectangle_area} actual {calc_rectangle.rectangle_area()} ')


def test_rectangle_area(calc_rectangle):
    try:
        assert calc_rectangle.rectangle_perimeter() ==rectangle_parimiter
        log.testwriteToFile(f'triangle parimiter {test_pass} expected {rectangle_parimiter} actual {calc_rectangle.rectangle_perimeter()}')
    except:
        log.testwriteToFile(f'triangle parimiter {test_fail} expected {rectangle_parimiter} actual {calc_rectangle.rectangle_perimeter()} ')

def test_exception(calc):
    try:
        with pytest.raises(ValueError):
           Calc(shape_test)
        log.testwriteToFile(f'shape exeption  {exception_pass}')
    except:
         log.testwriteToFile(f'shape exeption {exception_fail}')



