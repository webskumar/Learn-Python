#3. Mathematical Logic
#Question: Write a program to find the sum of all digits of a number (e.g., if input is 123, output is 6).
  

number = 123

total_sum = 0


for digit in number:
    total_sum += int(digit)  # अंक को वापस integer में बदलकर जोड़ना

print("अंकों का कुल योग है:", total_sum)