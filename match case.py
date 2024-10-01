#match_case
choice = int(input("Input No from 1 to 7 : "))

match choice:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("SUnday")
    case _:
        print("Invalid Input")
