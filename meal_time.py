def main(): 
    time_in = input("Why don't you tell gram gram the time sweetie? ")

    if ":" not in time_in:
        print("Are you sure this is a time?")
        return   

    else: 

        time_out = convert(time_in)
        
        if time_out >= 7 and time_out <= 8 or time_out >= 19 and time_out <= 20:
            print ("Breakfast Time")
        elif time_out >= 12 and time_out <= 13 or time_out >= 24 and time_out <= 25:
            print ("Lunch Time")
        elif time_out >= 6 and time_out <= 7 or time_out >= 18 and time_out <= 19:
            print ("Dinner Time")
        else:
            print ("Stop eating")


def convert(time):
        Hour, Minute = time.split(":")
        Minute = int(Minute)
        Hour = int(Hour)
        if Minute < 0 and Minute > 59:
            return print("USE EARTH TIME YA ALIEN! (0 to 59 minutes)")
        else:
            Minute = int(Minute) / 60
            # MUnnecesary for "minute = eval(Minute)""
            return Hour + Minute


if __name__ == "__main__":
    main()
