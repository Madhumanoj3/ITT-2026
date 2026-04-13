def fifo(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fifo(n-1)+fifo(n-2)
n=int(input("enter your number:"))
for i in range(n):
   c=fifo(i)
   print(c,end=" ")
print()
