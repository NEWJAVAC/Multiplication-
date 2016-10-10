import random

def one(round_on=1):
    print("Welcome to round one")
    trails=0
    counter=0
    question=1
    while trails<=11:
        if trails==10:
            if counter>=8:
                print("You got", counter,"out of",trails)
                print("Well, you are going to the next round.")
                round_on= two(round_on=2)
                break
            else:
                ("You got", counter,"out of",trails)
                print("you have failed. Please try again")
                trails=0
                counter=0
                question=1
                print("Welcome back to round one")
                
        else:
            while trails<=9:
                a=random.randint(2,5)
                b=random.randint(2,5)
                print("Question",question)
                print(a,"x", b)
                answer=a*b
                user=(int(input("the answer is:")))
                if answer==user:
                    counter=counter+1
                trails=trails+1
                question=question+1
    return(round_on)

#--------------------------------------------------------------------           
def two(round_on=2):
    print("Welcome to round two")
    trails=0
    counter=0
    question=1
    while trails<=14:
        if trails==13:
            if counter>=10:
                print("You got", counter,"out of",trails)
                print("Well, you are going to the next round.")
                round_on= three(round_on=3)
                break
            else:
                ("You got", counter,"out of",trails)
                print("you have failed. Please try again")
                round_on= one(round_on=1)
                break
                
                
        else:
            while trails<=12:
                a=random.randint(6,9)
                b=random.randint(6,9)
                print("Question",question)
                print(a,"x", b)
                answer=a*b
                user=(int(input("the answer is:")))
                if answer==user:
                    counter=counter+1
                trails=trails+1
                question=question+1
    return(round_on)
#---------------------------------------------------------------------           
def three(round_on=3):
    print("Welcome to round three")
    trails=0
    counter=0
    question=1
    while trails<=19:
        if trails==18:
            if counter>=14:
                print("You got", counter,"out of",trails)
                print("Well. You are smart.")
                exit()
            else:
                ("You got", counter,"out of",trails)
                print("you have failed. Please try again")
                round_on= two(round_on=2)
                break
                
        else:
            while trails<=17:
                a=random.randint(10,13)
                b=random.randint(10,13)
                print("Question",question)
                print(a,"x", b)
                answer=a*b
                user=(int(input("the answer is:")))
                if answer==user:
                    counter=counter+1
                trails=trails+1
                question=question+1               
    return(round_on)


one(1)
two(2)
three(3)
