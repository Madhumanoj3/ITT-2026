t=int(input("No.of Test Cases: "))
for i in range(t):
   n=int(input("Enter no.of Rows: "))
   tri=[];
   for i in range(n):
      l=[]
      for j in range(i+1):
         a=int(input("Enter : "))
         l.append(a)
      tri.append(l)
   for i in tri:
      for j in i:
         print(j,end="")
      print()
   sumspaths=[]
