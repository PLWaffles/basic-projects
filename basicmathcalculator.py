def start():
    print("Still don't understand this part")

while True:
    print("THIS IS THE BASIC MATH CALCULATOR!")
    print("It can add, subtract, multiply and divide TWO terms.")

    define = input("Type either 'add', 'sub', 'mul', or 'div' (type 'end' to stop the calcuator): ")
    define.lower()

    if define == "add":
        print("You selected addition.")
        addx = input("Type your first term: ")
        addx.lower()
        if addx.isdigit():
            addy = input("Type your second term: ")
            addy.lower()
            if addy.isdigit():
                addtotal = int(addx) + int(addy)
                print(int(addx), "+", int(addy), "=", int(addtotal))
                print("")
            else:
                print("Invalid Input: not an integer")
                print("")
        else:
            print("Invalid Input: not an integer")
            print("")

    elif define == "sub":
        print("You selected subtraction.")
        subx = input("Type your first term: ")
        subx.lower()
        if subx.isdigit():
            suby = input("Type your second term: ")
            suby.lower()
            if suby.isdigit():
                subtotal = int(subx) - int(suby)
                print(int(subx), "-", int(suby), "=", int(subtotal))
                print("")
            else:
                print("Invalid Input: not an integer")
                print("")
        else:
            print("Invalid Input: not an integer")
            print("")

    elif define == "mul":
        print("You selected multiplication.")
        mulx = input("Type your first term: ")
        mulx.lower()
        if mulx.isdigit():
            muly = input("Type your second term: ")
            muly.lower()
            if muly.isdigit():
                multotal = int(mulx) * int(muly)
                print(int(mulx), "*", int(muly), "=", int(multotal))
                print("")
            else:
                print("Invalid Input: not an integer")
                print("")
        else:
            print("Invalid Input: not an integer")
            print("")

    elif define == "div":
        print("You selected division.")
        divx = input("Type your first term: ")
        divx.lower()
        if divx.isdigit():
            divy = input("Type your second term: ")
            divy.lower()
            if divy.isdigit():
                divtotal = int(divx) / int(divy)
                print(int(divx), "/", int(divy), "=", int(divtotal))
                print("")
            else:
                print("Invalid Input: not an integer")
                print("")
        else:
            print("Invalid Input: not an integer")
            print("")

    elif define == "end":
        print("Thank you for using Paul's calculator!")
        break

    else:
        print("Invalid Input: not a valid response ('add', 'sub', 'mul', 'div' or 'end')")
        print("")
