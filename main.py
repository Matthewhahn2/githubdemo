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


while True:
    print(f"""Menu
---------------
1. Encode
2. Dedode
3. Quit
""")

    ms = int(input("Please enter an option: "))

    if ms == 1:
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!")
    if ms ==2:
        asnwer = print(f" The encoded password is {encoded}, and the original password is {password}")
    if ms == 3:
        break