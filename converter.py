while True:
    #Get from base for conversion
    while True:
        validfrombases = ("binary", "hexadecimal", "octal", "decimal")
        frombase = input("Would you like to convert from binary, decimal, hexadecimal or octal? ").lower()
        if frombase not in validfrombases:
            print("Invalid input please enter \"binary\", \"decimal\", \"octal\" or \"hexadecimal\"")
        else:
            break

    #Binary
    if (frombase == "Binary" or frombase == "binary"):
        while True:
            binaryinput = input("Please enter your binary number: ")
            try:
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

    #Decimal
    if (frombase == "Decimal" or frombase == "decimal"):
        while True:
            decimalinput = input("Please enter your decimal number: ")
            try:
                decimalinput = int(decimalinput)
                binfromdecimal = bin(decimalinput)
                octfromdecimal = oct(decimalinput)
                hexfromdecimal = hex(decimalinput)
                break
            except ValueError:
                print("Invalid input please enter a decimal number")
        print()
        print("Your binary number in:")
        print("binary -", binfromdecimal)
        print("octal -", octfromdecimal)
        print("hexadecimal -", hexfromdecimal)

    #Octal
    if (frombase == "Octal" or frombase == "octal"):
        while True:
            octalinput = input("Please enter your octal number: ")
            try:
                decimalfromoct = int(octalinput, 8)
                binfromoct = bin(decimalfromoct)
                hexfromoct = hex(decimalfromoct)
                break
            except ValueError:
                print("Invalid input please enter a decimal number")
        print()
        print("Your octal number in:")
        print("decimal -", decimalfromoct)
        print("binary -", binfromoct)
        print("hexadecimal -", hexfromoct)

    #Hexadecimal
    if (frombase == "Hexadecimal" or frombase == "hexadecimal"):
        while True:
            hexinput = input("Please enter your hexadecimal number: ")
            try:
                decimalfromhex = int(hexinput, 16)
                binfromhex = bin(decimalfromhex)
                octfromhex = oct(decimalfromhex)
                break
            except ValueError:
                print("Invalid input please enter a decimal number")
        print()
        print("Your octal number in:")
        print("decimal -", decimalfromhex)
        print("binary -", binfromhex)
        print("octal -", octfromhex)
    
    #Asks the user if they want to re-run the pogram
    print()
    while True:
        validrepeatinput = ("yes", "no", "y", "n")
        repeat = input("Would you like to run the pogram again? ").lower()
        if repeat not in validrepeatinput:
            print("Invalid in put please enter \"yes\", \"no\", \"y\" or \"n\"")
        else:
            break
    if (repeat == "yes" or repeat == "y"):
            print()
    else:
        break
