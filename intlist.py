test_list1=[1,2,1,3,5]
test_list2=[1,2,4,3,5]
print("The first list is:"+str(test_list1))
print("The second list is:"+str(test_list2))
test_list1.sort()
test_list2.sort()
if len(test_list1)==len(test_list2):
   print("The lists are have same length")
else:
   print("The lists are not have same length")
def common_data(list1,list2):
    result=0
    for x in list1:
     for y in list2:
       if x==y:
         result=result+x
    return result
print('sum is:',common_data(test_list1,test_list2))
x=int(input("Enter number to be searched:"))
if x in test_list1:
    print("The first list contains the value")
elif x in test_list2:
    print("The second list contains the value")
else:
    print("The lists has no such vale")
