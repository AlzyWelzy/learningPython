from datetime import date
name = input("Enter your Name: ")
today = date.today()
_date = today.strftime("%d/%m/%Y")
letter = '''Dear <|NAME|>,
Greetings from AlzyWelzy Coding House.
I'm very happy to tell you about your selection.
You are selected!
Have a great day ahead.
Thanks and regards,
WelzyAlzy
Date: <|DATE|>'''
# letter = f"Dear {name}\n\tYou are selected!\n\tDate: {_date}"
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", _date)
print(letter)
