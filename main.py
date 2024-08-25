 # Basic Exercises for Arth Operators

#===============================================Addition=====================================================


# You drove 250 miles on the first day and 320 miles on the second day,
# How many miles did you drive in total by the end of the second day? 


# Example 1 : 

# first_day = int(input ("Enter the miles driven on the first day:"))
# second_day = int(input (" Enter the miles driven on the second day:"))
# total_miles_driven = first_day + second_day
# print(total_miles_driven)




# Question 2: 
# You bought a shirt for 2000, a pair of jeans for 3000, and a pair of shoes for 4000.
#How much did you spend in total for these three items? 

# Example 2 : 
# shirt_price = int(input("Enter the price of the shirt:"))
# jeans_price = int(input("Enter the price of the jeans:"))
# shoes_price = int(input("Enter the price of the shoes:"))
# total_spent = shirt_price + jeans_price + shoes_price 
# print(total_spent)


#==========================================Substraction=====================================================

# Question 3: 
# You had 50000 in your bank account and withdrew 20000 for a concert ticket. 
#How much money do you have left in your account after the withdrawal? 

# Example 3: 

# initial_blnc = int(input("Enter your initial balance:"))
# withdrew_blnc = int(input("Enter the amount you withdrew:"))
# remaining_blnc = initial_blnc - withdrew_blnc 
# print(f'Your remaining blnc is {remaining_blnc}')


# Question 4: 
# You needed 5 cups of flour for your recipe but only had 2 cups. How many more
# cups of flour do you need? 

# Example 4 : 
# required_cups = int(input("Enter the required cups of flour:"))
# available_cups = int(input("Enter the available cups of flour:"))
# flour_needed = required_cups - available_cups
# print(f"Additional flour needed: {flour_needed} Cups")



# Extra Question: 
# You've consumed 800 calories for breakfast and 600 calories for lunch. If your 
# daily calorie limit is 2,000, how many more calories can you consume for dinner and 
# snacks without exceeding your limit? 

# Example Extra : 

# Breakfast_cal = int(input("Enter the calories consumed for breakfast:"))
# lunch_cal = int(input("Enter the calories consumed for lunch:"))
# daily_cal = int(input("Enter your daily calorie limit:"))

# merge_calories = Breakfast_cal + lunch_cal 
# remaining_cal = daily_cal - merge_calories
# print(f"Remaining calorie limit: {remaining_cal}")


#==========================================Multiplications=====================================================

# Question 5:

# Each student needs a ticket that costs 500, and you have 25 students going on the trip.
# How much will the total cost of the tickets be? 

# Example 5 : 

# ticket_price = int(input("Enter the ticket price:"))
# no_of_std = int(input("Enter the number of students:"))
# total_cost = ticket_price * no_of_std
# print(f"Total cost of tickets: {total_cost}")


# Question 6: 

# Your  garden is 10 feet long and 5 feet wide. How many square feet of soil
# will you need to cover the entire garden? 

# Formula to calculate the Square Feet =  Length x Width 

# Example 6 : 

# length = int(input("Enter the length of the garden (in feet):"))
# width = int(input("Enter the width of the garden (in feet):"))
# total_Area = length * width
# print(f"Total area of the garden is {total_Area} square feet")



#==========================================Division=====================================================

# Question 7: 

# You are planning a dinner, and you have 36 cupcakes to share among your guests.
# If you want to ensure that each guest receives an equal number of cupcakes, 
# how many guests can you invite to your dinner? 

# Example 7 : 

# no_of_cupcakes = int(input(" Enter the number of cupcakes you have:"))
# guest_receive = int(input("Enter the number of cupcakes you want each guest to receive:"))
# invites = no_of_cupcakes / guest_receive 
# print(f"You can invite {invites} guests to your dinner")

# Question 8: 

# You are organizing a charity event to raise money for a cause. Your goal is 
# to collect 100,000 in  donations. If each donor contributes 2500, how many donors
# do you need to reach your fundraising goal? 

# Example 8 : 
# fund_goal = int(input("Enter your fundraising goal :"))
# contribution_amount = int(input("Enter the amount each donor contributes: :"))
# donar = fund_goal / contribution_amount
# print(f"You need {donar}donors to reach your fundraising goal.")





