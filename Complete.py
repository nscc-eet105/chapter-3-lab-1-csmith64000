print("Workday Translator")
day = int(input("Enter the numeric value of the day you wish to work:"))
if day== 1:
    day = "Monday"
elif day==2:
    day = "Tuesday"
elif day== 3:
    day = "Wednesday"
elif day==4:
    day = "Thursday"
elif day==5:
    day = "Friday"
elif day== 0:
    day = "Weekend"
else:
    print("Invalid")
    day = "Invalid"

print(("The workday is"), day)

print("Chris smith")
print("Chapter 3 Lab 1")
print("6/16/2025")
