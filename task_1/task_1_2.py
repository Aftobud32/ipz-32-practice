def int_to_string(n):
    if n == 0:
        return "0"

    result = ""
    is_negative = False

    if n < 0:
        is_negative = True
        n = -n

    while n > 0:
        digit = n % 10
        result = chr(ord('0') + digit) + result
        n //= 10

    if is_negative:
        result = "-" + result

    return result

num = 4512
print(int_to_string(num))

num_neg = -123
print(int_to_string(num_neg))

num_zero = 0
print(int_to_string(num_zero))