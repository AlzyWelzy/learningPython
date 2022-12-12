# ?/100
maths = float(input("Enter your Marks in Mathematics: "))
science = float(input("Enter your Marks in Science: "))
literature = float(input("Enter your Marks in Literature: "))
total = (maths+science+literature)/3

if (total >= 40 and maths >= 33 and science >= 33 and literature >= 33):
    print("You passed!")
else:
    print("You failed")
