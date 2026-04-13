bal = 1000
a=int(input("Enter Amount: "))
if a<bal and a>0 and a%100==0 :
   print("Withdraw Successful ")
   bal=bal-a
   print("Balance :",bal)
elif a>bal:
   print("Insufficient Balance ")
elif a%100!=0:
   print("Amount must be in multiples of 100 ")
else:
   print("problem")

