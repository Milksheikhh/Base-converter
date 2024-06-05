while True:
    # Get the base to convert from
    while True:
        validfrombases = ("binary", "hexadecimal", "octal", "decimal")
        frombase = input("Would you like to convert from binary, decimal, hexadecimal or octal? ").lower()
        if frombase not in validfrombases:
            print("Invalid input please enter \"binary\", \"decimal\", \"octal\" or \"hexadecimal\"")
        else:
            break

    # Conversion from binary
    if frombase == "binary":
        while True:
            binaryinput = input("Please enter your binary number: ")
            try:
                # Convert binary to decimal, octal, and hexadecimal
                decimalfrombin = int(binaryinput, 2)
                octfrombin = oct(decimalfrombin)
                hexfrombin = hex(decimalfrombin)
                break
            except ValueError:
                print("Invalid input please enter a binary number")
        print()
        print("Your binary number in:")
        print("decimal -", decimalfrombin)
        print("octal -", octfrombin)
        print("hexadecimal -", hexfrombin)

    # Conversion from decimal
    if frombase == "decimal":
        while True:
            decimalinput = input("Please enter your decimal number: ")
            try:
                # Convert decimal to binary, octal, and hexadecimal
                decimalinput = int(decimalinput)
                binfromdecimal = bin(decimalinput)
                octfromdecimal = oct(decimalinput)
                hexfromdecimal = hex(decimalinput)
                break
            except ValueError:
                print("Invalid input please enter a decimal number")
        print()
        print("Your decimal number in:")
        print("binary -", binfromdecimal)
        print("octal -", octfromdecimal)
        print("hexadecimal -", hexfromdecimal)

    # Conversion from octal
    if frombase == "octal":
        while True:
            octalinput = input("Please enter your octal number: ")
            try:
                # Convert octal to decimal, binary, and hexadecimal
                decimalfromoct = int(octalinput, 8)
                binfromoct = bin(decimalfromoct)
                hexfromoct = hex(decimalfromoct)
                break
            except ValueError:
                print("Invalid input please enter a valid octal number")
        print()
        print("Your octal number in:")
        print("decimal -", decimalfromoct)
        print("binary -", binfromoct)
        print("hexadecimal -", hexfromoct)

    # Conversion from hexadecimal
    if frombase == "hexadecimal":
        while True:
            hexinput = input("Please enter your hexadecimal number: ")
            try:
                # Convert hexadecimal to decimal, binary, and octal
                decimalfromhex = int(hexinput, 16)
                binfromhex = bin(decimalfromhex)
                octfromhex = oct(decimalfromhex)
                break
            except ValueError:
                print("Invalid input please enter a valid hexadecimal number")
        print()
        print("Your hexadecimal number in:")
        print("decimal -", decimalfromhex)
        print("binary -", binfromhex)
        print("octal -", octfromhex)
    
    # Ask the user if they want to re-run the program
    print()
    while True:
        validrepeatinput = ("yes", "no", "y", "n")
        repeat = input("Would you like to run the program again? ").lower()
        if repeat not in validrepeatinput:
            print("Invalid input please enter \"yes\", \"no\", \"y\" or \"n\"")
        else:
            break
    if repeat == "yes" or repeat == "y":
        print()
    else:
        break
