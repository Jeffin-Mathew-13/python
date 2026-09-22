import random


print("1.Guessing Number")
print("2.Multiplication Table")
print("3.BMI Calculator")


choice=int(input("enter your choice:"))


if choice==1:

    print("Guessing Game\nGuess a number between 1 and 10")
    s_num=random.randint(1,10)
    attempts=3
    while attempts > 0:
        print("enter your guess:")
        num = int(input())
        if num < 1 or num > 10:
            print("enter valid guess number between 1 and 10")
            attempts=attempts-1
            continue
        elif num == s_num:
            print("Correct Guess")
            break
        elif num > s_num:
            print("Incorrect Guess Think Lower")
            attempts=attempts-1
            print("try again attempts remaining:",attempts)
        elif num < s_num:
            print("Incorrect Guess Think Upper")
            attempts=attempts-1
            print("try again attempts remaining:",attempts)
        else:
            print("Incorrect Guess")
            attempts=attempts-1
            print("try again attempts remaining:",attempts)
    else:
        print("GAME OVER\nBETTER LUCK NEXT TIME")
        print("The number was : ",s_num)
        print("Thank you for playing")

elif choice==2:

    print("Multiplication Table")
    print("enter the number for multiplication table")
    m_num=int(input())

    print("multiplication table of",m_num)

    for i in range(1,11):
        p_num=m_num*i
        print(m_num,"x",i,"=",p_num)

    print("multiplication table finished")


elif choice==3:

    print("BMI Calculator")
    print("enter your weight in kg")
    weight=float(input())
    print("enter your height in m")
    height=float(input())

    def calc_bmi(weight,height):
        bmi=weight/(height*height)
        return bmi

    print("Your BMI is",calc_bmi(weight,height))


else:

    print("INVALID CHOICE")



