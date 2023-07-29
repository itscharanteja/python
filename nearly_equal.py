def nearly_equal(a, b):
    if len(a) != len(b):
        return False
    diffs = 0
    for c1, c2 in zip(a, b):
        if c1 != c2:
            diffs += 1
            if diffs > 1:
                return False
    return diffs == 1
a = input("Enter first str: ")
b = input("Enter second str: ")
if nearly_equal(a, b):
    print(f"{a} and {b} are nearly equal")
else:
    print(f"{a} and {b} are not nearly equal")
