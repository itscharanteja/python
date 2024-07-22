def reverse( x):
        temp = x
        num = ""
        while temp>0:
            digit = str(temp % 10)
            num += digit

            temp //= 10
        return int(num)

print(reverse(123))