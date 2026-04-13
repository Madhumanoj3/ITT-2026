a=int(input("Enter Number: "))
even=0
for i in range (1,a+1,1):
   if i%2==0:
      even+=1
print("Count of Even Numbers 0 to ",a,": ",even)
