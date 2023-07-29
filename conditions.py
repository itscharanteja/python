on_road = 250000

credit = True
debit = True
if credit:
    down_payment = on_road*0.1
else:
    down_payment = on_road*0.2
    
print(f"Total payment is ~ {down_payment}")


if credit or debit:
    print("Paying.....")
    print("Success!!!")
else:
    print("Transaction failed")
