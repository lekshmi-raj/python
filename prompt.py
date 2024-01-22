list1=[]
n=int(input("Enter a limit:"))
i=0
while i<n:
     i=i+1
     inp=int(input("Enter an integer:"))
     if(inp<100):
       list1.append(inp)
     else:
       list1.append("over")
print("List is",list1)
