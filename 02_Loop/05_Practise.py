#5. Intermediate Challenge
#Question: Write a program to reverse a number using a loop (e.g., 1234 becomes 4321).
num = 1234
reverse = 0
while num > 0:
    reverse = (reverse * 10) + (num % 10)
    num //= 10
print(reverse)
