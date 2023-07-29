weight = int(input("Enter weight to convert: "))
unit = input("Unit : Lbs or Kgs  ")

if unit.upper() == "K" or "KGS":
    converted = weight*0.45
    print(f"Your converted weight is {converted} kgs")
elif unit.upper() == "L" or "LBS":
    converted = weight / 0.45
    print(f"Your converted weight is {converted} lbs")
else:
    print("Give correct input")
    
