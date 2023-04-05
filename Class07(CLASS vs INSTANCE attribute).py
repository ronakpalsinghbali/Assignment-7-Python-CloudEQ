# Class attributes vs Instance attribute

class Employee:
    
    company = "CLoudEQ"
    role = "Trainee"
    salary = 10000

Ronak = Employee()
Mayank = Employee()

# Here salary is taken from CLASS attribute.

print(f"Here Salary is taken from CLASS attribute: Ronak's salary: Rs.{Ronak.salary} \n")

print(f"Here Salary is taken from CLASS attribute: Mayank's salary: Rs.{Mayank.salary} \n")


# Changing the salary in INSTANCE attribute:

Mayank.salary = 10000 + 1000

Ronak.salary = 10000 - 1000


# Here salary is taken from INSTANCE attribute.

print(f"Here Salary is taken from INSTANCE attribute: Ronak's salary: Rs.{Ronak.salary} \n")

print(f"Here Salary is taken from INSTANCE attribute: Mayank's salary: Rs.{Mayank.salary} \n")



# As we can see the INSTANCE attribute took preference over CLASS attribute.


