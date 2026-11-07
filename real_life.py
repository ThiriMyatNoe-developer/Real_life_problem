#16. Shopping Bill
#A shirt costs 15,000 MMK. A customer buys 3 shirts. Calculate the total price.
"""
shirt_cost=15000
quality=3
total_price=shirt_cost*quality
print(total_price)

"""
#17. Discount Calculator
#A product costs 50,000 MMK. The shop gives a 10% discount. Calculate the discount amount and final price.
"""
product_cost=50000
discount_percentage=10
discount_amount=product_cost*discount_percentage/100
final_price=product_cost-discount_amount
print("Discount Amount:",discount_amount)
print("Final Price:",final_price)

"""
#18. Student Marks
#A student gets 70, 80, and 90 marks in three subjects. Calculate the total and average marks.
"""
student_marks=[70, 80, 90]
total_marks=sum(student_marks)
average_marks=total_marks/len(student_marks)
print("Total Marks:",total_marks)
print("Average Marks:",average_marks)

"""
#19. Age Calculator
#Ask the user to enter their birth year. Calculate their approximate age using the current year, 2026.
"""
birth_year=int(input("Enter your birth year:"))
current_year=2026
age=current_year-birth_year
print("Your approximate age is:",age)

"""
#20. Split a Bill
#A group of 4 friends shares a bill of 25,000 MMK equally. Calculate how much each person pays and the remaining amount.
"""
friends=4
total_bill=25000
each_person_pays=total_bill/friends
remaining_amount=total_bill%friends
print("Each person pays:",each_person_pays)
print("Remaining amount:",remaining_amount)

"""
#21. Seconds Converter
#Ask the user to enter a number of seconds. Convert it into hours, minutes, and remaining seconds.
"""
seconds=int(input("Enter number of seconds:"))
hours=seconds//3600
minutes=(seconds%3600)//60
remaining_seconds=seconds%60
print("Hours:",hours)
print("Minutes:",minutes)
print("Remaining seconds:",remaining_seconds)

"""
#22. Temperature Converter
#Ask the user to enter a temperature in Celsius. Convert it to Fahrenheit using the formula F = (C * 9 / 5) + 32.
"""
C=float(input("Enter temperature in Celsius:"))
F=(C * 9 / 5) + 32
print("Temperature in Fahrenheit:",F)

"""
#23. BMI Calculator
#Ask the user to enter weight in kilograms and height in meters. Calculate BMI using weight / (height ** 2).
"""
kg=float(input("Enter weight in kilograms:"))
m=float(input("Enter height in meters:"))
BMI=kg/(m**2)
print("BMI:",BMI)

"""
#24. Simple Interest
#Ask the user to enter the principal, annual interest rate, and time in years. Calculate simple interest using P * R * T / 100.
"""
P=float(input("Enter principal amount:"))
R=float(input("Enter annual interest rate (in %):"))
T=float(input("Enter time in years:"))
simple_interest=(P * R * T) / 100
print("Simple Interest:",simple_interest)

"""
#25. Digit Calculator
#Ask the user to enter a two-digit integer. Find its tens digit and ones digit using // and %.
two_digit_number=int(input("Enter a two-digit integer:"))
tens_digit=two_digit_number//10
ones_digit=two_digit_number%10
print("Tens digit:",tens_digit)
print("Ones digit:",ones_digit)
