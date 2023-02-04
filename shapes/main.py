from detect import Detect
from  calc import Calc
from complex import Complex




if __name__ == '__main__':
    ls = [4,2,5]
    shape_list=[[2, 2, 2, 2], [3, 4, 5], [5, 6, 6], [2, 3, 2, 3], [2, 3, 8], [3, 4, 5],[2,3,9],[2, 2, 1, 2]]
    #shape_list = [ [3, 4, 5], [5, 6, 6], [3, 4, 6]]
    riase_on_error=False
    #d=Detect(ls)
    #print(d.sides_list)
    #print(d.is_rectangle())
    #print(d.is_square())
    #print(d.is_triangle())
    #c=Calc(ls)
    #try:
     #   print(c.rectangle_perimeter())
     #   print(c.rectangle_area())
     #   print(c.triangle_perimeter())
     #   print(c.triangle_area())
   # except Exception as e:
      #  print(e)
    x=Complex(shape_list)
    #print(x.complex.calc.sides_list)
    try:
        print(x.shapes_calc(riase_on_error))
    except Exception as  e:
        print(e)

