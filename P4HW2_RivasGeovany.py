#Geovany Rivas
#11/21/2023
#Use if/else to determine an employees pay and now add while

#Create variables to hold totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0


#Get user input
emp_name = input('Enter employee name or type Done to quit: ')

#Loop to control adding employees
while emp_name != "Done":
    num_em += 1
    emp_hours = float(input("Enter employee's hours: "))
    emp_pay = float(input("Enter the emplotee's pay rate: "))


    #Calculations
    if emp_hours > 40:
        ot_hours = emp_hours - 40
        reg_hours = 40

    #This represents if enmp_hours is 40 or less
    else:
        ot_hours = 0
        reg_hours = emp_hours

    #Calculate pay
    ot_pay = (emp_pay * 1.5) * ot_hours
    total_ot += ot_pay
    
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay
    

    #Display employee information and pay
    print("\nEmployee Name:", emp_name)
    print("Pay Rate: $", format(emp_pay, ",.1f"))
    print("Hours Worked: {:.1f}".format(emp_hours))
    print("Pay Rate: $", format(emp_pay, ",.1f"))
    print("OverTime: {:.1f}".format(ot_hours))
    print("OverTime Pay: $", format(ot_pay, ",.2f"))
    print("RegHour Pay: $", format(reg_pay, ",.2f"))
    print("Gross Pay: $", format(gross_pay, ",.2f"))
    print()
    emp_name = input('Enter employee name or type Done to quit: ')


#This code executes after the loop breaks
print("Done adding employees")
print("")
print(f"Total number of employees entered: {num_em}")
print(f"Total amount paid for overtime: {total_reg}")
print(f"Total amount paid for regular hours: {total_ot}")
print(f"Total amount paid in gross: {total_gross}")
