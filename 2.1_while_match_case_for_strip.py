todos = []

while True:
    user_action = input("Type add,show,remove or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo) #after this it goes in user_action
        case 'show' | 'display': # OR
            for item in todos:
                item = item.title() # capitalize first letter
                print(item)
        case 'remove':
            print(todos)
            print("You removed the last todo")
            todos.pop(-1) #removes the last item that we added
            print(todos)
        case 'exit':
            break #breaks the loop
        case user_types_whatever: # in case user writes whatever , case understands on the fly to print please dont type random things
            print("Please don't type random things")


#strip method can help here , the program is more intelligent with spaces
#user_action = user_action.strip()