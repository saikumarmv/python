import random

highest = 10
answer = random.randint(1, highest)

print("please guess number between 1 and {}".format(highest))
guess = 0

# if guess < answer:
#     print("please guess higher")
#     guess = int(input())
#     if guess==answer:
#         print("well done champ!,you guessed it")
#     else:
#         print("sorry you ran out of chances ")
# elif guess > answer:
#     print("please guess lower")
#     guess = int(input())
#     if guess==answer:
#         print("well done champ!,you guessed it")
#     else:
#         print("sorry you ran out of chances ")
# else:
#     print("what a guess you are champ!")
while guess != answer:
    guess = int(input())
    if guess == answer:
        print("well done champ!,you guessed it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
