def main():

    answer = (input("What is the answer to life, the universe, and everything? "))
    if answer.isdigit():
        
            #make into int and then detect for math

        answer2 = int(answer)

        if answer2 == 42:
            print ("Correct")
                        
        else:
            print ("Wrong")

    elif("1" in answer or "2" in answer or "3" in answer or "4" in answer or "5" in answer or "6" in answer or "7" in answer or "8" in answer or "9" in answer or "0" in answer) and ("+" in answer or "-" in answer or "*" in answer or "/" in answer):

        try:
            answer2 = eval(answer)
        except (SyntaxError, NameError, ZeroDivisionError, TypeError):
            print ("wrong")
            return
    
        if answer2 == 42:
            print ("Correct")
            
        else:
            print ("Wrong")
            

    else:
        answer2 = (answer).lower
        #if not int, make it into .lower and check for uh spelling

        if "fourty two" in answer2() or "fourty-two" in answer2() or "42.0" in answer2() or "fourtytwo" in answer2()or "forty two" in answer2() or "forty-two" in answer2() or "cuarenta y cuatro" in answer2() or "fortytwo" in answer2():
            print ("Correct")

        else:
            print("Wrong")



main()




