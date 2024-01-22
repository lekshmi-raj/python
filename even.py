def remove_even(x):
    for i in x[:]:
      if(i%2)==0:
        x.remove(i)
    return x
a=[12,15,7,9,14,16,18,19,21,24,28,26]
print(remove_even(a))
