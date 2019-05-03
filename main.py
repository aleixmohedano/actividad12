#!/bin/python3 SE

def showInstructions():
    #print a main menu and the commands
    print('''
RPG Game
========
Llega al atico con la llave para ganar
evita el monstruo!
Commands:
  go [direccion]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print("Inventory : " + str(inventory))
  #print an item if there is oneç
  if "descripcion" in rooms[currentRoom]:
    print("esta habitacion huele a otaku, y hay papeleras rotas por el suelo")
  if "sur" in rooms[currentRoom]:
    print('sur : '+ rooms[currentRoom]['sur'])
  if "este" in rooms[currentRoom]:
    print('este : '+ rooms[currentRoom]['este'])
  if "norte" in rooms[currentRoom]:
    print('norte : '+ rooms[currentRoom]['norte'])
  if "oeste" in rooms[currentRoom]:
    print('oeste : '+ rooms[currentRoom]['oeste'])
  if "item" in rooms[currentRoom]:
    for element in rooms[currentRoom]["item"]:
      print('You see a ' + element)
  print("---------------------------")
#an inventory, which is initially empty
inventory = []
#a dictionary linking a room to other room positions
rooms = {
                 #Habitaciones Manu
            'baño' : {'oeste' : 'Comedor',
                #tendras que usar las tijeras para cortar la cuerda del armario
                            'item'  : ["desodorante","rollo de papel"]
                            },

            'armario de limpieza' : { 'este' : 'pasillo',
                           'item'  : ["mechero","cortauñas"]

            },


            'sala de empleados' : { 'este' : 'pasillo',
                                  'item'  : ["cuchillo","liquido"]
              
            },

            'Recibidor' : { 'sur' : 'Cocina',
                  'este'  : 'Comedor',

                  'norte' : 'pasillo',
                  'item'  : ["reloj"]
                  
                },        
            'Cocina' : { 'norte' : 'Recibidor',
                  'sur' : 'Despensa',
                  'item'  : ["sopa","monstro"]
                },
                
            'Comedor' : { 'oeste'  : 'Recibidor',
                  'Sur' : 'jardin',
                  'este' : 'baño',
                  'item'  : 'potion'
              
                },
                
            'jardín' : { 'norte' : 'Comedor' },
            
            # HABITACIONES DE cdeveloper ###### v
            'Sala de descanso' : { 'item' : ["tumbona","altavoz"],
                  'este' : 'Salón'
              },
              'Despensa' : { 'item' : ["pan bimbo","Chocapic","Escoba mágica","Cromo de Doraemon"],
                  'norte' : 'Cocina',
              },
              'Sala de esclavos' : { 'item' : ["soga","espada láser","legia","candelabro"],
                'norte' : 'jardin'
              },
            # Si coges el paraguas y bajas por las escaleras, mueres.
            # Si l ocoges y te tiras por el balcón, mueres.
              'Atico' : { 'sur' : 'pasillo',
                          'item' : ["cofre"]},
             #HABITACIONES DE CDEVELOPER
#HABITACIONES de sdeveloper

              'Habitacion del Milia' : { 'descripcion' : '',
                                        'item' : ["papelera","anime","hentai","llave"],
      	                                'oeste' : 'pasillo'},
	            'pasillo' : {  'este' : 'Habitacion del Milia', 
		                         'norte' : 'Atico',
		                         'oeste' : 'sala de empleados',
		                         'sur' : 'Recibidor'
	               },
		 
         }

#start the player in the Hall
currentRoom = 'Recibidor'
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
  if 'item' in rooms[currentRoom] and 'monstro' in rooms[currentRoom]['item']:
    print('te ha comido el monstro... GAME OVER!')
    break
  if currentRoom == 'Atico' and 'llave' in inventory:
    print('has llegado al atico y has abierto el cofre easy peasy lemon squeezy')
    break
  # player wins if they get to the garden with a key and a shield
  

    
