# while True:
#     print("Hello") # infinite loop
user_prompt = "Enter a to-do: "
to_dos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    to_dos.append(todo)