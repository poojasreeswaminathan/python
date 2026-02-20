def fizz_buzz(n):
    result = []
    
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    
    return result


# Example usage
print(fizz_buzz(20))



def union_arrays(arr1, arr2):
    return list(set(arr1 + arr2))
arr1=[1,2,3,4]
arr2=[5,6,7,8]
result=union_arrays(arr1, arr2)
print(result)



def reverse_string_swap(s):
    s = list(s)               # string → list
    x = 0
    y = len(s) - 1

    while x < y:
        s[x], s[y] = s[y], s[x]  # swap
        x += 1
        y -= 1

    return ''.join(s)          # list → string

s = "hello"
print(reverse_string_swap(s))  # olleh
