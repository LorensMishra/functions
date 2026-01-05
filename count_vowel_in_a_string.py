def count_vowel(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count
message = input("Enter a string: ")
print(count_vowel(message))