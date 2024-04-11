#Matthew Hahn

def encode(password):
    encoded = ''
    for digit in password:
        shifted = int(digit) + 3
        if shifted > 9:
            encoded += str(shifted - 10)
        else:
            encoded += str(shifted)
    return encoded

def display_menu():
    print(f"""Menu
---------------
1. Encode
2. Dedode
3. Quit
""")

def decoder(encoded):
    decoded = ''
    for digit in encoded:
        if int(digit) < 3:
            shifted = (int(digit) + 10) - 3
        else:
            shifted = int(digit) - 3
        decoded += str(shifted)
    return decoded
def main():
    encoded = ''
    while True:
        display_menu()
        ms = int(input("Please enter an option: "))

        if ms == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!")
        elif ms ==2:
            decoded = decoder(encoded)
            asnwer = print(f" The encoded password is {encoded}, and the original password is {decoded}")
        elif ms == 3:
            break

if __name__ == "__main__":
    main()