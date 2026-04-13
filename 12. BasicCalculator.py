a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
print("MENU\n1.Add\n2.Sub\n3.Mul\n4.Div")
choice=int(input("Enter choice:"))
match choice:
   case 1:
      print("Sum: ",a+b)
   case 2:
      print("Diff: ",a-b)
   case 3:
      print("Mul: ",a*b)
   case 4:
      print("Div: ",a/b)
   case _:
      print("Invalid Choice")
