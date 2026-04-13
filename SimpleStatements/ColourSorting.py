print("Colours: 1. Red 2. Blue 3. Green")
n = eval(input("Enter colurs in numbers "))
n.sort()
for i in n:
   if i == 0:
      print("Red ",end=" ")
   elif i == 1:
      print("Blue ",end=" ")
   elif i == 2:
      print("Green ",end=" ")
   else:
      print("Invalid ",end=" ")
