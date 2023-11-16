#Geovany Rivas
#11/14/2023
#Using lists to make grade anlaysis.

#Create an empty list for grades.
grades_list = []

#Ask the user to enter grades for each module.
mod1 = float(input("Enter grade for Module 1: "))
mod2 = float(input("Enter grade for Module 2: "))
mod3 = float(input("Enter grade for Module 3: "))
mod4 = float(input("Enter grade for Module 4: "))
mod5 = float(input("Enter grade for Module 5: "))
mod6 = float(input("Enter grade for Module 6: "))

#Connect the empty list to the module grades inputted from the people.
grades_list.append(mod1)
grades_list.append(mod2)
grades_list.append(mod3)
grades_list.append(mod4)
grades_list.append(mod5)
grades_list.append(mod6)

#Calculate lowest,highest,sum, and average.
lowest_grade = min(grades_list)
highest_grade = max(grades_list)
sum_of_grades = sum(grades_list)
average_grade = sum_of_grades / len(grades_list)


#Display the results of the grades
print("-----------------Results-----------------------")
print(f"Lowest Grade: {lowest_grade:.1f}")
print(f"Highest Grade: {highest_grade:.1f}")
print(f"Sum of Grades: {sum_of_grades:.1f}")
print(f"Average: {average_grade:.2f}")
print("---------------------------------------------------")
