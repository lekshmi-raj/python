list1=[]
count=0
n=int(input("Enter a limit:"))
i=0
while i<n:
      i=i+1
      inp=input("Enter a name:")
      list1.append(inp)
print("List is",list1)
for name in list1:
    if'a' in name:
       count=count+name.count('a')
print("The total number of'a' in the list is:",count)
