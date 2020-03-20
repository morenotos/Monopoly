from random import randint
from time import sleep
#import sys
#from cards import card_chooser


players_number = []
players_names = []
players_money = []
players_position = []

property_names = ['Go', 'Mediterranean Av', 'Community Chest', 'Baltic Av', 'Income Tax', 'Reading Railroad', 'Oriental Av', 'Chance', 'Vermont Av', 'Conneticut Av', 'Jail', 'St Charles Place', 'Electric Company', 'States Av', 'Virginia Av', 'Pennsylvania Railroad', 'St James Place', 'Community Chest', 'Tennesse Av', 'New York Av', 'Free Parking', 'Kentucky Av', 'Chance', 'Indiana Av', 'Illinois Av', 'B&O Railroad', 'Atlantic Av', 'Ventnor Av', 'Water Works', 'Marvin Gardens', 'Go to Jail!', 'Pacific Av', 'North Carolina Av', 'Community Chest', 'Pennsylvania Av', 'Short Line', 'Chance', 'Park Place', 'Luxury Tax', 'Boardwalk' ]
property_price = [0, 60, 0, 60, 0, 200, 100, 0, 100, 120, 0, 140, 150, 140, 160, 200, 180, 0, 180, 200, 0,220, 0, 220, 240, 200, 260, 260, 150, 280, 0, 300, 300, 0, 320, 200, 0, 350, 0, 400 ]
property_position = [1 , 2 , 3, 4, 5, 6, 7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
property_owner = ['No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner', 'No owner']
property_rent = [0, 2, 0, 4, 200, 25, 6, 0, 6, 8, 0, 10, 28, 10, 12, 25, 14, 0, 14, 16, 0, 18, 0, 18, 20, 25, 22, 22, 28, 24, 0, 26, 26, 0, 28, 25, 0, 35, 75, 50]
property_has_home = ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No']
property_has_hotel = ['No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No'] 

print('------------------------')
print('-----  MONOPOLY  -------')
print('------------------------')

number_of_players = int(input('How many players will play? '))

#creates the list with players' number
for player in range(1, (number_of_players + 1)):
  players_number.append(player)

#creates the lists with players' name, initial money and initial position 
for player in players_number:
  player_name = input('Player choose your name: ')
  players_names.append(player_name)
  players_money.append(1500)
  players_position.append(0)

print(players_names)
print(players_money)
print(players_position)

game_on = True
turn = 0 #variable that stores wich player's turn it is
money_in_free_parking = 0

#checks if the player has money left after he has payed for something
def player_has_money():
  if players_money[turn] < 0:
    print('You are broke, the game has ended for you')
    game_on = False
  else:
    print('You have now $' + str(players_money[turn]) + ' available')

#This function runs when a player lands on Go, income tax, Jail, Free Parking, Go to Jail or luxury tax
def special_properties():
  global money_in_free_parking
  if players_position[turn] == 0:
    print('Your position is now ' + str(property_names[players_position[turn]]))
  elif players_position[turn] == 4:
    print('You have to pay income tax of $200 or 10% of your total money (the highest)')
    income_tax_10 = 0.1 * players_money[turn]
    if income_tax_10 > 200:
      players_money[turn] -= income_tax_10
      print('You paid $' + str(income_tax_10) + ' of income tax')
      money_in_free_parking += income_tax_10
      print('This money you paid will go to Free Parking.')
      print('The total money in Free Parking is $' + str(money_in_free_parking))
      player_has_money()
    else:
      players_money[turn] -= 200
      print('You paid $200 of income tax')
      money_in_free_parking += 200
      print('This money you paid will go to Free Parking.')
      print('The total money in Free Parking is $' + str(money_in_free_parking))
      player_has_money()
  elif players_position[turn] == 10:
    print('You are in ' + str(property_names[players_position[turn]]) + ', but you are just visiting' )
  elif players_position[turn] == 20:
    print('Your position is now ' + str(property_names[players_position[turn]]))
    print('Congratulations! You earn $' + str(money_in_free_parking) + ' that was saved here')
    players_money[turn] += money_in_free_parking
    money_in_free_parking = 0
  elif players_position[turn] == 30:
    print(str(property_names[players_position[turn]]) + ' You will not collect $200 and will go back straight to jail.')
    players_position[turn] = 10
  elif players_position[turn] == 38:
    print('Luxury tax: you have to pay $75')
    players_money[turn] -= 75
    money_in_free_parking += 75
    print('This money you paid will go to Free Parking.')
    print('The total money in Free Parking is $' + str(money_in_free_parking))
    player_has_money()

#choses a card when a player lands on community chest or chance
def card_chooser(x):
  number = turn
  
#community chest cards 

  #card that advances player to GO and gives him $200
  def one():
    print('You advance directly to GO and collect $200')
    players_position[number] = 0
    players_money[number] += 200  
    player_has_money()

  #gives player $100
  def two():
    print('You inherit $100')
    players_money[number] += 100
    player_has_money()

  #player collects $50 from every player. 
  def three():
    print('Collect $50 from every player')
    payment_from_players = 50 * (len(players_number) - 1)
    players_money[number] += payment_from_players
    for name in players_names:
      if name != players_names[number]:
        index = players_names.index(name)
        players_money[index] -= 50
    print('You received a total of $' + str(payment_from_players))
    player_has_money()

  #player receives $25
  def four():
    print ('You receive $25 for services')
    players_money[number] += 25
    player_has_money()

  #sents player to Jail
  def five():
    print('You go directly to Jail without passing GO and without collecting $200')
    players_position[number] = 10
    player_has_money()

  #player receives $100
  def six():
    print('Xmas funds matures, you receive $100')
    players_money[number] += 100
    player_has_money()

  #NOT COMPLETE YET!!! player recieves get-out-of-jail-free card
  def seven():
    print('You now have a card to get out of jail for free')
    print('You can use it wenever you want or sell it')
    player_has_money()

  #player receives $10
  def eight():
    print('You have won 2nd place in a beauty contest, collect $10')
    players_money[number] += 10
    player_has_money()
  
  #player receives $45
  def nine():
    print('From sale of stock you get $45')
    players_money[number] += 45
    player_has_money()

  #players pays $100 for the hospital
  def ten():
    global money_in_free_parking
    print('Pay $100 for hospital expenses')
    players_money[number] -= 100
    money_in_free_parking += 100
    print('This money you paid will go to Free Parking.')
    print('The total money in Free Parking is $' + str(money_in_free_parking))
    player_has_money()

  #player receives $20
  def eleven():
    print('Income tax refund, you receive $20')
    players_money[number] += 20
    player_has_money()

  #player pays $50
  def twelve():
    global money_in_free_parking
    print('For Doctor\'s fee you pay $50')
    players_money[number] -= 50
    money_in_free_parking += 50
    print('This money you paid will go to Free Parking.')
    print('The total money in Free Parking is $' + str(money_in_free_parking))
    player_has_money()

  #player receives $200
  def thirteen():
    print('Bank error in your favor, you receive $200')
    players_money[number] += 200
    player_has_money()

  #player receives $100
  def fourteen():
    print('Life insurance matures, you receive $100')
    players_money[number] += 100
    player_has_money()

  #player pays $150
  def fifteen():
    global money_in_free_parking
    print('School tax, you pay $150')
    players_money[number] -= 150
    money_in_free_parking += 150
    print('This money you paid will go to Free Parking.')
    print('The total money in Free Parking is $' + str(money_in_free_parking))
    player_has_money()

  #NOT COMPLETE YET!!! player pays $40 for each house and $115 for each hotel
  def sixteen():
    print('For street repairs you pay $40 for each house and $115 for each hotel')
    player_has_money()


  #chance cards

  #player pays $50 to each payer
  def seventeen():
    print('You are elected Chairman of the Board, pay each player $50')
    payment_to_players = 50 * (len(players_number) - 1)
    players_money[number] -= payment_to_players
    for name in players_names:
      if name != players_names[number]:
        index = players_names.index(name)
        players_money[index] += 50
    print('You payed a total of $' + str(payment_to_players))
    player_has_money()

  #player goes back 3 spaces 
  def eighteen():
    print('Go back three spaces')
    players_position[number] -= 3
    print('You are now in ' + str(players_position[number]))
    player_has_money()

  #player advances to St Charles Place and collects $200 if he passes GO
  def nineteen():
    print('You advance to ' + property_names[11])
    if players_position[number] > 11:
      print('As you passed Go you receive $200')
      players_money[number] += 200
      players_position[number] = 11
      player_has_money()
    else:
      players_position[number] = 11
      player_has_money()
  
  #player pays $15
  def twenty():
    global money_in_free_parking
    print('You pay a poor tax of $15')
    players_money[number] -= 15
    money_in_free_parking += 15
    print('This money you paid will go to Free Parking.')
    print('The total money in Free Parking is $' + str(money_in_free_parking))
    player_has_money()

  #Player advances to Boardwalk
  def twentyone():
    print('Take a walk on the board walk, you advance to Boardwalk')
    players_position[number] = 39
    player_has_money()

  #advances player to the nearest railroad.
  def twentytwo():
    if players_position[number] == 7:
      print('You will advance to ' + property_names[15])
      players_position[number] == 15
      player_has_money()
    elif players_position[number] == 22:
      print('You will advance to ' + property_names[25])
      players_position[number] == 25
      player_has_money()
    elif players_position[number] == 36:
      print('You will advance to ' + property_names[5])
      players_position[number] == 5
      player_has_money()

  #card that advances player to GO and gives him $200
  def twentythree():
    print('You advance directly to GO and collect $200')
    players_position[number] = 0
    players_money[number] += 200  
    player_has_money()
  
  #NOT COMPLETE YET!!! player pays $25 for each house and $110 for each hotel
  def twentyfour():
    print('Make repairs to you properties, you pay $25 for each house and $110 for each hotel')
    player_has_money()

  #sents player to Jail
  def twentyfive():
    print('You go directly to Jail without passing GO and without collecting $200')
    players_position[number] = 10
    player_has_money()

  #Player advances to Illinois Av  
  def twentysix():
    print('You advance to ' + property_names[24])
    players_position[number] = 24
    player_has_money()

  #NOT COMPLETE YET!!! player recieves get-out-of-jail-free card
  def twentyseven():
    print('You now have a card to get out of jail for free')
    print('You can use it wenever you want or sell it')
    player_has_money()

  #player receives $50
  def twentyeight():
    print('Your building and loan matures, you receive $50')
    players_money[number] += 50
    player_has_money()

  #player receives $50
  def twentynine():
    print('The bank pays you a dividend of $50')
    players_money[number] += 50
    player_has_money()

  #player goes to Reading railroad and if he passes GO collects $200
  def thirty():
    print('Take a ride on the ' + property_names[5] + '.')
    players_position[number] = 5
    print('As you passed GO, you will receive $200')
    players_money[number] += 200
    player_has_money()

  #player advances to the nearest utility
  def thirtyone():
    print('You advance to the nearest utility');
    if players_position[number] == 7:
      print('You will advance to ' + property_names[12])
      players_position[number] == 12
      player_has_money()
    elif players_position[number] == 22:
      print('You will advance to ' + property_names[28])
      players_position[number] == 28
      player_has_money()
    elif players_position[number] == 36:
      print('You will advance to ' + property_names[12])
      players_position[number] == 12
      player_has_money()


#'switch' statement to run the selected card

  switcher = {
    1: one,
    2: two,
    3: three,
    4: four,
    5: five,
    6: six,
    7: seven,
    8: eight,
    9: nine,
    10: ten,
    11: eleven,
    12: twelve,
    13: thirteen,
    14: fourteen,
    15: fifteen,
    16: sixteen,
    17: seventeen,
    18: eighteen,
    19: nineteen,
    20: twenty,
    21: twentyone,
    22: twentytwo,
    23: twentythree,
    24: twentyfour,
    25: twentyfive,
    26: twentysix,
    27: twentyseven,
    28: twentyeight,
    29: twentynine,
    30: thirty,
    31: thirtyone
  }
  # Get the function from switcher dictionary
  func = switcher.get(x)
  # Execute the function
  return func()

#rolls the dice 
def roll_dice():
  return randint(1,6) + randint(1,6)


#game code
while game_on:
  print('------------------------------------')
  print(players_names[turn] + ' you are in ' + str(property_names[players_position[turn]]))
  sleep(3)
  print(players_names[turn] + ' Roll the dice')
  print('Rolling the dice...')
  sleep(3)
  player1_dice = roll_dice()
  print('The dice turned ' + str(player1_dice))
  if players_position[turn] + player1_dice > 39:
    players_money[turn] += 200
    print('You completed another lap and got $200. You now have $' + str(players_money[turn]))
    players_position[turn] = players_position[turn] + player1_dice - 40
  else:
    players_position[turn] = players_position[turn] + player1_dice
  print('Your position is now ' + str(property_names[players_position[turn]]))
  if players_position[turn] == 2 or players_position[turn] == 17 or players_position[turn] == 33:
    comm_card_number = randint(1,16)
    print(comm_card_number)
    card_chooser(comm_card_number)
  elif players_position[turn] == 7 or players_position[turn] == 22 or players_position[turn] == 36:
    chance_card_number = randint(17,31)
    print(chance_card_number)
    card_chooser(chance_card_number)
  elif players_position[turn] == 0 or players_position[turn] == 4 or players_position[turn] == 10 or players_position[turn] == 20 or players_position[turn] == 30 or players_position[turn] == 38:
    special_properties()
  else:
    if property_owner[players_position[turn]] == 'No owner':
      print(str(property_names[players_position[turn]]) + ' has no owner!')
      print('You can buy it for $' + str(property_price[players_position[turn]]) + ' and get a rent of $'+ str(property_rent[players_position[turn]]))
      print('You have $' + str(players_money[turn]) + ' available')
      print('Choose a) to buy it or b) Not buy it')
      player_choice = input('What do you want to do?')
      if player_choice == 'a':
        print('Processing your request...')
        sleep(5)
        if players_money[turn] >= property_price[players_position[turn]]:
          print('Congratulations! You are now the owner of ' + property_names[players_position[turn]])
          property_owner[players_position[turn]] = players_names[turn]
          players_money[turn] -= property_price[players_position[turn]]
          print('You have now $' + str(players_money[turn]) + ' available')
        else:
          print('You do not have enough money to buy this property')
      else:
        print('Processing your request...')
        sleep(5)
        print('You did not buy ' + property_names[players_position[turn]])
    elif property_owner[players_position[turn]] == players_names[turn]:
      print('You are the owner of ' + property_names[players_position[turn]] + '. Welcome! Enjoy your stay.')
    else:
      print('This property is owned by ' + property_owner[players_position[turn]] + ' and you will have to pay the owner $' + str(property_rent[players_position[turn]]) + ' for your stay')
      players_money[turn] -= property_rent[players_position[turn]]
      landlord = players_names.index(property_owner[players_position[turn]])
      players_money[landlord] += property_rent[players_position[turn]]
      player_has_money()
  print('It is now the turn for the next player')
  sleep(3)
  if turn < len(players_number) - 1:
    turn += 1
  else:
    turn = 0


