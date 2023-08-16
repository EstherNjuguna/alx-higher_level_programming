#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    sum_result = add(a, b)
    sub_result = sub(a, b)
    mul_result = mul(a, b)
    div_result = div(a, b)
    print("10 + 5 =", sum_result)
    print("10 - 5 =", sub_result)
    print("10 * 5 =", mul_result)
    print("10 / 5 =", div_result)
