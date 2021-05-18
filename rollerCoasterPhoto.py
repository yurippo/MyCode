print("Welcome to the rollercoaster!")

height = float(input("What is your height in cm? "))
bill = 0

if height > 120.0:
    print("You can ride the rollercoaster!")
    age = int(input("What's your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are$ 7")
    else:
        bill = 12
        print("Adult tickets are$ 12")

    wantsPhoto = input("Do you want a photo taken? Y or N ")
    if wantsPhoto == "Y":
        #add $3 to their bill
        bill = bill + 3
        ###or a more simple way to write that bill+= 3
        print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride :(")
