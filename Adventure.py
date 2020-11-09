from Room import Room, Monster
from Player import Player 
# Declare all the rooms
import random

room = {
'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [], 0, [], ["Body Armor" ], ["There are no enemies here..."]),

'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "snakes", 4, 4, ["sword", "helmet"], ["Snakes...why did it have to be snakes?"]),

'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "goblins", 12, 3, ["key", "bomb"], ["Out of nowhere come three scary goblins"]),

'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "mummies", 15, 3, ["bow", "arrows"], ["A group of Mummies lumber towards you"]),

'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. """, "red dragon", 40 , 2, ["diamond", "Arkenstone"], ["A giant Red Dragon approaches"]),

'Cave Exit': Room("Cave Exit", """You have free solod your way out of the treasure room to the opening above, 
the sun greets you as you claw your way through the rocks to a giant open field""", [], 0, [] ),

'Enchanted Forest': Room("Enchanted Forest", """As you enter the woods you feel a bit funny...You turn around to 
retreat, only to find that you are completely lost""", "giant spider", 80, 1, ['Ocarina', 'Bag of marbles'], ['From the treetops, a giant spider \
descends upon you!']),

'Magical Entrance': Room("Magical Entrance", """The forest has captured you and brought you here...A world of wonder and magic
await you now! Beware the beasts that dwell within!""",[], 0, [],  ['Magic Cloak', 'Crystal Sword', 'Wand of Death']),

'Cauldron Room': Room("Cauldron Room", """In the center of the room lies a large cauldron...it is bubbling.""", "witch", 185, 1, 
['Broomstick', 'Glowing Candle'], ['As you enter the room, a witch flies down from the ceiling to attack you!']),

'Wizard training room':Room("Wizard Training Room", """Wizards are battling it out in the corner...they spot you...""", "wizard", 140, 1, 
['Enchanted Staff', 'Boomerang'], ['The head Wizard aims his wand at you']),

'Cloud Fortress': Room("Cloud Fortress", """You jump off of the broomstick and land at the gates of a mighty fortress, high up on a magical floating cloud city""", [], 0, [] ),
'Mysterious Shack': Room("Mysterious Shack", """You arrive at an old run down shack in the middle of the clouds\
    what on earth is this thing doing here???""", [], 0, [], ['Glowing Orb']),  
'Rabbit Hole': Room("Rabbit Hole", """You fall down a giant hole within the hut, in front of you is a tiny door""", [], 0, [],\
     ['Mysterious looking Brownie'] ),
'Castle Gates': Room('Castle Gates', """Before you stands a towering fortress. As you walk closer you see two giant posts with skulls at the top of them""",\
    "Ogre Guard", 165, 2, ['Golden Axe'], ['A large brute wielding a giant mace comes charging at you']),
'Ogre Fortress': Room('Ogre Fortress', """The fortress ceiling is at least 100 feet tall...you are but a puny ant in this lair!""",\
    'Captain of the Ogre Guard', 300, .8, ['Diamond Sword'], ['A massive ogre descends down the stairs!']),
"Ogre King's Lair": Room("Ogre King's Lair", """You hear a thumping from within the cave...the sound grows louder and louder!""",\
    'The Ogre King', 1000, .5, ['Ring of invisibility'],['A towering ogre with a golden crown comes lumbering through the cave'] )                      
}





Wonderland = {'WonderWorld': Room('WonderWorld', """As you fit through the miniature door, a vast forest lies before you""", [], 0, [])

}

# Link rooms together
#World 1
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['treasure'].n_to = room['Cave Exit']
room['Cave Exit'].s_to = room['treasure']
room['Cave Exit'].e_to = room['Enchanted Forest']
room['Enchanted Forest'].magic_to = room['Magical Entrance']
#World 2
room['Magical Entrance'].n_to = room['Cauldron Room']
room['Cauldron Room'].s_to = room['Magical Entrance']
room['Magical Entrance'].e_to =room['Wizard training room']
room['Wizard training room'].w_to = room['Magical Entrance']
room['Cauldron Room'].fly_to = room['Cloud Fortress']
room['Cloud Fortress'].e_to = room['Mysterious Shack']
room['Cloud Fortress'].fly_to = room['Cauldron Room']
room['Mysterious Shack'].magic_to = room['Rabbit Hole']
room['Rabbit Hole'].magic_to = Wonderland['WonderWorld']
room['Mysterious Shack'].w_to = room['Cloud Fortress']
room['Mysterious Shack'].n_to = room['Castle Gates']
room['Castle Gates'].s_to = room['Mysterious Shack']
room['Castle Gates'].n_to = room['Ogre Fortress']
room['Ogre Fortress'].s_to = room['Castle Gates']
room['Ogre Fortress'].n_to = room["Ogre King's Lair"]
room["Ogre King's Lair"].s_to = room['Ogre Fortress']


