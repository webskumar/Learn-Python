#04 Take temperature as input and print: •	Above 30 → "Hot" •	Between 20 and 30 → "Normal" •	Below 20 → "Cold"


temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 30:
    print("Hot")
elif temperature < 30 and temperature >= 20:
    print("Normal")
else:
    print("Cold")