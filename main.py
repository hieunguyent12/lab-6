def encode(password):
    result = ""
    for digit in password:
        digit = int(digit)

        new_digit = digit + 3
        result += str(new_digit % 9 - 1 if new_digit > 9 else new_digit)

    return result


def main():
    a = encode(input("Enter a password: "))
    print(a)

main()