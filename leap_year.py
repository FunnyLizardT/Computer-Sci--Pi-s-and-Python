def main():

    year = (input("Is this year is a leap year doc? "))

    Year = int(year)



    if Year % 400 == 0 and Year % 100 == 0 and Year % 4 ==0:

          print ("It's a leap year!")
          return

    elif Year % 400 != 0 and Year % 100 != 0 and Year % 4 ==0:

          print ("It's a leap year!")
          return
    else:
        print ("GREAT SCOTT, IT'S NOT A LEAP YEAR!? ")

























main()