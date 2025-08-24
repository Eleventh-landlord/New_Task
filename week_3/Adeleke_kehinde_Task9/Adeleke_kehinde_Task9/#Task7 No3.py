#Task7 no 3
dic = {}
days = ("Monday","Tuesday","Wednesday","Thursday","friday","Saturday","Sunday")
no = 3
for i in range (no):
  day_acts = input("Enter day: ").title()
if day_acts in days:
  activity = input({day_acts[0]}: ,{day_acts[1]})
else:
  print("Enter a correct date")
  for day, dic in dic.days:
   print(f"{day_acts}{dic}")