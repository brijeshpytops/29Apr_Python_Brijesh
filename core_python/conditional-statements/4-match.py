import datetime

# Get the current date
current_date = datetime.datetime.now()

# Get the weekday number (Monday is 0, Sunday is 6)
weekday_number = current_date.weekday()
# day = 6

match weekday_number:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3: 
        print("Thursday")
    case 4:
        print("Friday")
    case 5: 
        print("Saturday")
    case 6:
        print("Sunday")
    case _:
        print("Invalid day num.")