class parallelogram:
    def __init__(self,height,base):
        self.height = height 
        self.base = base 

    def area(self):
        area = self.height*self.base
        print(area)

rhombus = parallelogram(18,9)

rhombus.area()

class triangles:
    def __init__(self,height,base):
        self.height = height
        self.base = base

    def area(self):
        area = self.base*self.height*1/2
        print(area)

triangleabc = triangles(4,3)
triangleabc.area() 