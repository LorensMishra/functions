def len_string(s):
    count = 0
    for ch in s:
        count += 1
    return count
message =input("Enter your message: ")
print(len_string(message))    
    