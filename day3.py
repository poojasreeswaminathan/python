# n = int(input("Enter how many numbers: "))

# a = 0
# b= 1

# print(a)
# print(b)

# for i in range(2, n):
#     c = a+ b
#     print(c)
    
#     a= b
#     b= c





# a=[1,2,3,4,5]
# b=[1,2,3,4,5,6,7]
# print(a[3])
# print(b[0:6])
# print(a+b)
# print(a*3)
# print("9" in a)
# print("10" not in b)
# print(a==b)
# print(a>b)
# print(a<b)
# a.append(6)
# print(a)
# b.insert(4,9)
# print(b)
# a.extend(b)
# print(a)
# b.remove(5)
# print(b)
# a.pop(3)
# print(a)
# a.clear()
# print(a)
# print(b.index(7))
# c=[5,6,3,8,9]
# c.sort()
# print(c)
# c.sort(reverse=True)
# print(c)


# a=[1,2,4]
# b=[5,6,7]
# c=lambda: a+b
# print(c())

# gp=[2,3,4,8]
# pg=list(map(lambda y:y*2,gp))
# print(pg)

# gp = [2, 3, 4, 8]
# def multiply(y):
#     return y * 2
# pg = list(map(multiply, gp))
# print(pg)  

# gp=[2,3,4,8]
# pg=list(filter(lambda y:y%2==0,gp))
# print(pg)

# gp = [2, 3, 4, 8]
# def multiply(y):
#     return y%2==0
# pg = list(filter(multiply, gp))
# print(pg)  


# from functools import reduce
# a=[3,6,9,2,3]
# c=reduce(lambda b,d:b+d,a)
# print(c)

# from functools import reduce
# a=[1,2,3,4,5,6,7,8,9,10]
# b=list(filter(lambda y:y%2==0,a))
# print(b)
# c=reduce(lambda d,e:d+e,b)
# print(c)


# from functools import reduce
# a=[1,2,3,4,5,6,7,8,9,10]
# b=list(filter(lambda y:y%2==1,a))
# print(b)
# c=reduce(lambda d,e:d+e,b)
# print(c)

# # pallindrome using slicing
# word=input("enter a word:")
# if word==word[::-1]:
#     print("palindrome")
# else:
#     print("not pallindrome")

# not using slicing

# word=input("enter a word:")

# for ch in word:
#     rev=ch+rev
# if word==rev:
#     print("palindrome")
# else:
#     print("not pallindrome")

# word=int(input("enter a word:"))
# rev=0
# for ch in word:
#     rev=ch+rev
# if word==rev:
#     print("palindrome")
# else:
#     print("not pallindrome")


# a= int(input("enter a num"))
# b=int(input("enter a num"))
# if(len(a)==len(b)):
#     n=(sorted(a))
#     m=(sorted(b))
#     if(n==m):
#         print("anagram")
#     else:
#         print("not anagram "


def is_happy(n):
    seen = set()

    while n != 1:
        if n in seen:
            return False
        
        seen.add(n)

        total = 0
        while n > 0:
            digit = n % 10
            total += digit * digit
            n //= 10

        n = total

    return True
num = int(input("Enter a number: "))

if is_happy(num):
    print("Happy Number")
else:
    print("Not a Happy Number")
