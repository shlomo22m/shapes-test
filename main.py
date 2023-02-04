#from .shapes.detect import Detect
# from  shapes.calc import Calc
from shapes.detect import Detect
#from complex import Complex
from shapes.calc import Calc
import json
from shapes.complex import Complex
from dotenv import load_dotenv
import os



if __name__ == '__main__':
    load_dotenv()
    #ls = '[[4,2,5],[5,6,8]]'
    shape_list=json.loads(os.getenv("TRIANGLE"))
    #shape_list=os.getenv('RECTANGLE')
    #print(shape_list)
    #shape_list = list(map(int, shape_list.split(',')))
    riase_on_error=False
    #print(len(ls))

    #d=Detect(shape_list)
    #print(d.sides_list)
    #print(d.is_rectangle())
    #print(d.is_square())
    #print(d.is_triangle())
   # c=Calc(shape_list)
    #try:
    #    print(c.rectangle_perimeter())
       # print(c.rectangle_area())
     #   print(c.triangle_perimeter())
      # print(c.triangle_area())
   # except Exception as e:
   #    print(e)
    x=Complex(shape_list)
    #print(x.complex.calc.sides_list)
    try:
        print(x.shapes_calc(riase_on_error))
    except Exception as  e:
        print(e)
