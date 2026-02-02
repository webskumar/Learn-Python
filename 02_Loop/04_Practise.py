#4. Loop Control (Break/Continue) 
#Question: Iterate through a list of names and stop the loop immediately if you find the name "Python".
names = ["Java", "C++", "Ruby", "Python"]
for i in names:
    if i == "Python":
        break
    print(i)