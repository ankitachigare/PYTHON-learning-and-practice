class Rectangle:
    def setLength(self,l):
        self.__length=l

    def setWidth(self,w):
        self.__width=w

    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def calculate(self):
        self.__a=self.__length*self.__width
        self.__p=2*(self.__length+self.__width)

    def display(self):
        print("Area of rectangle is : ",self.__a)
        print("Perimeter if rectangle : ",self.__p)

    def isSquare(self):
        if self.__length==self.__width:
            return True
        else:
            return False

r=Rectangle()
a=float(input("Enter length of rectangle : "))
b=float(input("Enter breadth of rectangle : "))
r.setLength(a)
r.setWidth(b)
ans=r.isSquare()
if(ans):
    print("IT is square.")
else:
    print("It is not square.")

r.calculate()
r.display()