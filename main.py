# Hieu Nguyen

stored_encoded_password = None

def encode(password):
    result = ""
    for digit in password:
        digit = int(digit)

        new_digit = digit + 3
        result += str(new_digit % 9 - 1 if new_digit > 9 else new_digit)

    return result

def decode():
    pass

def main():

    option = None

    while option != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option: "))

        if option == 1:
            stored_encoded_password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")
        elif option == 2:
            decode()
        elif option == 3:
            break

        print()




main()