a=int(input("Enter a Number: "))
n=a
rev=0
while (n!=0):
   temp=n%10
   rev=rev*10+temp
   n=n//10
print("Reverse of Number: ",rev)
