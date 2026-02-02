#3. Mathematical Logic
#Question: Write a program to find the sum of all digits of a number (e.g., if input is 123, output is 6).
  

number = 987

total_sum = 0

for digit in str(number):
    total_sum += int(digit)  

print("Total Value", total_sum)