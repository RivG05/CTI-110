#Geovany Rivas
#11/21/2023
#Use if/else to determine an employees pay

#Get user input
emp_name = input('Enter employee name: ')

emp_hours = float(input("Enter employee's hours: "))

emp_pay = float(input("Enter the emplotee's pay rate: "))

#Calculations
if emp_hours > 40:
    ot_hours = emp_hours - 40
    reg_hour = 40

#This represents if enmp_hours is 40 or less
else:
    ot_hours = 0
    reg_hours = emp_hours

#Calculate pay
ot_pay = (emp_pay * 1.5) * ot_hours
reg_pay = emp_pay * reg_hour
gross_pay = ot_pay + reg_pay

#Display employee information and pay
print("\nEmployee Name:", emp_name)
print("Pay Rate: $", format(emp_pay, ",.1f"))
print("Hours Worked: {:.1f}".format(emp_hours))
print("Pay Rate: $", format(emp_pay, ",.1f"))
print("OverTime: {:.1f}".format(ot_hours))
print("OverTime Pay: $", format(ot_pay, ",.2f"))
print("RegHour Pay: $", format(reg_pay, ",.2f"))
print("Gross Pay: $", format(gross_pay, ",.2f"))

