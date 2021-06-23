from datetime import date

# Program calculate year of birth!
#Create program that calculates the year of birth.

#Tasks
# define the variables age and name
age = 31
name = "Diana"

# make a calculation for the year in which the person was born
year_of_birth = 2021 - age;

# print out "OMG <person>, you are <age> years old so you were born in <year>" with the correct values
print(f'OMG {name}, you are {age} years old so you were born in {year_of_birth}')

# Second Part
# prompt the user for input and re-assign the variable age and name
age = input("Enter your age: ")
name = input("Enter your name: ")

# figure out a way to account for if the persons birthday has already happened this year or not
birth_date = "03/09/1996"


# Extra
# go look into the library time
# print out the amount of hour this person has lived

# Acceptance Criteria
# program defines the variable age and name
# program prints the string "OMG <person>, you are <age> years old so you were born in <year>"
