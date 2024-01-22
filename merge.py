def Merge(dict1,dict2):
    for i in dict2.keys():
        dict1[i]=dict2[i]
    return dict1
dict1={'x':10,'y':8}
dict2={'a':6,'b':4}
dict3=Merge(dict1,dict2)
print(dict3)
   
