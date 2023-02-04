import math
#from detect import Detect
from .detect import Detect



class Calc:
    def __init__(self,side_list):
        self.calc=Detect(side_list)

    def rectangle_perimeter(self):
        if not self.calc.is_rectangle():
            raise ValueError("Provided shape is not a proper rectangle.")
        self.calc.sides_list.sort()
        return 2 * (self.calc.sides_list[0] + self.calc.sides_list[3])

    def rectangle_area(self):
        if not self.calc.is_rectangle():
            raise ValueError("Provided shape is not a proper rectangle.")
        self.calc.sides_list.sort()
        return self.calc.sides_list[0] * self.calc.sides_list[3]

    def triangle_perimeter(self):
        if not self.calc.is_triangle():
            raise Exception("Not a triangle")
        return round(sum(self.calc.sides_list),3)

    def triangle_area(self):
        if not self.calc.is_triangle():
            raise Exception("Not a triangle")
        s = self.triangle_perimeter()/2
        return int(round(math.sqrt(s * (s - self.calc.sides_list[0]) * (s - self.calc.sides_list[1]) * (s - self.calc.sides_list[2])),3))


    def square_area(self):
        if not self.calc.is_square():
            raise ValueError("Provided shape is not a proper square.")
        return self.calc.sides_list[0] * self.calc.sides_list[1]

    def square_perimeter(self):
        if not self.calc.is_square():
            raise ValueError("Provided shape is not a proper square.")
        return 4 * self.calc.sides_list[0]