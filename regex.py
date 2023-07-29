import re

v = "SupportsSecureRestorableState: and returning YES."

x = re.findall("s", v)

# print(x)


y = re.fullmatch("YES.", v)

# print(y)

z = re.match("Supp", v)

print(z.string)
