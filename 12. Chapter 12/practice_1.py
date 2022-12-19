try:
    with open("9. Chapter 9/abarakadabra.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("ERROR!")

try:
    with open("9. Chapter 9/abarakadabra 2.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("ERROR!")


try:
    with open("9. Chapter 9/3. error.txt", "r") as f:
        print(f.read())
except Exception as e:
    print("ERROR!")
