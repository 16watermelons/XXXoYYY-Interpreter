'''
Windows:

Run the following commands in the cmd prompt after downloading python

- pip install numpy

- python "<path to this python file>" "<path to the xxxoyyy file>"
'''

import os, sys, numpy, random

# Declare variables
variable = {f"{i:03}": numpy.int32(i) for i in range(1000)}
register = numpy.int32(0)
variable["AIO"] = numpy.int32(0)
variable["NIO"] = numpy.int32(0)
index = 0

debug_mode = input("Type anything to enter debug mode, press enter to skip")

# Check for file
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    sys.exit("No input file given >:3")
if os.path.exists(filename):
    text = open(filename, 'r').read()
    instruction = [[text[i], text[i + 1:i + 4]] for i in range(0, len(text), 4)]
else:
    sys.exit(f"'{filename}' wasn't found >:3")


# misc
def print_ascii(value):
    if 32 <= ord(value) <= 126:
        print(value)
    else:
        print(f"\\x{ord(value):02x}")

kaomoji = lambda: random.choice(["૮ ˶ᵔ ᵕ ᵔ˶ ა", "(˶˃ ᵕ ˂˶) .ᐟ.ᐟ", "    >⩊<   ", "(˶ˆᗜˆ˵)", "ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧", "₍^. .^₎⟆", "(˶ᵔ ᵕ ᵔ˶)", "(*ᴗ͈ˬᴗ͈)ꕤ*.ﾟ", "◝(ᵔᗜᵔ)◜", "(˶˃⤙˂˶)", "ᓚ₍⑅^..^₎♡", "ദ്ദി ˉ͈̀꒳ˉ͈́ )✧", "(⸝⸝> ᴗ•⸝⸝)"])

