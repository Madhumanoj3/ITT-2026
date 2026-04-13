s1=input("enter your string:")
s3=''
for i in s1:
   if i not in s3:
      s3+=i
m=map(lambda a:a.upper() if a.islower() else a.lower(),s3)
s2=''.join(m)
print(s2)
