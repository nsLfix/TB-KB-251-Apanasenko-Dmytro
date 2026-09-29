def dis(a,b,c):
    d = b ** 2 - 4 * a * c
    return d


a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

result = dis(a,b,c)
print("Result =", result)
