# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
#     print(countries)

country = input("Enter a country: ")

while True:

    match country:

        case "Italy":
            print("Ciao")
            break
        case "Germany":
            print("Hallo")
            break
        case "USA":
            print("Hello")
            break
        case "Greece":
            print("Souvlaki")
            break