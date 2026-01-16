todos = []

while True:
    user_action = input("Type add,show or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo) #after this it goes in user_action
        case 'show':
            print(todos)#after this it goes in user_action
        case 'exit':
            break #breaks the loop


# while True:
#
#     match country:
#
#         case "Italy":
#             print("Ciao")
#             break
#         case "Germany":
#             print("Hallo")
#             break
#         case "USA":
#             print("Hello")
#             break
#         case "Greece":
#             print("Souvlaki")
#             break