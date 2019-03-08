import random
import time

deck = [
		{
			'suit':'Heart',
			'value':'2',
			'point': 2
		},
		{
			'suit':'Diamond',
			'value':'2',
			'point': 2
		},
		{
			'suit':'Club',
			'value':'2',
			'point': 2
		},
		{
			'suit':'Spade',
			'value':'2',
			'point': 2
		},
		{
			'suit':'Heart',
			'value':'3',
			'point': 3
		},
		{
			'suit':'Diamond',
			'value':'3',
			'point': 3
		},
		{
			'suit':'Club',
			'value':'3',
			'point': 3
		},
		{
			'suit':'Spade',
			'value':'3',
			'point':3
		},
		{
			'suit':'Heart',
			'value':'4',
			'point': 4
		},
		{
			'suit':'Diamond',
			'value':'4',
			'point': 4
		},
		{
			'suit':'Club',
			'value':'4',
			'point': 4
		},
		{
			'suit':'Spade',
			'value':'4',
			'point': 4
		},
		{
			'suit':'Heart',
			'value':'5',
			'point': 5
		},
		{
			'suit':'Diamond',
			'value':'5',
			'point': 5
		},
		{
			'suit':'Club',
			'value':'5',
			'point': 5
		},
		{
			'suit':'Spade',
			'value':'5',
			'point': 5
		},
		{
			'suit':'Heart',
			'value':'6',
			'point': 6
		},
		{
			'suit':'Diamond',
			'value':'6',
			'point': 6
		},
		{
			'suit':'Club',
			'value':'6',
			'point': 6
		},
		{
			'suit':'Spade',
			'value':'6',
			'point': 6
		},
		{
			'suit':'Heart',
			'value':'7',
			'point': 7
		},
		{
			'suit':'Diamond',
			'value':'7',
			'point': 7
		},
		{
			'suit':'Club',
			'value':'7',
			'point': 7
		},
		{
			'suit':'Spade',
			'value':'7',
			'point': 7
		},
		{
			'suit':'Heart',
			'value':'8',
			'point': 8
		},
		{
			'suit':'Diamond',
			'value':'8',
			'point': 8
		},
		{
			'suit':'Club',
			'value':'8',
			'point': 8
		},
		{
			'suit':'Spade',
			'value':'8',
			'point': 8
		},
		{
			'suit':'Heart',
			'value':'9',
			'point': 9
		},
		{
			'suit':'Diamond',
			'value':'9',
			'point': 9
		},
		{
			'suit':'Club',
			'value':'9',
			'point': 9
		},
		{
			'suit':'Spade',
			'value':'9',
			'point': 9
		},
		{
			'suit':'Heart',
			'value':'10',
			'point': 10
		},
		{
			'suit':'Diamond',
			'value':'10',
			'point': 10
		},
		{
			'suit':'Club',
			'value':'10',
			'point': 10
		},
		{
			'suit':'Spade',
			'value':'10',
			'point': 10
		},
		{
			'suit':'Heart',
			'value':'Jack',
			'point': 10
		},
		{
			'suit':'Diamond',
			'value':'Jack',
			'point': 10
		},
		{
			'suit':'Club',
			'value':'Jack',
			'point': 10
		},
		{
			'suit':'Spade',
			'value':'Jack',
			'point': 10
		},
		{
			'suit':'Heart',
			'value':'Queen',
			'point': 10
		},
		{
			'suit':'Diamond',
			'value':'Queen',
			'point': 10
		},
		{
			'suit':'Club',
			'value':'Queen',
			'point': 10
		},
		{
			'suit':'Spade',
			'value':'Queen',
			'point': 10
		},
		{
			'suit':'Heart',
			'value':'King',
			'point': 10
		},
		{
			'suit':'Diamond',
			'value':'King',
			'point': 10
		},
		{
			'suit':'Club',
			'value':'King',
			'point': 10
		},
		{
			'suit':'Spade',
			'value':'King',
			'point': 10
		},
		{
			'suit':'Heart',
			'value':'Ace',
			'point': 0
		},
		{
			'suit':'Diamond',
			'value':'Ace',
			'point': 0
		},
		{
			'suit':'Club',
			'value':'Ace',
			'point': 0
		},
		{
			'suit':'Spade',
			'value':'Ace',
			'point': 0
		},
]

