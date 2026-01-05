def fun_name(s):
    count = 0
    h = len(s)
    for i in s:
        count += i
    print("sum of numbers",count)

    print("average of this:",count/len(s))

num = list(map(int, input("Enter a number seperated by space: ").split()))
print(fun_name(num))