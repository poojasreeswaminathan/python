# for i in range(1,100):
#  if(i%3 ==0):
#   print("fizz")
#  elif (i%5 ==0):
#   print("buss")
#  else:
#   print(i)
# _apple=10
# print(_apple)
# Apple123=10
# print(Apple123)


# DATATYPES
# int,float,str,bool



# current_year = 2026  
# birthyear = int(input("Enter your birth year: "))
# age = current_year - birthyear
# print(age)


# current_age = int(input("Enter your current age: "))
# maxage = int(input("Enter your maximum expected age: "))
# waterperday = float(input("How many liters you drink per day "))
# years_left = maxage - current_age
# print(years_left )
# days_left = years_left * 365
# print(days_left )
# total_water_left = waterperday*days_left
# print(total_water_left)


# distance=int(input("enter"))
# carmile=int(input("enter a mileage"))
# petrol=int(input("petrol price per day"))
# fuel_needed=distance/carmile
# print(fuel_needed)
# total_cost=fuel_needed*petrol
# print(total_cost)



# datausage=int(input("enter a useage"))
# total_days=int(input("enter"))
# monthly_usage=datausage*total_days
# print(monthly_usage)
# current_age=int(input("enter a age"))
# years_to_days=current_age*365
# print(years_to_days) 

# price=int(input("enter"))
# discount=int(input("enter a discount"))
# decimal = discount/ 100
# print(decimal)
# discount_amount = (discount / 100) * price
# print(discount_amount)
# final_price = price - discount_amount
# print(final_price)


# x=int(input("enter a num"))
# y=int(input("enter a num"))
# if(x==y):
#     print("equal")
# elif(x>y):
#    print("x is greater than y")
# else:
#     print("x is less than y")


# a=input("enter a letter")
# if(a="a"or a="e" or a="i" or a="0"or a="u"):
#  print("vowels")
# else:
#  print("cons")   
    

# mark=int(input("enter a num"))
# if(mark==100):
#     print("s")
# elif(mark<100 and mark>=90):
#     print("A")
# elif(mark<90 and mark>=80):
#     print("B")
# elif(mark<80 and mark>=70):
#     print("C")
# elif(mark<70 and mark>=60):
#     print("D")
# elif(mark<60 and mark>=50):
#     print("E")
# elif(mark>100):
#     print("invalid")
# else:
#     print("f")


# x=float(input("enter a num"))
# y=float(input("enter a num"))
# if x > y:
#     print("Profit ", x - y)
# elif x > y:
#     print("Loss ", x - y)
# else:
#     print("No profit, no loss")



# student_type=input("enter a type:")
# fee=int(input("enter a fee:"))
# hostelfee=int(input("enter a hostel fee:"))
# total_fee=(fee+hostelfee)
# print("the fees to be paid is",total_fee)



# LOOP
# total = 0

# for i in range(1, 101):
#     if i % 2 != 0:         
#         print(i)
#         total += i

# print("Sum of odd numbers:", total)



# total = 0

# for i in range(1, 101):
#     if i % 2 == 0:         
#         print(i)
#         total += i

# print("Sum of even numbers:", total)


# for i in range(1, 11):         
#         a=i*5
#         print(i ,"*5=",a)

# tamil=int(input("enter a mark"))
# maths=int(input("enter a mark"))
# physics=int(input("enter a mark"))
# chem=int(input("enter a mark"))
# science=int(input("enter a mark"))
# total=(tamil+maths+physics+chem+science)
# print("total",total)
# average=((tamil+maths+physics+chem+science)/5)
# print("average:",average)

# a = 5

# for i in range(1, a+ 1):
    # print("*" * i)

# a = 5

# for i in range(a, 0, -1):
#     print("*" * i)



# total = 0
# i = 1

# while i <= 100:
#     if i % 2 != 0:
#         print(i)
#         total += i
#     i += 1

# print("Sum of odd numbers:", total)


# total = 0
# i = 1

# while i <= 100:
#     if i % 2 == 0:
#         print(i)
#         total += i
#     i += 1

# print("Sum of even numbers:", total)

# i = 1

# while i <= 10:
#     a = i * 5
#     print(i, "*5 =", a)
#     i += 1

# i = 1
# total = 0

# while i <= 5:
#     if i == 1:
#         tamil = int(input("Enter marks for Tamil: "))
#         total += tamil
#     elif i == 2:
#         maths = int(input("Enter marks for Maths: "))
#         total += maths
#     elif i == 3:
#         physics = int(input("Enter marks for Physics: "))
#         total += physics
#     elif i == 4:
#         chem = int(input("Enter marks for Chemistry: "))
#         total += chem
#     elif i == 5:
#         science = int(input("Enter marks for Science: "))
#         total += science
#     i += 1

# average = total / 5
# print("Total:", total)
# print("Average:", average)


# a = 5
# i = 1

# while i <= a:
#     print("*" * i)
#     i += 1

# a = 5
# i = a

# while i > 0:
#     print("*" * i)
#     i -= 1
seats = ["O"] * 5

for i in range(5):
    if seats[i] == "O":
        name = input("Enter passenger name: ")
        seats[i] = name
        print("Seat", i+1, "booked for", name)

if "O" not in seats:
    print("All seats are booked")







