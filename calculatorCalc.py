def main():

    answer = (input("Wibbly-Wobbly Timey-Wimey Calculator Stuff? "))
   
    if ("/0") in answer or ("/ 0") in answer:
        print("Invalid Input, don't EVER do that again <3")

    else:
        try: Num1, Symbol, Num2 = answer.split(" ")

        except (SyntaxError, NameError, ValueError, TypeError):
            try: answer2 = eval(answer) # MOVE THIS TO THE OPTHER AREA

            except (SyntaxError, NameError, ValueError, TypeError):
                print ("USE SYMBOLS AND DIGITS ONLY!?")
                return

            print (answer2)
            return
            

        if "+" in Symbol or "-" in Symbol or "*" in Symbol or "/" in Symbol and (Num1.isdigit and Num2.isdigit):
            answer2 = eval(answer)
            print (answer2)

        else:
            print ("No ablo ingless?")


main()