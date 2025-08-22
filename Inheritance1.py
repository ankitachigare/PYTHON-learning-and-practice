class Student:
    cnt=0
    def __init__(self,r,n,m):
        self.__roll=r
        self.__name=n
        self.__mks=m
        Student.cnt+=1
    
    def display(self):
        print(self.__roll,'\t',self.__name,'\t',self.__mks)

    @staticmethod
    def show():
        print('Number of students : ',Student.cnt)

    def __del__(self):
        print('object destroyed.')
        Student.cnt-=1
        print('Number of students remaining : ',Student.cnt)
    
a=int(input('Enter roll : '))
b=input('Enter name:')
c=float(input('Enter mks:'))
st1=Student(a,b,c)
st1.show()

a=int(input('Enter roll : '))
b=input('Enter name:')
c=float(input('Enter mks:'))
st2=Student(a,b,c)
st2.show()

a=int(input('Enter roll : '))
b=input('Enter name:')
c=float(input('Enter mks:'))
st3=Student(a,b,c)
st3.show()

st1.display()
st2.display()
st3.display()