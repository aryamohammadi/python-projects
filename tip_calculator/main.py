print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill?\n"))
tip = int(input("How much tip would you like to give? 10, 12, or 15\n"))
people = int(input("How many people to split the bill?\n"))
total = bill + bill*tip/100
each_person = total/people
round(each_person, 2)
print(f"Each person should pay: {each_person:.2f}")
