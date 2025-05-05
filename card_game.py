#code for a card game

import random

print("hello welcome to tricksey battle!")

#have 8 random cards passed out to player 
card_stack = ["2 of Hearts","3 of Hearts","4 of Hearts","5 of Hearts","6 of Hearts"," 7 of Hearts","8 of Hearts","9 of Hearts","10 of Hearts",
              "2 of Clubs","3 of Clubs","4 of Clubs","5 of Clubs","6 of Clubs","7 of Clubs","8 of Clubs","9 of Clubs","10 of Clubs",
              "2 of Diamonds","3 of Diamonds","4 of Diamonds","5 of Diamonds","6 of Diamonds","7 of Diamonds","8 of Diamonds","9 of Diamonds","10 of Diamonds",
              "2 of Spades","3 of Spades","4 of Spades","5 of Spades","6 of Spades","7 of Spades","8 of Spades","9 of Spades","10 of Spades"]
#player 1 stack
player_cards= random.sample(card_stack, k=8)
print("your cards are", player_cards)
#taking the cards our the deck
for s in player_cards:
    split_player_cards= s.split(",")
res=[]
for val in card_stack: 
    if val not in player_cards:
        res.append(val)

#player 2 stack 
player_cards_2= random.sample(res, k=8)
print("Player 2 cards have been dealt")
#taking it out the deck 
for s in player_cards_2:
    split_player_cards_2=s.split(",")
res_2=[]
for val_2 in card_stack:
    if val_2 not in player_cards_2:
        res_2.append(val_2)

#randomly decided player starts the game 
players= ["Player 1", "Player 2"]
score=0
score_2=0
player_choice= random.choice(players)
print(player_choice, "will start the round")

#main gameplay
#for random card to be shown

#card stack must be at least 4 to maintain gameplay
while len(player_cards)>4 and len(player_cards_2) >4:
    #if player 1 starts the round
    if player_choice == "Player 1" or score > score_2:
        card_selection = input("What card would you like to put down? ")
        player_cards.remove(card_selection)
        determining_val_2= card_selection.split(" ")
        print("Player 2 has put down "+ player_cards_2[0])
        determining_val = player_cards_2[0].split(" ")
        player_cards_2.remove(player_cards_2[0])
        #comparing suite values
        if determining_val[2] != determining_val_2[2] and determining_val[0]<determining_val_2[0]:
            print("Congrats you won this round!")
            score= score +1
        elif determining_val[2] == determining_val_2[2] and determining_val[0]< determining_val_2[0]:
            print("you won this round")
            score=score+1
        else:
            print("Sorry, you lost :(")
            score_2=score_2+1
    else:
        #if player 2 starts the round
        print("Player 2 has put down", player_cards_2[0])
        player_cards_2.remove(player_cards_2[0])
            #obtaining information about the suite
        determining_val = player_cards_2[0].split(" ")
            #asking player 1 what they will put down
        card_pick= input("What card will you put down: ")
        determining_val_2= card_pick.split(" ")
        player_cards.remove(card_pick)
            #obtaining information about suite
    if determining_val_2[2] != determining_val[2] and determining_val_2[0]>determining_val[0]:
        print("You won this round!")
        score=score_2+1
    elif determining_val_2[2]==determining_val[2] and determining_val_2[0]>determining_val[0]:
        print("You won this round! ")
        score=score+1
    else:
            print("You lost this round :(")
            score_2=score_2+1
else: 
     additional_cards= random.sample(card_stack, k=4)
     player_cards= player_cards+additional_cards
     player_cards_2=player_cards_2+additional_cards
     print("You have been given 4 more cards, here is your deck: ", player_cards)

#keeping track of points
with open("card_game_results", "a") as write_connection:
            write_connection.write(f"Player 1: {score} \n Player 2:  {score_2}")