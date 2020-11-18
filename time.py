def time_of_the_day():
    name = input("ENTER A NAME PLEASE: ")
    print("Your name is",name)
    clock = int(input("whats says the time? "))
    if clock >=0 and clock <=12:
        print("GOOD MORNING")
    elif clock >=13 and clock <=16:
        print("GOOD AFTERNOON")
    elif clock >=17 and clock <=20:
        print("GOOD EVENING")
    elif clock >=21 and clock <=24:
        print("GOOD NIGHT")
    else:
        print("WRONG INPUT")

time_of_the_day()