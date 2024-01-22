a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
i=1
while(i<=a and i<=b):
   if(a%i==0 and b%i==0):
      gcd=i
   i=i+1
print("GCD of numbers is:",gcd)
