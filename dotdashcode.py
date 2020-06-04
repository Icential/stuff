print("Awaiting input...")
msg = input()

def find_letter(mes):
    if (len(msg) <= 250):
        for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
            if i in mes:
                if i == " ":
                    continue
                if i == "a":
                    mes = mes.replace("a", "e")
                if i == "b":
                    mes = mes.replace("b", "t")
                if i == "c":
                    mes = mes.replace("c", "i")
                if i == "d":
                    mes = mes.replace("d", "a")
                if i == "e":
                    mes = mes.replace("e", "n")
                if i == "f":
                    mes = mes.replace("f", "m")
                if i == "g":
                    mes = mes.replace("g", "s")
                if i == "h":
                    mes = mes.replace("h", "u")
                if i == "i":
                    mes = mes.replace("i", "r")
                if i == "j":
                    mes = mes.replace("j", "w")
                if i == "k":
                    mes = mes.replace("k", "d")
                if i == "l":
                    mes = mes.replace("l", "k")
                if i == "m":
                    mes = mes.replace("m", "g")
                if i == "n":
                    mes = mes.replace("n", "o")
                if i == "o":
                    mes = mes.replace("o", "h")
                if i == "p":
                    mes = mes.replace("p", "v")
                if i == "q":
                    mes = mes.replace("q", "f")
                if i == "r":
                    mes = mes.replace("r", "l")
                if i == "s":
                    mes = mes.replace("s", "p")
                if i == "t":
                    mes = mes.replace("t", "j")
                if i == "u":
                    mes = mes.replace("u", "b")
                if i == "v":
                    mes = mes.replace("v", "x")
                if i == "w":
                    mes = mes.replace("w", "c")
                if i == "x":
                    mes = mes.replace("x", "y")
                if i == "y":
                    mes = mes.replace("y", "z")
                if i == "z":
                    mes = mes.replace("z", "q")
                if i == "A":
                    mes = mes.replace("A", "E")
                if i == "B":
                    mes = mes.replace("B", "T")
                if i == "C":
                    mes = mes.replace("C", "I")
                if i == "D":
                    mes = mes.replace("D", "A")
                if i == "E":
                    mes = mes.replace("E", "N")
                if i == "F":
                    mes = mes.replace("F", "M")
                if i == "G":
                    mes = mes.replace("G", "S")
                if i == "H":
                    mes = mes.replace("H", "U")
                if i == "I":
                    mes = mes.replace("I", "R")
                if i == "J":
                    mes = mes.replace("J", "W")
                if i == "K":
                    mes = mes.replace("K", "D")
                if i == "L":
                    mes = mes.replace("L", "K")
                if i == "M":
                    mes = mes.replace("M", "G")
                if i == "N":
                    mes = mes.replace("N", "O")
                if i == "O":
                    mes = mes.replace("O", "H")
                if i == "P":
                    mes = mes.replace("P", "V")
                if i == "Q":
                    mes = mes.replace("Q", "F")
                if i == "R":
                    mes = mes.replace("R", "L")
                if i == "S":
                    mes = mes.replace("S", "P")
                if i == "T":
                    mes = mes.replace("T", "J")
                if i == "U":
                    mes = mes.replace("U", "B")
                if i == "V":
                    mes = mes.replace("V", "X")
                if i == "W":
                    mes = mes.replace("W", "C")
                if i == "X":
                    mes = mes.replace("X", "Y")
                if i == "Y":
                    mes = mes.replace("Y", "Z")
                if i == "Z":
                    mes = mes.replace("Z", "Q")
        print("\n" + mes)
    else:
        print("Message is too long!")

find_letter(msg)