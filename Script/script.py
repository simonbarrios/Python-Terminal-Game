import random

#Card suits & rank declaration
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

#Building the Deck 
deck = []

for suit in suits:
    for rank in ranks:
        deck.append(f"{rank} of {suit}")

random.shuffle(deck)

#This method pop a card from the deck and append into a hand list
def deal_card(deck, hand):
    card = deck.pop()
    hand.append(card)

#This method calculate the value of each card in hand
def calculate_hand_value(hand):
    value = 0
    has_ace = False

    for card in hand:
        rank = card.split()[0]

        if rank.isdigit():
            value += int(rank)
        
        elif rank in ['Jack', 'Queen', 'King']:
            value += 10

        elif rank == 'Ace':
            has_ace = True
            value += 11
        
    if has_ace and value > 21:
        value -= 10

    return value

print("""

                                                                                           
                                                                                           
    ,---,.   ,--,                              ,-.                                    ,-.  
  ,'  .'  \,--.'|                          ,--/ /|                                ,--/ /|  
,---.' .' ||  | :                        ,--. :/ |    .--.                      ,--. :/ |  
|   |  |: |:  : '                        :  : ' /   .--,`|                      :  : ' /   
:   :  :  /|  ' |     ,--.--.     ,---.  |  '  /    |  |.    ,--.--.     ,---.  |  '  /    
:   |    ; '  | |    /       \   /     \ '  |  :    '--`_   /       \   /     \ '  |  :    
|   :     \|  | :   .--.  .-. | /    / ' |  |   \   ,--,'| .--.  .-. | /    / ' |  |   \   
|   |   . |'  : |__  \__\/: . ..    ' /  '  : |. \  |  | '  \__\/: . ..    ' /  '  : |. \  
'   :  '; ||  | '.'| ," .--.; |'   ; :__ |  | ' \ \ :  | |  ," .--.; |'   ; :__ |  | ' \ \ 
|   |  | ; ;  :    ;/  /  ,.  |'   | '.'|'  : |--'__|  : ' /  /  ,.  |'   | '.'|'  : |--'  
|   :   /  |  ,   /;  :   .'   \   :    :;  |,' .'__/\_: |;  :   .'   \   :    :;  |,'     
|   | ,'    ---`-' |  ,     .-./\   \  / '--'   |   :    :|  ,     .-./\   \  / '--'       
`----'              `--`---'     `----'          \   \  /  `--`---'     `----'             
                                                  `--`-'                                   

""")

print("Made by Simon Barrios")

print("\n\nWelcome to Blackjack!")
player_name = input("Please enter your name: ")

while True:
    print("""\n\nGame menu:
        1 - Play Game
        2 - Exit""")

    choice = input("Choice: ")

    if int(choice) == 1:
        player_hand = []
        dealer_hand = []

        deal_card(deck, player_hand)
        deal_card(deck, player_hand)
        deal_card(deck, dealer_hand)
        deal_card(deck, dealer_hand)

        while True:
            print(f"{player_name}'s hand = {player_hand} ({calculate_hand_value(player_hand)})")
            print(f"Dealers hand = [{dealer_hand[0]}, <face down>]")

            if calculate_hand_value(player_hand) > 21:
                print("Player bust!")
                break

            action = input("Do you want hit or stand?: ")

            if action.lower() == "hit":
                deal_card(deck, player_hand)
            else:
                break
        
        print(f"{player_name}'s Hand = {player_hand} ({calculate_hand_value(player_hand)})")
        print(f"Dealer Hand = {dealer_hand} ({calculate_hand_value(dealer_hand)})")

        if calculate_hand_value(player_hand) > 21:
            print("Player bust!")
        elif calculate_hand_value(dealer_hand) > 21:
            print(f"Dealer bust! {player_name} wins!")
        elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
            print("Player wins!")
        elif calculate_hand_value(player_hand) < calculate_hand_value(dealer_hand):
            print("Dealer wins!")
        else:
            print("Push!")

    elif int(choice) == 2:
        print("Thanks for playing!")
        break
    else:
        print("Choose a valid option!")


