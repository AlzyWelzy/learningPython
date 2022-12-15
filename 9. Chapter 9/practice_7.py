content = True
i = 1

with open("9. Chapter 9/essay.txt") as f:
    while content:
        content = f.readline()
        if "python" in content.lower():
            print(content)
            print(f"Yes python is in the file at index {i}")
        i += 1
