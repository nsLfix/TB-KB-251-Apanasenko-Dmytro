import math

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "na 0 ne dilit`sya"
    return a / b

a = float(input("num 1: "))
op = input("znak (+, -, *, /): ") 
b = float(input("num 2: "))

if op == "+":
    res = plus(a, b)
if op == "-":
    res = minus(a, b)
if op == "*":
    res = mult(a, b)
if op == "/":
    res = div(a, b)

print("result:", res)