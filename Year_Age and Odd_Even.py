from datetime import date

age = input("Enter age: ")
age = int(age)
name = input("Enter your name: ")
print("Your age is ", age, "and your name is ", name)
current_year = date.today().year
hundred_years = (current_year + 100)
answer = (hundred_years - age)

print("You will be 100 years old in", answer)

if age % 2 == 0:
    print("Your age is even.")
else:
    print("Your age is odd.")
    
             
