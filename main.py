#!/bin/python3 SE
#activar cdeveloper
def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Get to the Garden with a key and a potion
Avoid the monsters!
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print("Inventory : " + str(inventory))
  #print an item if there is one
  if "south" in rooms[currentRoom]:
    print('south : '+ rooms[currentRoom]['south'])
  if "east" in rooms[currentRoom]:
    print('east : '+ rooms[currentRoom]['east'])
  if "north" in rooms[currentRoom]:
    print('north : '+ rooms[currentRoom]['north'])
  if "west" in rooms[currentRoom]:
    print('west : '+ rooms[currentRoom]['west'])
  if "item" in rooms[currentRoom]:
    for element in rooms[currentRoom]["item"]:
      print('You see a ' + element)
  print("---------------------------")
#an inventory, which is initially empty
inventory = []
#a dictionary linking a room to other room positions
rooms = {
            'Hall' : { 'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'item'  : ["key","reloj"],
                  
                },        
            'Kitchen' : { 'north' : 'Hall',
                  'item'  : 'monster'
                },
                
            'Dining Room' : { 'west'  : 'Hall',
                  'south' : 'Garden',
                  'item'  : 'potion'
              
                },
                
            'Garden' : { 'north' : 'Dining Room' },
            
            # HABITACIONES DE cdeveloper ###### v
            # Puedes ver o tumbarte en la tumbona, si te tumbas, mueres, si la ves, no hace nada
            # Si lo enciendes no pasa nada, si lo miras, se te cae y mueres
            'Sala de descanso' : { 'item' : ["tumbona","altavoz"],
                  'este' : 'Salón'
              },
            # Si comes el pan bimbo te curas y sale un oso mágico que te concede 1 deseo, y puedes elegir. Que muera el otaku, ser Lv35 Boss mafia, Liberar al oso. Si liberas al oso, tienes una vida extra, si eres Lv35 boss mafia ganas el juego, si haces que muera el otaku, te mueres tu
            # Lo coges y es un ingrediente para mezclar con "Legia" pero solo podrás hacerlo en la "Cocina".
            # Escoba mágica, te lleva al "Ático"
            # Te lo pegas en la frente, y ya está.  
              'Despensa' : { 'item' : ["pan bimbo","Chocapic","Escoba mágica","Cromo de Doraemon"],
                  'norte' : 'Cocina',
            # Lo coges y es un ingrediente para mezclar con "Legia" pero solo podrás hacerlo en la "Cocina".
            # Escoba mágica, te lleva al "Ático"
            # Te lo pegas en la frente, y ya está.
              },
            # La coges, si la usas en el "ático" bajas al "jardín", si la usas en algun "baño" mueres.
            # Puedes matar al "Otaku Monster", si la coges y te lo encuentras, si no la coges, mueres (Ya que llega el "monsterOtaku" y te mato).
            # Lo coges y es un ingrediente para mezclar con "Chocapic" pero solo podrás hacerlo en la "Cocina".    
            # Si le pones una luz, lo puedes encender si lo coges y lo tienes contigo encendido todo el rato. 
              'Sala de esclavos' : { 'item' : ["soga","espada láser","legia","candelabro"],
                'norte' : 'Jardín'
              },
            # Si coges el paraguas y bajas por las escaleras, mueres.
            # Si l ocoges y te tiras por el balcón, mueres.
              'Atico' : { 'item' : ["paragüas", "paracaidas"]
              },

            # HABITACIONES DE cdeveloper ####### ^
            
         }
#start the player in the Hall
currentRoom = 'Hall'
showInstructions()
#loop forever
while True:
  showStatus()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>') 
    
  move = move.lower().split()
  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
      print('You can\'t go that way!')
  #if they type 'get' first 
  if move[0] == 'get' :

    #if the room contains an item, and the item is the one they want to get
    if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      print(rooms[currentRoom]["item"][0])
      #delete the item from the room
      del rooms[currentRoom]["item"][rooms[currentRoom]["item"].index(move[1])]
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')

  
  # player loses if they enter a room with a monster
  if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
  # player wins if they get to the garden with a key and a shield
  

    