User_name = input("Please enter your name: \n")

player = Player(name=User_name, level=1, defense=1,  magic_level=1, \
    room=room["outside"],  item=[] ) 

print(f"Welcome {player.name}")

difficulty_choice = ""

while difficulty_choice != "easy" and difficulty_choice != "medium" and difficulty_choice != "hard" and difficulty_choice != "expert":
    difficulty_choice = input("Please choose easy, medium, hard, or expert: \n")
        
player.set_lives(difficulty_choice)
player.set_initial_fortune_and_defense()

print(f"Your starting fortune is {player.fortune}") 
print(f"Your starting defense is {player.defense}") 
Quit_Choice = False 

while True:
    #Set attributes at start of every battle
    if Quit_Choice == True:
        print("Your journey has ended!")
        break 
    
    if player.lives <=0:
        print("Your journey has ended, but we all must fade someday...try again soon!")
        break 
    print('----------------------------------------')
    print('----------------------------------------')
    print(f"You are currently in the {player.room.name}")
    print('----------------------------------------')        
    
    player.set_player_attributes(difficulty_choice)

    #lives, level, and magic level are based on experience and defeating monsters, they can not reset
    # player.lives = round((player.lives * player.level * player.magic_level),1)
    print(f"Your current level is {round(player.level, 1)}, your current magic level is {round(player.magic_level,1)}")
    print('----------------------------------------')
    print(f"You currently have {round(player.lives,1)} lives left.")
    print('----------------------------------------')
    print(f"Your current attack is {round(player.attack,1)}, Your current magic attack is {round(player.magic_attack,1)},\n\
    Your current defense is {round(player.defense, 1)}")
    print('----------------------------------------')
    print("Your attack, magic_attack, defense, level, and magic level all improve your ability to defeat monsters!")
    print('----------------------------------------')
           
    if player.room.name == "Rabbit Hole":
        if 'Mysterious looking Brownie' in player.item:
            print("A tiny door stands before you. Dirt begins to fall from the ceiling, you'd better find a way out quickly!")
            escape = input("Do you walk through the tiny door?")
            escape = escape.lower()
            if "yes" in escape:
                player.room = Wonderland['WonderWorld']
                player.item.remove("Mysterious looking Brownie")
                continue
            else:
                print("You have been buried alive")
                break     
        elif 'Mysterious looking Brownie' not in player.item:
            print('Dirt begins to fall from the ceiling...there is no escape...perhaps you should have eaten the brownie')
            break 
    
    if "Broomstick" in player.item:
        choices = ["north", "east", "west", "south", "magic", "fly"]
        Choices = False
        while Choices == False:
            users_choice = input("Please choose north, east, west, south, magic, or fly: \n ")
            print('----------------------------------------')
            if users_choice == 'q':
                Quit_Choice = True 
                break
            elif users_choice not in choices:
                print("That is not a valid direction")
            elif users_choice in choices:
                Choices = True
           
        directions = [player.room.n_to, player.room.e_to, player.room.w_to, player.room.s_to, player.room.magic_to, player.room.fly_to]
        path_dict = dict(zip(choices, directions))
    
    else:
        choices = ["north", "east", "west", "south", "magic"]
        Choices = False
        while Choices == False:
            users_choice = input("Please choose north, east, west, south, magic: \n ")
            print('----------------------------------------')
            if users_choice == 'q':
                Quit_Choice = True 
                break  
            elif users_choice not in choices:
                print("That is not a valid direction")
            elif users_choice in choices:
                Choices = True
                   
        directions = [player.room.n_to, player.room.e_to, player.room.w_to, player.room.s_to, player.room.magic_to]
        path_dict = dict(zip(choices, directions))

    #consolidated all directions into one for loop!    
    for key, value in path_dict.items():
        if users_choice == key:
            if value is not None:
                player.room = value
            
                print(player.room.description)
                print('----------------------------------------')
                if len(player.room.enemies) >=1:
                    print(f" {player.room.enemy_description}")
                    print('----------------------------------------')
                    
                    #trying new format for battles
                    if player.room.name == "Ogre King's Lair":
                        
                        Special_Weapon = False
                        while Special_Weapon == False:
                                                        
                            if "Diamond Sword" not in player.item or "Glowing Orb" not in player.item:
                                player.lives = 0
                                print("The king's skin is impenetrable without the special weapon!")
                                print('----------------------------------------') 
                                break 
                            else:
                                print("You wield the special weapon...strike now!")
                                print('----------------------------------------')
                                Special_Weapon = True 

                    Enemy_hp = player.room.enemyHP 
                    while Enemy_hp >0 and player.lives > 0:
                        

                        print(f"You have {round(player.lives,1)} lives, let the battle begin!")
                        attack = round(random.uniform(0, (player.room.enemyHP * player.room.enemy_diff)), 1) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                        print(f"You prepare to battle the {player.room.enemies} with {Enemy_hp} hitpoints left. You attack for {round(attack,1)} damage !")
                                                        
                        if attack >= Enemy_hp:
                            player.lives += (1/ player.room.enemy_diff)
                            player.level += (.1 / player.room.enemy_diff)
                            print(f"You have defeated the {player.room.enemies} with {round(player.lives,1)} lives left!")
                            print(f"You gain {round(.1 / player.room.enemy_diff ,2)} lives")
                            print('----------------------------------------')
                            break 
                        else:
                            player.lives -=1
                            if player.room.enemies.endswith('s'):
                                print(f"The {player.room.enemies} have injured you!")
                                print('----------------------------------------') 
                            else:
                                print(f"The {player.room.enemies} has injured you!")
                                print('----------------------------------------') 
                            Enemy_hp = round(Enemy_hp-attack,1) 

                    if player.lives  <= 0:

                        print(f"You have died to the {player.room.enemies}!")
                        break                 


                if len(player.room.item) < 1:
                    continue
                
                counter = 0
                len_items_in_bag = len(player.room.item)
                for item in player.room.item:
                    if item in player.item:
                        counter +=1
                if counter == len_items_in_bag:
                    counter = 0
                    continue
                
                else:
                    
                    counter = 0
                    print(f"You find {player.room.item}")
                    if len(player.item) >0:
                        print(f"You currently possess{player.item}")
                    print("-------------------------")
                    
                    for treasure in player.room.item:
                        player.describe_power(treasure)

                    item_choice = input("Which item will you pickup? Or say pass to move on: \n")
                                      

                    choice = False
                    while choice == False:
                        if item_choice == 'q':
                            Quit_Choice = True
                            break 
                        elif item_choice == 'pass':
                            choice = True 

                        elif item_choice not in player.room.item or item_choice in player.item:
                            item_choice = input("Which item will you pickup? Or say 'pass' to move on: \n")
                            continue 
                                                
                        elif item_choice in player.room.item and item_choice not in player.item:
                            if len(player.item) <5:
                                player.item.append(item_choice)    
                                                                            
                            elif len(player.item) >= 5:
                                print("You currently have too many items in your bag")
                                print(f"You currently possess {player.item}")
                                
                                choice2 = False
                                while choice2 == False:
                                    swap_choice = input("Please choose an item to swap from your bag, or pass to continue with your current bag: ")
                                    
                                    if swap_choice in player.item:
                                        player.item.remove(swap_choice)
                                        player.item.append(item_choice)
                                        choice2 = True 
                                    elif swap_choice == 'pass':
                                        choice2 = True 
                                   
                            choice = True                 
                    
                    if item_choice == 'q':
                        break 
                    
                    print("----------------------------------")
                    print(f"You currently possess {player.item}")

            else:
                print("----------------------------------")
                print('You can not go in that direction!')
                continue