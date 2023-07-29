#Write your code below this line 👇
import math
def paint_calc(height,width,cover):
    num = (height*width)%cover
    r = math.ceil(num)
    print(f"You'll need {r} cans")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

