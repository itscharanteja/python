import request
resp = request.get("https://www.wikipedia.org/")
content = resp.content
print(content)