from sys import argv
script , user_name , user_age = argv
prompt = '->'

print(f"Hi {user_name}, I'm the {script} script")
print(f"You are {user_age} old isn't?")

print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright , so you said {likes} about me.
You live in {lives} .Not sure where that is.
And you have a {computer} computer . Nice.
""")
