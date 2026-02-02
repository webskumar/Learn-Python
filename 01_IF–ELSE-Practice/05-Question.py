#Take salary as input and print: •	Salary ≥ 50000 → "High Salary" •	Salary between 20000 and 49999 → "Medium Salary" •	Salary < 20000 → "Low Salary"
salary = float(input("Enter your salary: "))
if salary >= 50000:
    print("High Salary")
elif salary >= 20000:
    print("Medium Salary")
else:
    print("Low Salary")
