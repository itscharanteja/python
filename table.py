from prettytable import PrettyTable

x = PrettyTable()

x.field_names=['Name','age']
x.add_row(['Charan',18])
x.add_row(['Charan',18])
x.add_row(['Charan',18])

print(x)