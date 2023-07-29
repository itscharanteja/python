class valid1:
    def valid(self, s: str):
        str = []
        for i in s:

            if i == "{" or i == "(" or i == "[":
                str.append(i)
            else:
                # if not str:
                #     return False
                if i == "]" and str[-1] == "[":
                    str.pop()
                elif i == ")" and str[-1] == "(":
                    str.pop()
                elif i == "}" and str[-1] == "{":
                    str.pop()
                else:
                    return False
        return not str


b = valid1()
print(b.valid("]"))
