##1. Create a greeting for your program

print("Welcome to the hacker name generator.\n")

#2. ask for the hacker name the person would like to generate

rawHackerString = input("What's the Hacker Name you'd like to generate?\n")

hackerString = rawHackerString.lower()

for char in hackerString:

    if char == "a":
        hackerString = hackerString.replace("a","4")
    elif char == "b":
        hackerString = hackerString.replace("b","B")
    elif char == "c":
        hackerString = hackerString.replace("c","C")
    elif char == "d":
        hackerString = hackerString.replace("d","D")
    elif char == "e":
        hackerString = hackerString.replace("e","3")
    elif char == "f":
        hackerString = hackerString.replace("f","F")
    elif char == "g":
        hackerString = hackerString.replace("g","6")
    elif char == "h":
        hackerString = hackerString.replace("h","H")
    elif char == "i":
        hackerString = hackerString.replace("i","1")
    elif char == "j":
        hackerString = hackerString.replace("j","J")
    elif char == "k":
        hackerString = hackerString.replace("k","K")
    elif char == "l":
        hackerString = hackerString.replace("l","L")
    elif char == "m":
        hackerString = hackerString.replace("m","M")
    elif char == "n":
        hackerString = hackerString.replace("n","N")
    elif char == "o":
        hackerString = hackerString.replace("o","0")
    elif char == "p":
        hackerString = hackerString.replace("p","P")
    elif char == "q":
        hackerString = hackerString.replace("q","9")
    elif char == "r":
        hackerString = hackerString.replace("r","R")
    elif char == "s":
        hackerString = hackerString.replace("s","5")
    elif char == "t":
        hackerString = hackerString.replace("t","7")
    elif char == "u":
        hackerString = hackerString.replace("u","U")
    elif char == "v":
        hackerString = hackerString.replace("v","V")
    elif char == "x":
        hackerString = hackerString.replace("x","X")
    elif char == "y":
        hackerString = hackerString.replace("y","Y")
    elif char == "z":
        hackerString = hackerString.replace("z","Z")

    else:
        pass


    print(f"The Hacker Name Generated is {hackerString}")
