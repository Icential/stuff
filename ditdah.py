print("Awaiting input...")
msg = input()

def find_letter(msg):
    if (len(msg) <= 250):
        msg = list(msg)
        new_msg = ""
        for i in msg:
            if i == "a":
                i = "e"
            elif i == "b":
                i = "t"
            elif i == "c":
                i = "i"
            elif i == "d":
                i = "a"
            elif i == "e":
                i = "n"
            elif i == "f":
                i = "m"
            elif i == "g":
                i = "s"
            elif i == "h":
                i = "u"
            elif i == "i":
                i = "r"
            elif i == "j":
                i = "w"
            elif i == "k":
                i = "d"
            elif i == "l":
                i = "k"
            elif i == "m":
                i = "g"
            elif i == "n":
                i = "o"
            elif i == "o":
                i = "h"
            elif i == "p":
                i = "v"
            elif i == "q":
                i = "f"
            elif i == "r":
                i = "l"
            elif i == "s":
                i = "p"
            elif i == "t":
                i = "j"
            elif i == "u":
                i = "b"
            elif i == "v":
                i = "x"
            elif i == "w":
                i = "c"
            elif i == "x":
                i = "y"
            elif i == "y":
                i = "z"
            elif i == "z":
                i = "q"
            elif i == "A":
                i = "E"
            elif i == "B":
                i = "T"
            elif i == "C":
                i = "I"
            elif i == "D":
                i = "A"
            elif i == "E":
                i = "N"
            elif i == "F":
                i = "M"
            elif i == "G":
                i = "S"
            elif i == "H":
                i = "U"
            elif i == "I":
                i = "R"
            elif i == "J":
                i =  "W"
            elif i == "K":
                i = "D"
            elif i == "L":
                i = "K"
            elif i == "M":
                i = "G"
            elif i == "N":
                i = "O"
            elif i == "O":
                i = "H"
            elif i == "P":
                i = "V"
            elif i == "Q":
                i = "F"
            elif i == "R":
                i = "L"
            elif i == "S":
                i = "P"
            elif i == "T":
                i = "J"
            elif i == "U":
                i = "B"
            elif i == "V":
                i = "X"
            elif i == "W":
                i = "C"
            elif i == "X":
                i = "Y"
            elif i == "Y":
                i = "Z"
            elif i == "Z":
                i = "Q"
            else: i = i
            new_msg += i
        print("\n" + new_msg)
    else: print("Message is too long!")

find_letter(msg)