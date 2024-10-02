#This program is a text based program that calculates the total based on the input of the user.

print("*"*40) #prints stars for formatting purposes
print("My Coffee and Muffin Shop") #prints the introduction sentence
coffee = int(input("Number of coffees bought? ")) #user input where only integers can be inputted
muffin = int(input("Number of muffins bought? "))#second user input where only integers can be inputted
banana_bread = int(input("Number of banana breads bought?")) #third user input where only integers can be inputted
orange_juice = int(input("Number of orange juice boxes bought?")) #fourth user input where only integers can be inputted
print("*"*40) #prints stars for formatting purposes

print("") #prints a space

print("*"*40) #prints stars for formatting purposes
print("My Coffee and Muffin Shop Receipt") #receipt title
subtotal_1 = print(str(coffee) + " Coffee at $5 each: " + "$" + str(int(coffee * 5))) #calculates the total for the coffee
subtotal_2 = print(str(muffin) + " Muffins at $4 each: " + "$" + str(int(muffin * 4))) #calculates the total for the muffins
subtotal_3 = print(str(banana_bread) + " Banana Bread at $5 each: " + "$" + str(int(banana_bread * 5)))
subtotal_4 = print(str(orange_juice) + " Orange Juice Boxes at $2 each: " + "$" + str(int(orange_juice * 2)))
tax_value = ((coffee*5 + muffin*4 + banana_bread*5 + orange_juice*2) * 0.06) #calculates the tax
print("6% tax: " + str(tax_value)) #prints the tax
calculation = coffee * 5 + muffin * 4 + banana_bread * 5 + orange_juice * 2 + tax_value #calculates the total from everything
print("-"*10) #formatting in the receipt
print("Total: " + str(float(calculation))) #prints the total
print("*"*40) #formatting

print("Thanks for coming to the shop. Please come again!") #ending message
