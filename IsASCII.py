class IsAscII:
    isascii = lambda s: len(s) == len(s.encode())

"""
EXAMPLE FOR FUTURE USAGES:
str1 = "♥O◘♦♥O◘♦"
str2 = "Python"

print(isascii(str1)) -> will return False
print(isascii(str2)) -> will return True"""