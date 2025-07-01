import random
def card_deck():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    """Takes a list of cards and returns the total score from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0  #Blackjack
    if 11 in cards and sum(cards)>21:   #If 11 is there and sum>21 this removes 11 and replaces it with 1
        cards.remove(11)
        cards.replace(1)
    return sum(cards)
def compare(u_score, c_score):
    if u_score==c_score:
        return "Draw"
    elif u_score==0:
        return "You won with blackjack"
    elif c_score==0:
        return "You lose and opponent wins"
    elif u_score>21:
        return "You went over so you lose"
    elif c_score>21:
        return "Opponent went over. You win"
    elif u_score>c_score:
        return "You win"
    else:
        return "You lose"
def play_game():
    user_cards=[]
    computer_cards=[]
    user_score=-1   #Initializing score with -1 cause 0 is the condition for blackjack
    computer_score=-1
    is_game_over=False
    for _ in range(2):
        user_cards.append(card_deck())  
        computer_cards.append(card_deck())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your card: {user_cards}, your score: {user_score}")
        print(f"Computer's first cards: {computer_cards[0]}")
        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_choice=input("Type 'y' to get another card or type 'n' to pass: ").lower()
            if user_choice=="n":
                is_game_over=True
            else:
                user_cards.append(card_deck())
    while computer_score!=0 and computer_score<21:
        computer_cards.append(card_deck())
        computer_score=calculate_score(computer_cards)
        print(f"Final hand is {user_cards}, final score is {user_score}")
        print(f"Computer's final hand {computer_cards}, final score {computer_score}")
        print(compare(user_score, computer_score))
    while input("Do you want to play blackjack game ? Type 'y' for yes or 'n' for no")=="y":
        print("\n"*20)
        play_game()
