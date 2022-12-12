userMarks = float(input("Enter your Marks: "))

# if (userMarks < 50):
#     print("You failed with F Grade")
# elif (userMarks > 50 and userMarks <= 60):
#     print("You passed with D Grade")
# elif (userMarks > 60 and userMarks <= 70):
#     print("You passed with C Grade")
# elif (userMarks > 70 and userMarks <= 80):
#     print("You passed with B Grade")
# elif (userMarks > 80 and userMarks <= 90):
#     print("You passed with A Grade")
# elif (userMarks > 90 and userMarks <= 100):
#     print("You passed with Ex Grade")

grade = None

if userMarks >= 90:
    grade = "Ex"
elif userMarks >= 80:
    grade = "A"
elif userMarks >= 70:
    grade = "B"
elif userMarks >= 60:
    grade = "C"
elif userMarks >= 50:
    grade = "D"
elif userMarks < 50:
    grade = "F"

print(f"Your grade is {grade}")
