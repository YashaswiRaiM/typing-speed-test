from time import *
import random as r

def mistake(paratest,usertest):
    error=0
    for i in range(len(paratest)):
        try:
            if paratest[i]!=usertest[i]:
                error +=1
        except:
            error +=1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)

if __name__ == '__main__' :

    while True:
        ck=input("Ready to test? yes/no : ").lower()
        if ck == "yes":
            test=["A paragragh is a self contained unit of discourse in writing dealing with a particular point or idea.",
                "My name is Yashaswi Rai M.",
                "Welcome to Typing test."]

            test1=r.choice(test)
            print("          *****Typing Speed*****")
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input(" Enter : ")
            time_2=time()

            print(" Speed : ", speed_time(time_1,time_2,testinput)," W/Sec ")
            print(" Error : ",mistake(test1,testinput))

        elif ck=="no":
            print("Thank you ")
            break

        else:
            print("Check Your Input and Try Again")
