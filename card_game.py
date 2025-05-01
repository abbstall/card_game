#code for a card game

import random

print("hello welcome to tricksey battle!")

#have 8 random cards passed out to player 
card_stack = ["Ace of Hearts","2 of Hearts","3 of Hearts","4 of Hearts","5 of Hearts","6 of Hearts"," 7 Hearts","8 of Hearts","9 of Hearts","10 of Hearts","Jack of Hearts","Queen of Hearts","King of Hearts",
              "Ace of Clubs","2 of Clubs","3 of Clubs","4 of Clubs","5 of Clubs","6 of Clubs","7 Clubs","8 of Clubs","9 of Clubs","10 of Clubs","Jack of Clubs","Queen of Clubs","King of Clubs",
              "Ace of Diamonds","2 of Diamonds","3 of Diamonds","4 of Diamonds","5 of Diamonds","6 of Diamonds","7 Diamonds","8 of Diamonds","9 of Diamonds","10 of Diamonds","Jack of Diamonds","Queen of Diamonds","King of Diamonds",
              "Ace of Spades","2 of Spades","3 of Spades","4 of Spades","5 of Spades","6 of Spades","7 Spades","8 of Spades","9 of Spades","10 of Spades","Jack of Spades","Queen of Spades","King of Spades"]
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
print(res)

#player 2 stack 
player_cards_2= random.sample(res, k=8)
print("Your cards are", player_cards_2)
#taking it out the deck 
for s in player_cards_2:
    split_player_cards_2=s.split(",")
res_2=[]
for val_2 in card_stack:
    if val_2 not in player_cards_2:
        res.append(val_2)
print(res_2)

#randomly decided player starts the game 
players= ["Player 1", "Player 2"]
player_choice= random.choice(players)
print(player_choice, "will start the round")

#main gameplay
while len(player_cards) > 4:
    #card stack must be at least 4 to maintain gameplay
    if player_choice == "Player 1":
        card_selection = input("What card would you like to put down?")
        player_cards.pop(card_selection)
        print("Player 2 has put down", player_cards_2[0])
        player_cards_2.pop(0)

    else:
        print("Player 2 has put down", player_cards_2[0])
        #obtaining information about the suite
        for c in player_cards_2[0]:
            determining_val = c.split(" ")
        card_suit= str(determining_val[2])
        #asking player 1 what they will put down
        card_selection= input("What card will you put down:")
        for d in card_selection:
            determining_val_2= d.split(" ")
        card_suite_2= str(determining_val_2[2])
        #obtaining information about suite
        if card_suite_2 != card_suit: 
             #how do I double check if the value of the card is great enough?
             if determining_val_2[0]<determining_val[0]:
                print("you lost this round")
                player_cards.pop(card_selection)
                player_cards_2.pop(0)
        else:
                print("congrats you won the round!")



# have last word of string be found, if the string cannot be found in the player input, have the number be crosschecked, if the number value is greater than first string (1,2,3, etc) 
#the player gets a point for the round


#random card selected to be shown to other player



#what happens if player is down to 4 cards?
# can happen twice in the game




#whatever suite is played first must be followed by the next player
#but if it cannot be followed, a higher suite must be played
#whoever plays the higher suite wins the round, plus 1 point

#that same player starts the next round 