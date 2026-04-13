def factor(n):
   for i in range(2,n+1):
      if n%i==0:
         print(prime(i))
      else:
         pass
def prime(n1):
   c=1
   for i in range(2,n1):
      if n1%i!=0:
         c=1
      else:
         c=0
         break
   if c==1:
      return n1
   else:
      d=' '
      return d
      pass
n=int(input("enter a number:"))
print("THE PRIME FACTOR OF GIVEN NUMBER %d IS"%n)
factor(n)