player_hand = []
dealer_hand = []
player_first = 1
dealer_first = 1
dealer_score = 0
player_score = 0

def Ace_check(score, hand):
	for i in hand:
		if i['value'] == 'Ace' and score + 11 > 21:
			score = score + 1
		elif i['value'] == 'Ace' and score + 11 <= 21:
			score = score + 11
	return score

def player(hand): #player option card picking
	global player_first
	global player_score
	player_score = 0
	if player_first == 1:
		player_first = player_first + 1
		more(hand)
	print('\nNow in you hand: ')
	for i in hand:
		print(i['value'] + ' of ' + i['suit'])
		player_score = player_score + i['point']
	player_score = Ace_check(player_score, hand)
	print('\nAnd you have ' + str(player_score) + ' score')
	
def dealer(hand):#dealer option card picking
	global dealer_first
	global dealer_score
	dealer_score = 0
	dealer_score = Ace_check(dealer_score, hand)
	print('\nDealer have: ')
	if dealer_first == 1:
		more(hand)
		print(hand[0]['value'] + ' of ' + hand[0]['suit'])
		if hand[0]['point'] > 9 or dealer_score > 9:
			print(hand[1]['value'] + ' of ' + hand[1]['suit'])
			for i in hand:

				dealer_score = dealer_score + i['point']
			print('Current Dealer score is ' + str(dealer_score))
		else:
			print('And hidden card')
			print('\nCurrent Dealer score is ' + str(hand[0]['point']))
		dealer_first = dealer_first + 1
	else:
		for i in hand:
			print(i['value'] + ' of ' + i['suit'])
			dealer_score = dealer_score + i['point']
		
		print('\nAnd ' + str(dealer_score) + ' score')
	
def more(hand, turn = 'none', deck = deck): #card picking
	a = random.choice(deck)
	deck.remove(a)
	hand.append(a)
	if turn == 'player':
		score = player(hand)
	elif turn == 'dealer':
		score = dealer(hand)

more(player_hand, turn = 'player')
time.sleep(0.5)
more(dealer_hand, turn = 'dealer')
while True:
	if int(player_score) == 21: #blackjack check
		print('BlackjacK!')
		if int(dealer_score) == 21:
			print('Dealer too have blackjack')
			print("That's push!")
		else:
			print('You win!')
		break
	else:#player add card
		while True:
			if int(player_score) < 21:
				pick_choise = input('\nDo you want pick another card?(y/n) ')
				if pick_choise == 'y' or pick_choise == 'Y':
					time.sleep(0.5)
					print('\nHit me! ')
					time.sleep(0.5)
					more(player_hand, turn = 'player')
				elif pick_choise == 'n' or pick_choise == 'N':
					print('\nEnough!')
					break
			elif int(player_score) > 21:
				print('\nMuch!')
				print('Dealer win!')
				break
			elif int(player_score) == 21:
				print('\nEnough!')
				break
		if int(player_score) > 21:
			break

	print('\nDealer have:')
	dealer_score = 0
	for i in dealer_hand:#dealer hand
		print(i['value'] + ' of ' + i['suit'])
		dealer_score = dealer_score + i['point']

	print('\nAnd ' + str(dealer_score) + ' score')
	while True:#dealer add card
		if int(dealer_score) > 16:
			if int(dealer_score) > 21:
				print('\nMuch')
				print('\nDealer finished picking cards.')
			else:
				print('\nDealer finished picking cards.')
			break
		else:
			print('Dealer picked a card')
			more(dealer_hand, turn = 'dealer')
	if dealer_score == player_score:#game resoult
		print('\nDealer have ' + str(dealer_score) + ' score')
		print('You too have ' + str(player_score) + ' score')
		print("That's push!")
	elif dealer_score > player_score and dealer_score < 22:
		print('\nDealer have ' + str(dealer_score) + ' score and win!')
	elif dealer_score < player_score or dealer_score > 21:
		print('\nYou have ' + str(player_score) + ' score and win!')
	break