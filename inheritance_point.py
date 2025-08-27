import math
class Point:
    def accept(self):
        self.x=int(input("Enter x Co-ordinate : "))
        self.y=int(input("Enter y Co-ordinate : "))

    def display(self):
        print("x co-ordinate is : ",self.x)
        print("Y co-ordinate is ",self.y)

    @staticmethod
    def calculate(p1,p2):
        d=(math.sqrt(math.pow(p2.x-p1.x,2))+(math.pow(p2.y-p1.y,2)))
        print("Distance between two points is : ",d)

print("Enter details of first point")
p1=Point()
p1.accept()
p1.display()
print("Enter details of second point")
p2=Point()
p2.accept()
p2.display()

Point.calculate(p1,p2)