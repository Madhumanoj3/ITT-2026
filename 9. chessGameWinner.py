t=int(input())
for i in range(t):
   c=n=0
   x=int(input())
   result=input()
   if len(result)!=14:
       print("INVALID")
       exit(0)
   for j in result:
      if j=="C":
         c=c+2
      elif j=="N":
         n=n+2
      elif j=="D":
         c=c+1
         n=n+1
      else:
         print("INVALID")
         exit(0)
   if c>n:
        print(60*x)
   elif c<n:
       print(40*x)
   else:
       print(55*x)

