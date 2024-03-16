#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

a = 10
b = 5

sum = add(a, b)
print("{} + {} = {}".format(a, b, sum))

subtract = sub(a,  b)
print("{} - {} = {}".format(a, b, subtract))

multiply = mul(a, b)
print("{} * {} = {}".format(a, b, multiply))

divide = div(a, b)
print("{} / {} = {}".format(a, b, divide))
