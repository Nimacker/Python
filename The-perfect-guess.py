import random
def ask_user():
    user_ask1=int(input("Guess the 4-digit number \n>>> "))
    return (user_ask1)
def num_gen():
    num1=random.randint(1000,9999)
    return num1
def game_on(num1):
    cows, bulls = 0,0
    num2=ask_user()
    while(1):
        if(num1==num2):
            cows+=1
            print("right guess:", cows, "   ", "wrong guess:", bulls)
            print("You guessed correctly..GameOver")
            break
        else:
            bulls+=1
            print("right guess:",cows,"   ","wrong guess:",bulls)
            num2=ask_user()
            if bulls>9:
                break
            else:
                continue

print("Welcome to cows and bulls game!!!!")
numgen=num_gen()
game_on(numgen)