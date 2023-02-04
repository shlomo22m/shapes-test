import pytest
from shapes.detect import Detect
from dotenv import load_dotenv
from service import Service
import os

load_dotenv()
log = Service()
rectangle=os.getenv('RECTANGLE')
square=os.getenv('SQURE')
triangle=os.getenv('TRIANGLE')

shape_test=os.getenv('SHAPE_EXCEPTION')

exception_pass=os.getenv('EXCEPTION_PASS')
exception_fail=os.getenv('EXCEPTION_FAIL')
test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')


@pytest.fixture()
def detect():
   return Detect(rectangle)
@pytest.fixture()
def detect_squre():
   return Detect(square)

@pytest.fixture()
def detect_triangle():
   return Detect(triangle)


def test_shapes(detect):
    try:
        with pytest.raises(ValueError):
             Detect(shape_test)
        log.testwriteToFile(exception_pass)
    except:
        log.testwriteToFile(exception_fail)

def test_is_rectangle(detect):
    try:
        assert detect.is_rectangle()==True
        log.testwriteToFile(f'is rectangle {test_pass} expected True result:True')
    except:
        log.testwriteToFile(f'is rectangle {test_fail} expected True result:False')




def test_is_square(detect_squre):
    try:
        assert detect_squre.is_square() == True
        log.testwriteToFile(f'is square {test_pass} expected True result:True')
    except:
        log.testwriteToFile(f'is square {test_fail} expected True result:False')


def test_is_triangle(detect_triangle):
    try:
        assert detect_triangle.is_triangle() == True
        log.testwriteToFile(f'is triagle {test_pass} expected True result:True')
    except:
        log.testwriteToFile(f'is triagle {test_fail} expected True result:False')