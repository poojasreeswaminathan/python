# def containsDuplicate(nums):
#     seen = set()
#     for num in nums:
#         if num in seen:
#             return True
#         seen.add(num)
#     return False
# nums = [1, 2, 3, 1]
# print(containsDuplicate(nums))


# def single_number(nums):
#     result = 0
#     for num in nums:
#         result ^= num  # XOR operation
#     return result

# # Example usage
# nums = [4, 1, 2, 1, 2]
# print("The single number is:", single_number(nums))

# def is_power_of_four(n):
#     if n <= 0:
#         return False
    
#     while n % 4 == 0:
#         n = n // 4
    
#     return n == 1

# num = int(input("Enter a number: "))

# if is_power_of_four(num):
#     print("it is a power of 4")
# else:
#     print("it is NOT a power of 4")


# def is_power_of_Three(n):
#     if n <= 0:
#         return False
    
#     while n % 3 == 0:
#         n = n // 3
    
#     return n == 1

# num = int(input("Enter a number: "))

# if is_power_of_Three(num):
#     print("it is a power of 3")
# else:
#     print("it is NOT a power of 3")

# def is_power_of_Two(n):
#     if n <= 0:
#         return False
    
#     while n % 2 == 0:
#         n = n // 2
    
#     return n == 1

# num = int(input("Enter a number: "))

# if is_power_of_Two(num):
#     print("it is a power of 2")
# else:
#     print("it is NOT a power of 2")



# def max_profit(prices):
#     if not prices:
#         return 0
    
#     min_price = prices[0]  
#     max_profit = 0
    
#     for price in prices:
#         profit = price - min_price
#         if profit > max_profit:
#             max_profit = profit
#         if price < min_price:
#             min_price = price
    
#     return max_profit
# prices_list = [7, 1, 5, 3, 6, 4]
# print("Maximum profit is:", max_profit(prices_list))




# oops

# class student:
#     def detail(self,name,mark):
#         if mark>=45:
#           result="pass"
#           print(result)
#         else:
#             print("fail")
# s1=student()
# s2=student()
# s1.detail("rvs",44)

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_result(self):
#         if self.age<18:
#             print("minor")
#         else:
#             print("major")
# name=input("enter a name:")
# age=int(input("enter a age:"))
# s1=student(name,age)
# s1.show_result()
        
class TemperatureConverter:
    def __init__(self, celsius):
        self.celsius= celsius

    def c_to_f(self):
        for c in self.celsius:
            f = c * (9/5) + 32
            print("f value is:",f)

celsius_values = [0, 20, 37, 100]
converter = TemperatureConverter(celsius_values)
converter.c_to_f()