# Other Arth Exercises 

# 1. Write a program that takes input in feet and display in inches. 
# Example 1: 

#  1 feet = 12 inches 

# ft_length = int(input("Please Enter Length in Feet:"))
# inch_length =  ft_length * 12
# print(f"Length in Inches: {inch_length}")

# Example 2: 

#area formula is area = (base * height) / 2

# base= int(input("Enter the base of the triangle "))
# height= int(input("Enter the height of the triangle"))
# triangle_area = (base * height) /2
# print(f"Area of the triangle is {triangle_area}")


# 3. Write a program which takes bits and convert it to bytes. 

# Example 3: 

# 8 bits = 1 Byte
# 1 byte = 8 bits

# no_of_bits = int(input("Enter the number of bits"))
# bytes = no_of_bits / 8
# print(f"No of bytes is {bytes}")

# 4. Write a program which takes bytes and convert it to bits. 

# Example 1: 
# no_of_bytes = int(input(" Enter the number of bytes :"))
# bits = no_of_bytes * 8
# print(f"No of Bits are {bits} ")



#====================================== Another Exercises of Arthematic ================





# Ali’s basic salary is input through the keyboard. His allowance is 40% of basic salary
# and  house rent allowance is 20% of basic salary. Write a program to calculate his
# gross salary. 

#  Example 

# basic_salary = int(input("Enter Basic Salary"))
# allowance = basic_salary * 40 /100
# house_Rent = basic_salary * 20 / 100
# gross_salary = basic_salary + allowance + house_Rent
# print(f"Basic Salary is {basic_salary}")
# print(f"Allowance is {allowance}")
# print(f"House Rent is {house_Rent}")
# print(f"Grosss Salary is {gross_salary}")



# 2. Ali’s basic salary is input through the keyboard. His Entertainment allowance is 10% of basic 
# salary, house medical allowance is 20% of basic salary and overtime allowance is 20% of 
# basic salary. Write a program to calculate his gross salary. 

#  For Example 


# basic_salary = int(input("Enter Basic Salary"))
# medical_allowance = basic_salary * 20 /100
# overtime_allowance = basic_salary * 20 / 100
# entertainment_allowance = basic_salary * 10 / 100
# gross_salary = basic_salary + medical_allowance + overtime_allowance + entertainment_allowance
# print(f"Basic Salary is {basic_salary}")
# print(f"Medical Allowance (20%) is {medical_allowance}")
# print(f"Overtime Allowance (20%) is {overtime_allowance}")
# print(f"Entertainment Allowance (10%)  is {entertainment_allowance}")
# print(f"Grosss Salary is {gross_salary}")



# 3. The distance between two cities (in km.) is input through the keyboard. 
# Write a program to convert and print this distance in meters, feet and centimeters.  

#  For Example 


# 1 KM = 1000M 
# 1 KM = 100000 CM 
# 1 KM = 3280.84 F 


# km_distance = int(input("Distance in Kilometer "))
# m_distance = km_distance * 1000
# cm_distance = km_distance * 100000
# ft_distance = km_distance * 3280.84
# print(f"Distance in meters is {m_distance}")
# print(f"Distance in centimeters is {cm_distance}")
# print(f"Distance in feet is {ft_distance}")


# 4. Take bill amount from user and give 5% discount on bill amount. 

#  For Example :- 


# bill_amount = int(input("Enter bill amount"))
# discount_amount = bill_amount * 10 / 100
# payable_amount = bill_amount - discount_amount
# print(f"Discount amount 5 % is {discount_amount}")
# print(f"Payable Amount  is : {payable_amount}")


# 5. Write a program which takes input loan amount, number of months   and then
# calculate the monthly payment. 

# Example:- 

# loan_amount = int(input("Please Enter Loan Amount: "))
# interest_amount = loan_amount * 10 / 100
# payable_amount = loan_amount + interest_amount
# no_of_install = int(input("Please Enter Number Of Installments "))
# monthly_install = payable_amount / no_of_install
# print(f"Loan Amount is {loan_amount}")
# print(f"Interest Amount (10%) is {interest_amount}")
# print(f"Payable Amount is {payable_amount}")
# print(f"Number of Installments : {no_of_install}")
# print(f"Monthly Installment : {monthly_install}")



