sal=int(input("Enter Salary : "));
if sal<= 250000:
   print("No Tax ");
   print("Your Salary : ",sal)
elif sal>250000  and sal<500000:
   print("5% Tax");
   print("Your Salary : ",sal-(sal*0.05));
elif sal>=500000 and sal<1000000:
   print("10% Tax");
   print("Your Salary : ",sal-(sal*0.10));
elif sal>=1000000:
   print("15% Tax");
   print("Your Salary : ",sal-(sal*0.15));
else:
   print("Invalid Salary ");
