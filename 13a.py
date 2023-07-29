def is_even_num(l):
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum
num = list(int(input("Enter numbers: ").split()))
lst = []
for i in range(0,num):
    ele = int(input())
    ele.append(lst)
    
print(is_even_num(lst))