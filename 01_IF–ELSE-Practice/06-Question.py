# Tax Calculator (India – Simplified) Income ≤ 2.5L → No tax, 2.5L–5L → 5%, 5L–10L → 20%, Above 10L → 30%,  Senior citizen gets 5% rebate
income = float(input("Enter your annual income in INR: "))
age = int(input("Enter your age: "))
tax = 0
if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = 0.05 * (income - 250000)
elif income <= 1000000:
    tax = 0.05 * 250000 + 0.20 * (income - 500000)
else:
    tax = 0.05 * 250000 + 0.20 * 500000 + 0.30 * (income - 1000000)
if age >= 60:
    rebate = 0.05 * tax
    tax -= rebate
print(f"The calculated tax is: INR {tax:.2f}")
