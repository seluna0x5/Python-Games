import random
price = random.randint(1,10)
score = 100
attempt = 0
print("Guess the right price! The price is a number between 1 and 10 inclusive.")
while True :
    attempt +=1
    number=int(input())
    if (number<1 or number>10) :
        print("you must choose a number between 1 and 10")
    else :
        if number<price :
            print("the price is lower")
        elif number>price :
            print("the price is higher")
        else :
            print(f"Congratulations, you have found the right price {price} in {attempt} attempts, your score is {(score/attempt) : .2f}")
            break
    