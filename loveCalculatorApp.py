###Don't change the code below
print("Welcome to the love calculator!")

name1 = input("What's your name? ")

name2 = input("What's their name? ")

##Don't change the code above

##Write your code below the line

combinedString = name1 + name2

lowerCaseString = combinedString.lower()

t = lowerCaseString.count("t")
r = lowerCaseString.count("r")
u = lowerCaseString.count("u")
e = lowerCaseString.count("e")

true = t + r + u + e

l = lowerCaseString.count("l")
o = lowerCaseString.count("o")
v = lowerCaseString.count("v")
e = lowerCaseString.count("e")


love = l + o + v + e


loveScore = str(true) + str(love)

intScore = int(loveScore)

if intScore < 10 or intScore > 90:
    print(f"Your love score is {loveScore}, you go together like coke and mentos.")

elif intScore >= 40 and intScore <= 50:
    print(f"Your love score is {loveScore}, you go ok together.")

else:
    print(f"Your score is {loveScore}")
