
import random
score = 300
def play():
    choose_1 = random.randint(1,13)
    print(f"The card is: {choose_1} ")
    high_lower = input("Higher or Lower? [h/l]:  ")

    choose_2 = random.randint(1,13)
    print(f"Next card was: {choose_2} ")


    if high_lower == "h":
        if choose_1 < choose_2:   
            total_score = score + 100
        else:
            total_score = score - 75     
    elif high_lower == "l":      
        if choose_1 > choose_2:   
            total_score = score + 100
        else:
            total_score = score - 75   
    print(f"Your score is: {total_score}")
    if total_score == 0:
        print("Game Over")
    play_again = None
    play_again=input("Play again [y/n]: ")
    if play_again =="y":
        play()
    if play_again =="n":
        print("Thank you for playing!")

play()