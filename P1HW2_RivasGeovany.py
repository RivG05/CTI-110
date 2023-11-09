# Uses string and integers to perform math

# 11/9/2023

# CTI-110 P1HW2 - Travel Expense

# Geovany Rivas


print("This program calculates and displays travel expenses")

#Ask user to enter their budget

Budget = int(input("Enter budget: "))

#Ask user to enter travel destination

Destination = input("Enter your travel destination: ")

#Ask user for amount they will spend on gas

Fuel = int(input("How much do you think you will spend on gas?: "))

#Ask user for amount they will spend on accommodation

Accommodation = int(input("Approximately, how much will you need for accomodation/hotel?: "))

#Ask user for amount they will spend on food

Food = int(input("Last, how much do you need for food?: "))

#Add expenses
print ("-------------Travel Expenses--------------")
print ("Location: ", Destination )
print ("Inital Budget: ", Budget)
print("\n") 
print ("Fuel: ",Fuel)
print ("Accommodation: ",Accommodation)
print ("Food: ",Food)



#Display Results of subtraction from expenses from budget
print("\n") 
print ("Remaining Balance: ", Budget-Fuel-Accommodation-Food)



