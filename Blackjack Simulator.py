import random
import time

# 1 Player vs Dealer Black Jack Simulation - No Split / No Double - Dealer stands at all 17

J, Q, K, A = 10, 10, 10, 11

cards = [2,3,4,5,6,7,8,9,10,J,Q,K,A]

deck = cards * 4

player_hand = []
dealer_hand = []

#print(str(dealer_hand) + '\n')

def draw(who, n):
    for i in range(n):
        who.append(random.choice(deck))
        deck.remove(who[-1])
        time.sleep(1)
        for j in who:
            if j == 11 and sum(who) > 21:
                who.remove(j)
                who.append(1)
        if who == player_hand:
            print('Player: ' + str(player_hand))

def start():
    draw(player_hand, 2)
    draw(dealer_hand, 2)
    print('Dealer: ' + '[' + str(dealer_hand[0]) + ']')
    time.sleep(1)


def choose():
    if sum(player_hand) != 21:
        choice = input('Hit or Stand?: ')
        if choice == 'Hit' :
            draw(player_hand, 1)
            if sum(player_hand) == 21:
                return
            elif sum(player_hand) > 21:
                time.sleep(1)
                print('Bust - player loses')
                print('Dealer: ' + str(dealer_hand))
            else:
                choose()
        else:
            return

def compare():
    if sum(player_hand) <= 21:
        while sum(dealer_hand) < 17:
            draw(dealer_hand, 1)
            print('Dealer: ' + str(dealer_hand))
            time.sleep(1)
        if sum(dealer_hand) == sum(player_hand) and sum(dealer_hand) >= 17:
            if sum(dealer_hand) >= 17:
                print('Dealer: ' + str(dealer_hand))
            time.sleep(1)
            print('Push! Nobody wins')
        if sum(dealer_hand) > 21:
            print('Dealer: ' + str(dealer_hand))
            print('Too much for the dealer - Player wins!')
        elif sum(dealer_hand) > sum(player_hand):
            time.sleep(1)
            print('Dealer: ' + str(dealer_hand))
            time.sleep(1)
            print('Dealer wins')
        elif sum(dealer_hand) == sum(player_hand):
            return
        else:
            print('Dealer: ' + str(dealer_hand))
            print('Player wins!')

start()
choose()
time.sleep(1)
compare()
        

