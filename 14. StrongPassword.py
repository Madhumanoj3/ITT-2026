p=input("Enter Password: ")
if' 'in p:
   print("The password shoud not contain any space")
if not any(chr.isdigit() for chr in p):
   print("The password shoud  contain atleast one digit")
if not any(chr.islower() for chr in p):
   print("The password shoud  contain atleast one lowercase")
if not any(chr.isupper() for chr in p):
   print("The password shoud  contain atleast one uppercase")
if not 8 <= len(p) <= 15:
   print("The password shoud  be in specific size")
if not any(chr in "@*!~:#" for chr in p):
   print("The password shoud  contain atleast one special character")
else:
   print("the password is valid:",p)

