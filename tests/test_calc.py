import pytest
from dotenv import load_dotenv
from shapes.calc import Calc
from shapes.detect import Detect
from service import Service
import os

load_dotenv()
log = Service()
rectangle=os.getenv('RECTANGLE')
square=os.getenv('SQURE')

triangle=os.getenv('TRIANGLE')
triangle_area=os.getenv('TRIANGLE_AREA')

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
def calc_triangle():
    return Calc(triangle)

def test_triangle_area(calc_triangle):

        assert calc_triangle.triangle_area()==6