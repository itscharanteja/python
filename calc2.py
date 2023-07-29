def add(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}

num1 = float(input("Enter Your first num: "))
for i in operations:
    print(i)
opt = input("Pick an operation: ")
num2 = float(input("Enter Your last num: "))

calc = operations[opt]
ans = calc(num1,num2)
print(f"{num1} {opt} {num2} = {ans}")


should = True
while should:
    yn = input("Want to calculate with another number? Y/N").lower()
    if yn == "n":
        break
    
    opt = input("Pick an operation: ")
    num3 = float(input("Enter Your last num: "))
    calc = operations[opt]
    answ = calc(ans,num3)
    print(f"{num3} {opt} {ans} = {answ}")
    