# Main loop
while index <= len(instruction) - 1:
    #x = input()
    output_flag = False
    if debug_mode:
        print(f"\n\n\n---------------\nINDEX: {index}")
    if debug_mode:
        print(instruction[index])
    if instruction[index][1] not in variable.keys():
        variable[instruction[index][1]] = numpy.int32(0)

    if instruction[index][1] == "NIO" and instruction[index][0] not in [":", ";", "(", ")"]:
        if instruction[index][1] == "NIO":
            variable["NIO"] = numpy.int32(int(input("Enter a numerical value: ")))
    elif instruction[index][1] == "AIO" and instruction[index][0] not in [":", ";", "(", ")"]:
        variable["AIO"] = numpy.int32(ord(input("Enter an ascii letter: ")))

    if instruction[index][0] == ".":
        register = variable[instruction[index][1]]
        if debug_mode:
            print(f"LOADING {variable[instruction[index][1]]} ({instruction[index][1]}) TO REGISTER!")
    elif instruction[index][0] == ":":
        variable[instruction[index][1]] = register
        if debug_mode:
            print(f"LOADING {register} (REG) TO {instruction[index][1]}!")
        output_flag = True
    elif instruction[index][0] == ";":
        e = variable[instruction[index][1]]
        char3 = chr(e % 128)
        e //= 128
        char2 = chr(e % 128)
        e //= 128
        char1 = chr(e % 128)
        full = char3+char2+char1
        if full not in variable.keys():
            variable[full] = numpy.int32(0)
        variable[full] = register
        if debug_mode:
            print(f"LOADING {register} (REG) TO THE ADDRESS STORED AT {instruction[index][1]} ({full})!")
        output_flag = True
    elif instruction[index][0] == ",":
        e = variable[instruction[index][1]]
        char3 = chr(e % 128)
        e //= 128
        char2 = chr(e % 128)
        e //= 128
        char1 = chr(e % 128)
        full = char1 + char2 + char3
        if full not in variable.keys():
            variable[full] = numpy.int32(0)
        register = variable[full]
        if debug_mode:
            print(f"LOADING THE VALUE AT THE ADDRESS STORED AT {variable[instruction[index][1]]} ({instruction[index][1]}), {variable[full]} ({full}) TO THE REGISTER!")
    elif instruction[index][0] == "#":
        register = ord(instruction[index][1][0]) * (128 ** 2) + ord(instruction[index][1][1]) * 128 + ord(instruction[index][1][2])
        if debug_mode:
            print(f"LOADING {ord(instruction[index][1][0]) * (128 ** 2) + ord(instruction[index][1][1]) * 128 + ord(instruction[index][1][2])} (ADDRESS OF {instruction[index][1]}) TO THE REGISTER!")
    elif instruction[index][0] == "+":
        register += variable[instruction[index][1]]
        if debug_mode:
            print(f"ADDING {variable[instruction[index][1]]} ({instruction[index][1]}) TO THE REGISTER!")
    elif instruction[index][0] == "-":
        register -= variable[instruction[index][1]]
        if debug_mode:
            print(f"SUBTRACTING {variable[instruction[index][1]]} ({instruction[index][1]}) FROM THE REGISTER!")
    elif instruction[index][0] == "*":
        register *= variable[instruction[index][1]]
        if debug_mode:
            print(f"MULTIPLYING THE REGISTER BY {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "/":
        register //= variable[instruction[index][1]]
        if debug_mode:
            print(f"DIVIDING THE REGISTER BY {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "/":
        register %= variable[instruction[index][1]]
        if debug_mode:
            print(f"MODULATING THE REGISTER BY {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "&":
        register &= variable[instruction[index][1]]
        if debug_mode:
            print(f"AND-ING THE REGISTER WITH {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "!":
        register ^= variable[instruction[index][1]]
        if debug_mode:
            print(f"XOR-ING THE REGISTER WITH {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "|":
        register |= variable[instruction[index][1]]
        if debug_mode:
            print(f"OR-ING THE REGISTER WITH {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "=":
        if register == variable[instruction[index][1]]:
            register = 1
        else:
            register = 0
        if debug_mode:
            print(f"CHECKING FOR EQUIVALENCE BETWEEN THE REGISTER AND {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == ">":
        if register > variable[instruction[index][1]]:
            register = 1
        else:
            register = 0
        if debug_mode:
            print(f"CHECKING IF THE REGISTER IS GREATER THAN {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "<":
        if register < variable[instruction[index][1]]:
            register = 1
        else:
            register = 0
        if debug_mode:
            print(f"CHECKING IF THE REGISTER IS LESS THAN {variable[instruction[index][1]]} ({instruction[index][1]})!")
    elif instruction[index][0] == "(":
        name = instruction[index][1]
        index += 1
        while instruction[index][1] != name:
            index += 1
        if debug_mode:
            print(f"JUMPING FORWARDS TO {instruction[index][1]}!")
    elif instruction[index][0] == ")":
        name = instruction[index][1]
        index -= 1
        while instruction[index][1] != name:
            index -= 1
        if debug_mode:
            print(f"JUMPING BACKWARDS TO {instruction[index][1]}!")
    elif instruction[index][0] == "[":
        register = variable[instruction[index][1]]
        if debug_mode:
            print(f"LOADING {variable[instruction[index][1]]} ({instruction[index][1]}) TO REGISTER AND SETTING LOOP POINT!")
    elif instruction[index][0] == "]":
        if register > 0:
            while instruction[index][0] != "[":
                index -= 1
            if debug_mode:
                print(f"{register} (REG) > 0. JUMPING TO LOOP POINT!")
        else:
            if debug_mode:
                print(f"{register} (REG) <= 0. LEAVING LOOP!")
    elif instruction[index][0] == "~":
        if debug_mode:
            print(f"HALTING PROGRAM!")
        break
    elif instruction[index][0] == "?":
        e = register
        register = variable[instruction[index][1]]
        if e < 1:
            index += 1
        if debug_mode:
            print(f"CHECKING THE REGISTER (?) !")
    else:
        if debug_mode:
            print(f"INVALID OPCODE!")




    if output_flag:
        if instruction[index][1] == "NIO":
            if debug_mode:
                print("--> NIO: ", end='')
            print(variable["NIO"])

        elif instruction[index][1] == "AIO":
            if debug_mode:
                print("--> AIO:", end='')
            print_ascii(str(chr(variable["AIO"]&0b1111111)))

    index += 1
    if debug_mode:
        print(kaomoji() + "\n---------------")

sys.exit("\n\nEnd of program")



