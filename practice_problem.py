## 1. Sales Target Checker

#A shop owner wants to check daily sales.

#- Ask how many days the shop operated.
#- For each day, ask the sales amount.
#- Count how many days had sales of 100,000 or more.
#- Display the number of successful days.
#Write a Python program to count how many days reached the sales target.

days=int(input("Enter days"))
count=0
for i in range(days):
   sales=int(input("Enter sales amount"))
    
   if sales>=100000:
       count+=1

print("Successful days",count)
  

## 2. Number Analyzer

#A program receives 10 numbers from a user.

#For each number:

#- Check whether it is positive, negative, or zero.
#- Count the positive numbers.
#- Count the negative numbers.
#- Count the zeros.

#Write a Python program to analyze 10 numbers and count positive numbers, negative numbers, and zeros.
# Positive, Negative, and Zero Counter

positive = 0
negative = 0
zero = 0

for i in range(10):
   num = int(input("Enter a number: "))

   if num > 0:
       positive += 1
   elif num < 0:
       negative += 1
   else:
       zero += 1

print("Positive numbers:", positive)
print("Negative numbers:", negative)
print("Zeros:", zero)

## 3. Bank Transaction Checker

#A bank wants to process 10 transactions.

#For each transaction:

#- Ask for the transaction amount.
#- A positive amount means a deposit.
#- A negative amount means a withdrawal.
#- Zero means no transaction.

#At the end, display:

#- Number of deposits
#- Number of withdrawals
#- Total deposited amount
#- Total withdrawn amount

#Write a Python program to process and summarize 10 bank transactions.
deposit=0
withdraw=0
total_de=0
total_with=0
for i in range(10):
    transaction=float(input("Enter transaction amount"))
    
    if transaction > 0:
        deposit+=1
        total_de+=transaction
        
    elif transaction < 0:
        withdraw+=1
        total_with+=abs(transaction)

    else:
        print("No transaction")
        
print("number of deposits",deposit)
print("nubmer of withdraw",withdraw)
print("total deposits",total_de)
print("total withdraw",total_with)
       
    
        
    

## 4. Cinema Ticket System

#A cinema sells tickets.

#- Ask how many customers want tickets.
#- For each customer, ask their age.
#- Under 13 → Child ticket = 5
#- 13–59 → Adult ticket = 10
#- 60 or above → Senior ticket = 7

#At the end, display the total ticket price.

#Write a Python program to calculate the total cinema ticket price for multiple customers.
customers=int(input("Enter number of customers"))
total_price=0
for i in range(customers):
    age=int(input("Enter age:"))
    
    if age < 13:
        total_price+=5
    elif age > 13 and age < 59 :
        total_price+=10
    else:
        total_price+=7
print("Total ticket price:", total_price)


# Employee Salary Checker

employees = int(input("Enter number of employees: "))

high_salary = 0
low_salary = 0
total_salary = 0

for i in range(employees):
    salary = float(input("Enter salary: "))

    if salary > 500000:
        high_salary += 1
    else:
        low_salary += 1

    total_salary += salary

average_salary = total_salary / employees

print("Employees with salary greater than 500,000:", high_salary)
print("Employees with salary 500,000 or less:", low_salary)
print("Total salary:", total_salary)
print("Average salary:", average_salary)

## 6. Student Attendance System

#A teacher wants to record attendance for a class.

#- Ask how many students are in the class.
#- For each student, enter:
#  - P for Present
#  - A for Absent
#- Count the total present students.
#- Count the total absent students.
#- Calculate the attendance percentage.

#Write a Python program to calculate the attendance summary of a class.
# Student Attendance System

students = int(input("Enter number of students: "))

present = 0
absent = 0

for i in range(students):
    attendance = input("Enter attendance (P/A): ").upper()

    if attendance == "P":
        present += 1
    elif attendance == "A":
        absent += 1

attendance_percentage = (present / students) * 100

print("Total present students:", present)
print("Total absent students:", absent)
print("Attendance percentage:", attendance_percentage, "%")

## 7. Monthly Sales Report

#A shop has sales for 30 days.

#- Ask for the sales amount for each day.
#- Calculate total sales.
#- Find the highest sales amount.
#- Find the lowest sales amount.
#- Count how many days had sales above 100,000.

#Write a Python program to create a simple monthly sales report.
# Monthly Sales Report

total_sales = 0
highest_sales = 0
lowest_sales = 0
count = 0

for i in range(30):
    sales = float(input("Enter daily sales: "))

    total_sales += sales

    if i == 0:
        highest_sales = sales
        lowest_sales = sales
    else:
        if sales > highest_sales:
            highest_sales = sales

        if sales < lowest_sales:
            lowest_sales = sales

    if sales > 100000:
        count += 1

print("Total sales:", total_sales)
print("Highest sales:", highest_sales)
print("Lowest sales:", lowest_sales)
print("Days with sales above 100,000:", count)
## 8. Mini Shopping System

#Create a simple shopping system.

#- Ask how many products the customer wants to buy.
#- For each product, ask for its price.
#- Calculate the total price.
#- If the total is 100 or more, give a 10% discount.
#- If the total is 200 or more, give a 20% discount.
#- Display:
 # - Total price
  #- Discount
  #- Final price

#Write a Python program to create a simple shopping system.
# Shopping System

products = int(input("Enter number of products: "))

total_price = 0
discount = 0

for i in range(products):
    price = float(input("Enter product price: "))
    total_price += price

if total_price >= 200:
    discount = total_price * 0.20

elif total_price >= 100:
    discount = total_price * 0.10

print("Total price:", total_price)
print("Discount:", discount)
print("Final price:", total_price - discount)
