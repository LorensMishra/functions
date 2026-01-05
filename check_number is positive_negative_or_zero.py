def check(num):
    if num == 0:
        return "Zero"
    elif num < 0:
        return "Negative Number"
    else:
        return "Positive number"
n = int(input("Enter a number: "))
print(check(n))