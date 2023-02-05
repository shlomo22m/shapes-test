from .detect import Detect
from .calc import Calc


class Complex:
    result = {}

    def __init__(self,shapes_list):
        self.complex=Calc(shapes_list)


    def shapes_calc(self,riase_on_error):
        """shlomo mhadker
            4.2.23
            function get a lists of shape and a error flag if flag is false will return dictinory of shapes and list of improper shapes if error flag is
             true and we have improper shapes it will raise an error
             """
        triangles=[]
        improper_shapes=[]
        squers=[]
        seen_shapest=[]
        rectangles=[]
        for length in self.complex.calc.sides_list:
            c=Calc(length)

            if c.calc.is_triangle() and length not in seen_shapest:
                 triangles.append({'sides': length, "area": c.triangle_area(), "perimeter": c.triangle_perimeter()})
                 seen_shapest.append(length)
                 self.result["triangles"] = triangles
            elif c.calc.is_rectangle() and length not in seen_shapest:
                rectangles.append({'sides': length, "area": c.rectangle_area(), "perimeter": c.rectangle_perimeter()})
                seen_shapest.append(length)
                self.result["rectangle"] = rectangles
            elif c.calc.is_square() and length not in seen_shapest:
                squers.append({'sides': length, "area": c.square_area(), "perimeter": c.square_perimeter()})
                seen_shapest.append(length)
                self.result["squers"] = squers
            elif length not in seen_shapest and riase_on_error==False:
                improper_shapes.append(length)
            elif riase_on_error==True:
                raise Exception("Provided shape is not a proper square,triangle or rectangle")
        return self.result,improper_shapes