
n = float(input("Enter Feet:"))

print("1.Convert Feet to Inches:")
print("2.Convert Feet to yards:")
print("3.Convert Feet to miles:")
print("4.Convert Feet to millimeters:")
print("5.Convert Feet to centimeters:")
print("6.Convert Feet to Meters:")
print("7.Convert Feet to kilometers:")

op = int(input("Choose an option from above:"))

if op == 1:
    Inches = n*12
    print("Feet to Inches:", Inches)
elif op == 2:
    Yards = n*0.33333
    print("Feet to Yards:", Yards)
elif op == 3:
    Miles = n*0.00018939
    print("Feet to Miles:", Miles)
elif op == 4:
    MM = n*304.8
    print("Feet to Millimeter is:", MM)
elif op == 5:
    CM = n*30.48
    print("Feet to Centimeter:", CM)
elif op == 6:
    meter = n/3.2808
    print("Feet to Meter:", meter)
elif op == 7:
    KM = n/3208.8
    print("Feet ti Kilometer:", KM)
else:
    print("Wrong Choice Choosen")
