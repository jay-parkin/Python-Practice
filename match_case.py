# Match Case - Switch Case
# 0 - Monday
# 1 - Tuesday
# 2 - Wednesday
# ...

day = 2

match day:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2:
        print("Wednesday")
    case 3:
        print("Thursday")
    case _:
        print("Invalid data")