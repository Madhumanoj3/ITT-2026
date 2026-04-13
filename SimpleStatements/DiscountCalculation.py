bill=int(input("Enter Bill Amount: "))
amt=bill
if bill>=3000:
   dis=bill*0.10
   print("10% discount : ",dis);
   print("Total Bill : ",amt-dis);
elif bill>=5000:
   dis=bill*0.20
   print("20% Discount : ",dis)
   print("Total Bill : ",amt-dis);
elif bill<0:
   print("Invalid Amount ");
else:
   print("No Discount.");
   print("Total Bill : ",amt)
