import requests
import flask

a = requests.get("https://www.geeksforgeeks.org/python-program-add-two-matrices/")

print(a.text)