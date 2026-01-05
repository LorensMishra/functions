def square_qube(num):
    res = num**2
    res_cube = num**3
    return f"square of number {num}",res,"and cube is",res_cube
n = int(input("Enter a number: "))
print(square_qube(n))        
        