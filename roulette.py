import random


money = 50
losses = 0



def roulette_sim():
    print ("How much do you want to bet?")
    bet = raw_input("> ")
    bet = int(bet)
if bet > money:
        bet_too_much()
    else:
        red_or_black()



def bet_too_much():
    print ("You do not have all that money. Please bet again.") 
    raw_input("Press ENTER to continue> ")
    roulette_sim()


def red_or_black():
    print("OK, you bet ") %  (bet)
    print("Red or black?")
    answer = raw_input(" ")
    number = random.randint(1, 2)
    if number == 1 and answer == "red":
        print("You win!")
        money += bet
        print("You now have  money") % (money)
        print("Your losses are ") % (losses)
        replay()
    elif number == 2 and answer == "black":
        print("You win!")
        money += bet
        print("You now have  money") % (money)
        print("Your losses are ") % (losses)
        replay()
    else:
        print("You lost!")
        money -= bet
        losses += bet
        print("You now have  money") % (money)
        print("Your losses are ") % (losses)
        replay()


def replay():
    print("Do you want to play again?")
    play_again = raw_input("y/n")
    if play_again == "y":
        roulette_sim()
    else:
        print("OK, bye!")


roulette_sim()
