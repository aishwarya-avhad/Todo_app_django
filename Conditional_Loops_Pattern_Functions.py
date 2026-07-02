# Conditional Statements
# 1. Leap Year Validator

year = int(input("Enter a Year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")

else:
    print(f"{year} is not a Leap Year")

# 2. Income Tax Calculator (given annual Income)

annual_income = float(input("Enter your Income: "))
tax_free_income = 250000

if annual_income <= 500000:
    tax = (annual_income - tax_free_income) * 0.05

elif annual_income <= 1000000:
    tax = (annual_income - tax_free_income)*0.2

elif annual_income > 1000000:
    tax = (annual_income - tax_free_income) * 0.3

print(tax) 

# 3. Triangle Type

a, b, c = map(int, input("Enter three sides of a triangle").split())

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b and b == c:
        print("Equilateral Triabgle")
    elif (a == b) or (a == c) or (b == c):
        print("Isoceles Triangle")
    elif a!=b and a!=c and b!=c:
        print("Scalene Triangle ")

else:
    print("Not a triangle")


# 4. Login System 

username = "python"
password = "python@123"

u_name = input("Enter username: ")
p_word = input("Enter password: ")

if u_name == username and p_word == password:
    print("Login Successful")

else:
    print("Invalid Credentials")

# 5. Electricity Bill

units_consumed = int(input("Enter the units consumed: "))
bill = 0
total_bill = 0

if units_consumed <= 100:
    bill = units_consumed * 5 
elif units_consumed <= 200:
    bill = (units_consumed - 100) * 8 + 500
elif units_consumed > 200:
    bill = (units_consumed - 200) * 10 + 500 + 800

if bill > 2000:
    total_bill = bill + (bill * 0.1)
else:
    total_bill = bill

print(total_bill)

# 6. Quadratic Equation Nature

a,b,c = map(int, input("Enter the values: ").split())

D = b * b - 4 * a * c

if D>0:
    print("Real and Unequal")
elif D==0:
    print("Real and equal")
else:
    print("Imaginary")

# 7. Loan Eleigibility

age = int(input("Enter your age: "))
salary = int(input("Enter your Salary: "))
credit_score = int(input("Enter your credit_score: "))
yoe = int(input("Enter years of employment: "))

if age >= 21:
    if salary >= 30000:
        if credit_score >= 700:
            if yoe >= 2:
                print("Eligible for Loan")
            else:
                print("Years of Experience not fulfilled")

        else:
            print("Credit Score not up to the mark")

    else:
        print("Salary insufficient for loan")

else:
    print("Age requirement not met")

# 8. Rock Paper Scissors

player1 = input("Your turn: ")
player2 = input("Your turn: ")

if player1 == "rock" and player2 == "scissor":
    print("Player1 wins")

elif player1 == "rock" and player2 == "paper":
    print("Player2 wins")

elif player1 == "rock" and player2 == "rock":
    print("Draw")

else:
    print("Invalid inputs")

# 9. Admission Eligibilty

physics = float(input("Enter physics marks: "))
chemistry = float(input("Enter chemistry marks: "))
maths = float(input("Enter maths marks: "))

total = physics + chemistry + maths
if (physics >= 60 and chemistry >= 60 and maths >= 65 and total >= 180) or (maths + physics >= 140):
    print("Eligible")
else:
    print("Not eligible")

#10. airline ticket discount

age = int(input("Enter your age: "))
gender = input("Select gender - M/F :  ")
is_student = input("Are you a student? y/n: ")
ticket_price = float(input("Enter your ticket price: "))

discount = 0

if age < 12:
    discount += 50
elif age >= 60:
    discount += 30

if gender == "F" or gender == "f":
    discount += 10

if is_student == "y" or is_student == "Y":
    discount += 5

if discount > 60:
    discount = 60

final_price = ticket_price - (ticket_price * discount/100)

print("Total Discount: ", discount, "%")
print("Final Ticket Price: ", final_price)












