def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mlt(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "na 0 ne dilit`sya"
    return a / b

a = float(input("num 1: "))
op = input("znak (+, -, *, /): ")
b = float(input("num 2: "))

match op:
    case "+":
        res = plus(a, b)
    case "-":
        res = minus(a, b)
    case "*":
        res = mlt(a, b)
    case "/":
        res = div(a, b)

print("result:", res)