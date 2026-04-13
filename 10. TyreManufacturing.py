t=int(input("Enter no. of Test Cases: "))
for i in range(t):
   n=int(input("Enter no.of manafactured tyres: "))
   if n%4==0:
      print("NO")
   elif n%4==2:
      print("YES")
   else:
      print("")
