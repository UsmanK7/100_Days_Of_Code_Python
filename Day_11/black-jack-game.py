import random
import sys

if input("Do you want to black-jack game made by usman? Type 'y' for yes and 'n' for no")=="y":
    #all functions 
    def deal_card():
        '''this functions will return a random card'''
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    print('''
    
     _     _            _    _            _    
    | |   | |          | |  (_)          | |   
    | |__ | | __ _  ___| | ___  __ _  ___| | __
    | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   <| | (_| | (__|   < 
    |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                        _/ |                
                        |__/                
    
    ''')

    # start

    # in start both user and computer will have zero cards
    user_cards=[]
    computer_cards=[]

    # the user and computer each get two random cards
    new_card=deal_card()
    user_cards.append(new_card)
    for _ in range(0,2):
        new_card=deal_card()
        computer_cards.append(new_card)

    #initialize again with True value
    again=True
    while(again==True):
        new_card=deal_card()
        user_cards.append(new_card)
        print(f"your cards {user_cards}")

        # sum both user and computer total cards

        print("your total sum -> "+str(sum(user_cards)))

        computer_total=sum(computer_cards) 

        if(sum(user_cards)>21):
            print("Oh Snap! your score exceeded 21 so you lost")
            exit()

        # check if the user or computer has black jack or not
        if 11 in computer_cards and 10 in computer_cards and len(computer_cards)==2:
            print("Snap computer have a black jack so you lost :(")
            exit()

        if 11 in user_cards and 10 in user_cards and len(user_cards)==2:
            print("Congrats You have a black jack so you win!")
            exit()

        # if an ace is drawn,count it as 11 but if the total goes above 21 then count it as 1
        if 11 in user_cards and sum(user_cards)>21:
            user_cards.remove(11)
            user_cards.append(1)

        # reveal computer's first card
        print("computer's hand :"+str(computer_cards[0]))

        if input("Do you want an another card type 'y' for yes and 'n' for no : ")=="y":
            continue
        else:
            again=False

    while(computer_total<17):
        new_card=deal_card()
        computer_cards.append(new_card)
        computer_total=sum(computer_cards)

    if(computer_total>21):
        print(f"computer final hand {computer_cards}")
        print(f"your final hand {user_cards}")
        print("congrats! computer score exceeded 21 so you win! ")
        exit()
    else:
        #if the computer score is more then user score computer wins
        if(computer_total>sum(user_cards)):
            print(f"computer final hand: {computer_cards}")
            print("snap! you lose computer win")
            exit()

        #if the computer score is less then user score user wins
        elif(computer_total<sum(user_cards)):
            print(f"Your Final hand  {user_cards}")
            print(f"Computer final {computer_cards}")
            print("Congrats! you win!")
            exit()

        #if the computer score and user score are equal then its a draw
        else:
            print(f"computer score {computer_total}")
            print(f"user score "+str(sum(user_cards)))
            print("its a draw")
            exit()
else:
    print("ok dude have a nice day")
