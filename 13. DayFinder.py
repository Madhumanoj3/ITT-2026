from datetime import datetime
date=input()
try:
   day=datetime.strptime(date, "%d %m %Y")
   print(f"{day.strftime('%A')}")
   print(capitalize(day.strftie('%A')))
except ValueError:
   print("Value Error")
