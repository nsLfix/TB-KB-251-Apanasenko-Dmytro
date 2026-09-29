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

print("=== calculator ===")
print("if u want close program write 'stop' or 'exit' ")

while True:
    op = input("\n write op (+, -, *, /) or 'stop': ")
    
    if op == "stop" or op == "exit":
        print("program closed")
        break

    if op != "+" and op != "-" and op != "*" and op != "/":
        print("error: unknwn command")
        continue

    a = float(input("first num: "))
    b = float(input("second num: "))

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