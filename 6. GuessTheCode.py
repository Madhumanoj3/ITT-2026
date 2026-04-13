code=eval(input("Enter Code: "))
guess=eval(input("Guess the code: "))
hit=nearhit=0
def nearhit(code,guess):
   c=0
   for i in range(len(code)):
      if guess[i] in code:
         if guess[i]!=code[i]:
            c=c+1
      else:
         continue
   return c
for i in range(len(code)):
   if code[i]==guess[i]:
      hit=hit+1
   else:
      continue
nearhit=nearhit(code,guess)
print(hit,"H",nearhit,"N")
