lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dir = input("Enter encode to encrypt or decode to decrypt").lower()
txt = input("Enter text :")
shift = int(input("Enter shift number"))
def ceaser(start,direction):
    end = ""
    if dir == "encode":
        txt = txt.split()
        