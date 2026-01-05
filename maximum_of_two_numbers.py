def maximum(a,b):
    if a > b:
        return "a is largest",a
    else:
        return "b is largest",b
# take user input two numbers
n = int(input("Enter a first number: "))
m = int(input("Enter a second number: "))
print(maximum(n,m))