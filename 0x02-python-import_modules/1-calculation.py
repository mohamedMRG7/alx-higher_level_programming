#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

sum = add(a, b)
print(f"10 + 5 = {sum}")

sub = sub(a, b)
print(f"10 - 5 = {sub}")

mul = mul(a, b)
print(f"10 * 5 = {mul}")

div = div(a, b)
print(f"10 / 5 = {div}")
