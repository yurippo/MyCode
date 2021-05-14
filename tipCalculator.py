#if the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")

#Create a variable to store the users input but that will come as a string so
#we need to use float to convert this string into a number so we can calculate

bill = float(input("What was the total bill? $"))

#Create another variable tip to store the input and as the number options as integers
#10,12 or 15 I'll use int to convert the string into integer

tip = int(input("How much % tip would you like to give 10, 12 or 15?"))

#Create another variable people to store the input and as the number options as integers
# never had a meal with 1.5 people right I'll use int to convert the string into integer

people = int(input("How many people to split the bill?"))

##Now that we've collected all the data from the user we'll go ahead and create
##the final calculation of the total bill

billWithTip = tip / 100 * bill + bill

###We'll go ahead and create the bill amount per person

billPerPerson = billWithTip / people

###use the python round function to limit the decimal places and set it in a final amount variable

finalAmount = round(billPerPerson, 2)

####Use the format function to format the decimal number

finalAmount = "{:.2f}".format(billPerPerson)

###Now we go ahead and print the final bill and results to the user

print(f"Each person should pay: ${finalAmount} ")
