class Detect():

    def __init__(self,sides_list):
        if type(sides_list)==str:
            self.sides_list=sides_list
            self.shapes_list()
        else:
            self.sides_list=sides_list




    def shapes_list(self):
        try:
            self.sides_list = list(map(int, self.sides_list.split(',')))
        except ValueError:
            raise ValueError


    def is_rectangle(self):
        """shlomo mhadker
            Date:4.2.23
            this functiom check if the list of side are a rectangle return true if yes and False if not
        """

        if len(self.sides_list)!=4:
            return False

        for length in self.sides_list:
            if length<0 or self.sides_list.count(length) != 2:
                return False
        return True



    def is_square(self):
        """shlomo mhadker
            Date:4.2.23
            this functiom check if the list of side are a square return true if yes and False if not
        """
        if len(self.sides_list)!=4:
            return False

        for length in self.sides_list:
            if length>0 and len(set(self.sides_list)) == 1:
                return True
            else:
                return False

    def is_triangle(self):
        """shlomo mhadker
           Date:4.2.23
           this functiom check if the list of side are a _triangle return true if yes and False if not
        """
        self.sides_list.sort()
        if len(self.sides_list) == 3 and self.sides_list[0] + self.sides_list[1] > self.sides_list[2]:
            return True
        else:
            return False