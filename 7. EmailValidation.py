class invalidexception(Exception):
   pass
t=int(input())
for i in range(t):
   try:
      email=input()
      if " " in email:
         raise invalidexception()
      if "@" not in email or email.count("@")!=1:
         raise invalidexception()
      if "#$%^&*!><;\|{}][" in email:
         raise invalidexception()
      if email.startswith("@") or email.endswith("."):
         raise invalidexception()
      if email.count(".")<1:
         raise invalidexception()
      if email.index("@")>email.index("."):
         raise invalidexception()
      else:
         print("VALID")
   except invalidexception:
      print("INVALID")
