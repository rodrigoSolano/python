from re import match

def isDigit(string):
    return bool(match(r"^[-+]?\d+\.?\d*?$", string))

print(isDigit("-255.00"))