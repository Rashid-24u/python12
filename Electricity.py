unit=int(input("Enter the unit:"))
amount=0
if unit<=100:
        amount=unit* 5
elif unit<=200:
        amount=(100 * 5) + ((unit - 100) * 8)
else:
    amount=(100 * 5) + (100 * 8) + ((unit - 200) * 10)     

print("Electricity bill : ",amount)     
