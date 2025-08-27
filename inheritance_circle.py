import math
class Circle:
    # def __init__(self,r):
    #     self.__radius=r
    
    def accept(self):
        self.__radius=float(input("Enter radius of circle : "))

    def calculate(self):
        self.__area=math.pi*self.__radius*self.__radius
        print("Area of circle is : ",self.__area)
        self.__perimeter=(2*math.pi*self.__radius)
        print("Perimeter of radius is : ",self.__perimeter)

c=Circle()
c.accept()
c.calculate()