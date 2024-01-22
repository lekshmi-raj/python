from math import pi
while True:
       print()
       print("1.Area of circle")
       print("2.Area of rectangle")
       print("3.Circumference of circle")
       print("4.Area of square")
       ch=int(input("Enter your choice 1,2,3,4(enter 0 to exit):"))
       if ch==1:
         r=float(input("Enter the radius of the circle:"))
         print("The area of the circle is:",str(pi*r**2))
       elif ch==2:
         l=int(input("Enter the length of the rectangle:"))
         b=int(input("Enter the breadth of the rectangle:"))
         print("The area of the rectangle is:",str(l*b))
       elif ch==3:
         r=float(input("Enter the radius of the circle:"))
         print("circumference of circle is:",str(2*pi*r))
       elif ch==4:
         a=int(input("Enter the length of a side of square:"))
         print("Area of square is:",str(a*a))
       elif ch==0:
         break
       else:
         print("Invalid choice")
