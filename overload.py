class rectangle:
    area=0
    def __init__(self,a,b):
       self.a=a
       self.b=b
    def calc_area(self):
       self.area=self.a*self.b
       print("Area is:",self.area)
    def __lt__(self,second):
      if self.area<second.area:
       return True
      else:
       return False
length1=int(input("Enter length of rectangle1:"))
width1=int(input("Enter width of rectangle1:"))
length2=int(input("Enter length of rectangle2:"))
width2=int(input("Enter width of rectangle2:"))
obj1=rectangle(length1,width1)
obj2=rectangle(length2,width2)
obj1.calc_area()
obj2.calc_area()
if(obj1<obj2):
  print("Rectangle two is large")
elif(obj1==obj2):
  print("Rectangles are same")
else:
  print("Rectangle one is large")
