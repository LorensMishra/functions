def factorial(num):
    if (num < 0):
        return "please enter apositive number"
    elif (num == 0) or (num ==1):
        return 1
    else:
        return num * factorial(num-1)
    
n = int(input("Enter a number: "))
res = factorial(n)
print(f"factorial of {n} is ",res)