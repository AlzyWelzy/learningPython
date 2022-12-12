# myDict = {
#     "Fast": "In a Quick Manner", "Alzy": "A Programmer", "Marks": [1, 3, 5], "anotherDict": {"Alzy": "Player"}
# }

myDict = {
    "fast": "In a Quick Manner",
    "alzy": "A Programmer",
    "marks": [1, 3, 5],
    "anotherDict": {"alzy": "Player"},
    1: 3
}

# print(myDict["Fast"])
# print(myDict["Alzy"])
# print(myDict["anotherDict"]["Alzy"])
# myDict["Marks"] = [45, 78]
# print(myDict["Marks"])
# print(myDict["anotherDict"]["Alzy"])

print(myDict.keys())  # Print the keys of the dictionary
print(myDict.values())  # Print the values of the dictionary

print(type(myDict.keys()))  # Print the type of keys of the dictionary
print(type(myDict.values()))  # Print the type of values of the dictionary

print(list(myDict.keys()))
print(list(myDict.values()))

print(myDict[1])

print(myDict.items())

print(myDict)

updateDict = {"wife": "Pratibha",
              "mistress": "Prema"}

print(myDict.update({"friends": "Sum"}))
print(myDict.update(updateDict))

print(myDict)

print(myDict["fast"])

a = myDict["fast"]
print(a)

print(myDict.get("fast"))

b = myDict.get('fast')
print(b)

print(myDict.get("Alzy"))  # Prints value associated with key "Alzy"
print(myDict["Alzy"])  # Prints value associated with key "Alzy"

# The difference between .get and [] syntax in Dictionaries
# Returns None as "Alzy2" is not present in the dictionary
print(myDict.get("Alzy2"))
# Throws an Error as "Alzy2" is not present in the dictionary
print(myDict["Alzy2"])
