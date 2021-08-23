answer = 5

print("please guess number between 1 and 10")
guess = int(input())

if guess == answer:
    print("you got it first time")
else:
    if guess < answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done champ, it is correct")
    else:
        print("you made it wrong again")

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
