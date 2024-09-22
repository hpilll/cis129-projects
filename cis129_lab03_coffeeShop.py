#This program is a text based program that calculates the total based on the input of the user.

print("*"*40) #prints stars for formatting purposes
print("My Coffee and Muffin Shop") #prints the introduction sentence
coffee = float(input("Number of coffees bought? ")) #user input where only integers can be inputted
muffin = float(input("Number of muffins bought? ")) #second user input where only integers can be inputted
print("*"*40) #prints stars for formatting purposes

print("") #prints a space

print("*"*40) #prints stars for formatting purposes
print("My Coffee and Muffin Shop Receipt") #receipt title
subtotal_1 = print(str(coffee) + " Coffee at $5 each: " + "$" + str(int(coffee * 5))) #calculates the total for the coffee
subtotal_2 = print(str(muffin) + " Muffins at $4 each: " + "$" + str(int(muffin * 4))) #calculates the total for the muffins
tax_value = ((coffee*5 + muffin*4) * 0.06) #calculates the tax
print("6% tax: " + str(tax_value)) #prints the tax
calculation = coffee * 5 + muffin * 4 + tax_value #calculates the total from everything
print("-"*10) #formatting in the receipt
print("Total: " + str(float(calculation))) #prints the total
print("*"*40) #formatting
