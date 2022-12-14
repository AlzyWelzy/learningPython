# import math

marks = [12, 12, 3, 4, 214, 5, 12, 35, 43, 1, 5, 2, 3, 234]

# marksAvg = math.ceil(sum(marks)/len(marks))
# marksAvg = math.floor(sum(marks)/len(marks))
# marksAvg = math.trunc(sum(marks)/len(marks))

marksAvg = round(sum(marks)/len(marks), 2)

print(marksAvg)
