from shapes.detect import Detect
from shapes.calc import Calc
from shapes.complex import Complex
import pytest
from dotenv import load_dotenv
from service import Service
import json
import os
import ast
load_dotenv()
log = Service()
shape_list=json.loads(os.getenv("TEST_LIST"))
result_complex=os.getenv('RESULT_COMPLEX')
riase_on_error=True
complex_list=json.loads(os.getenv("RESULT_LIST"))
exception_pass=os.getenv('EXCEPTION_PASS')
exception_fail=os.getenv('EXCEPTION_FAIL')
test_pass=os.getenv('TEST_PASS')
test_fail=os.getenv('TEST_FAIL')


@pytest.fixture()
def complex():
    return Complex(shape_list)

@pytest.mark.test_shapes_calc
def test_shapes_calc(complex):
    riase_on_error = False
    dict,list=complex.shapes_calc(riase_on_error)
    dict2 = ast.literal_eval(result_complex)

    try:
        assert dict.items() == dict2.items() and list==complex_list
        log.testwriteToFile(f'shape calc: {test_pass} expected\n {dict2} actual\n {dict}\n improper shapes expected{complex_list}actual {list} ')
    except:
        log.testwriteToFile(f'shape calc: {test_fail} expected\n {dict2} actual\n {dict}\n improper shapes expected{complex_list}actual {list}  ')

@pytest.mark.test_Exception
def test_Exception(complex):
    try:
        with pytest.raises(Exception):
            complex.shapes_calc(riase_on_error)
        log.testwriteToFile(f'shape dict calc when riase on error is True  {exception_pass}')
    except:
        log.testwriteToFile(f'shape dict calc when riase on error is True {exception_fail}')