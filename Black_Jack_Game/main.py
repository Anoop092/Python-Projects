import random
import sys
def card_points():
    card_points = {"A": 11,2: 2,3 : 3,4 : 4, 5 : 5,6 : 6,7 : 7,8 : 8,9 : 9, 10 : 10,"J": 10,"K": 10,"Q": 10}
    return card_points

# Game variables
player_cards = []
delear_cards = []
start_game = False

# Delars draw the card from set of card
def draw_cards():
    cards = card_points()
    cards = list(cards.keys())
    return random.choice(cards)
# calculates the scores
def get_scores(cards):
    card_point = card_points()
    sum = 0
    for card in cards:
        sum += card_point[card]
    return sum
# printing final scores
def print_final_scores(player_cards,player_score,delar_scores,delar_cards ):
    print(f"Your final hand : {player_cards} , your final Score : {player_score}")
    print(f"Your Delars hand : {delar_cards} , final Score : {delar_scores}")
    sys.exit()


def get_results(player_cards, delar_cards,flag="n"):
    player_score = get_scores(player_cards)
    delars_score = get_scores(delar_cards)
    if player_score == 21 and len(player_cards) == 2:
        print("You won with Black jack")
        print_final_scores(player_cards,player_score,delars_score,delar_cards)
    if delars_score == 21 and len(delar_cards) == 2:
        print("You loose ,your dealer won with Black Jack")
    if player_score > 21 and "A" in player_cards:
        player_score  = player_score - 11 + 1
    if delars_score > 21 and "A" in delar_cards:
        delars_score = delars_score - 11 + 1
    if player_score > 21:
        print("Oops you Loose you went over")
        print_final_scores(player_cards,player_score,delars_score,delar_cards)
    elif delars_score > 21:
        print("You won the delar went over")
        print_final_scores(player_cards,player_score,delars_score,delar_cards)
    if flag == 'n' or flag == 'no':    
        if player_score >  delars_score:
            print("Congratulation  you won")
            print_final_scores(player_cards,player_score,delars_score,delar_cards)
        elif delars_score > player_score:
            print("Oops you Loose ")
            print_final_scores(player_cards,player_score,delars_score,delar_cards)
        else:
            print("It's Draw ")
            print_final_scores(player_cards,player_score,delars_score,delar_cards)
    
            
        
    
# Delar distubutes the card after drawing the card
def add_cards(cards):
    card = draw_cards()
    if card in cards:
        add_cards(cards)
    else:
        cards.append(card)
for i in range(0,2):
    add_cards(player_cards)
    add_cards(delear_cards)



#Game begins
player_input = input("Do you want to play Blackjack, if yes then 'y', if no then 'n':  ").lower()

if player_input == 'y' or player_input == 'yes':
    start_game = True
else:
    sys.exit("Thank you for playing")

while start_game:
    print(f"your cards {player_cards}", f"Current score is: {get_scores(player_cards)}")
    print(f"Delar's first card is : {delear_cards[0]}")
    player_input = input("Do you want to draw the card type 'y' for yes or 'n' for no :  ").lower()
    if player_input == 'n' or player_input == 'no':
        while get_scores(delear_cards) < 17:
            add_cards(delear_cards)
        get_results(player_cards,delear_cards,player_input)
    elif player_input == 'y' or player_input == "yes":
        add_cards(player_cards)
        get_results(player_cards,delear_cards,player_input)
        

        



    





