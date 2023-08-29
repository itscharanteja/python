import cgi

# Get form data from the client's request
form = cgi.FieldStorage()

# Extract values from the form
username = form.getvalue("username")
password = form.getvalue("password")

# Generate an HTML response
print("Content-type: text/html\n")
print("<html><body>")
print(f"<p>Username: {username}</p>")
print(f"<p>Password: {password}</p>")
print("</body></html>")
