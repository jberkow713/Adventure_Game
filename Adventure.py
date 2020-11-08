from Room import Room, Monster
from Player import Player 
# Declare all the rooms
import random

room = {
'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["Body Armor" ], ["There are no enemies here..."]),

'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", "snakes", 4, ["sword", "helmet"], ["Snakes...why did it have to be snakes?"]),

'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "goblins", 12, ["key", "bomb"], ["Out of nowhere come three scary goblins"]),

'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "mummies", 15, ["bow", "arrows"], ["A group of Mummies lumber towards you"]),

'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. """, "red dragon", 40 , ["diamond", "Arkenstone"], ["A giant Red Dragon approaches"]),

'Cave Exit': Room("Cave Exit", """You have free solod your way out of the treasure room to the opening above, 
the sun greets you as you claw your way through the rocks to a giant open field""", [], 0 ),

'Enchanted Forest': Room("Enchanted Forest", """As you enter the woods you feel a bit funny...You turn around to 
retreat, only to find that you are completely lost""", "giant spider", 80, ['Ocarina', 'Bag of marbles'], ['From the treetops, a giant spider \
descends upon you!']),

'Magical Entrance': Room("Magical Entrance", """The forest has captured you and brought you here...A world of wonder and magic
await you now! Beware the beasts that dwell within!""",[], 0, ['Magic Cloak', 'Crystal Sword', 'Wand of Death']),

'Cauldron Room': Room("Cauldron Room", """In the center of the room lies a large cauldron...it is bubbling.""", "witch", 185,
['Broomstick', 'Glowing Candle'], ['As you enter the room, a witch flies down from the ceiling to attack you!']),

'Wizard training room':Room("Wizard Training Room", """Wizards are battling it out in the corner...they spot you...""", "wizard", 140, 
['Enchanted Staff', 'Boomerang'], ['The head Wizard aims his wand at you']),

'Cloud Fortress': Room("Cloud Fortress", """You jump off of the broomstick and land at the gates of a mighty fortress, high up on a magical floating cloud city""", [], 0 ),
'Mysterious Shack': Room("Mysterious Shack", """You arrive at an old run down shack in the middle of the clouds\
    what on earth is this thing doing here???""", [], 0, ['Glowing Orb']),  
'Rabbit Hole': Room("Rabbit Hole", """You fall down a giant hole within the hut, in front of you is a tiny door""", [], 0, ['Mysterious looking Brownie'] )         
}





Wonderland = {'WonderWorld': Room('WonderWorld', """As you fit through the miniature door, a vast forest lies before you""", [], 0)

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
# room['Mysterious Shack'].n_to = room['Castle Gates']
# room['Castle Gates'].s_to = room['Mysterious Shack']
# room['Castle Gates'].n_to = room['Ogre Fortress']
# room['Ogre Fortress'].s_to = room['Castle Gates']
# room['Ogre Fortress'].n_to = room["Ogre King's Lair"]
# room['Ogre Fortress'].e_to = room['Ogre Fortress East']
# room['Ogre Fortress'].w_to = room['Ogre Fortress West']
# room["Ogre King's Lair"].s_to = room['Ogre Fortress']
# room['Ogre Fortress East'].e_to = room['Ogre Fortress']
# room['Ogre Fortress West'].w_to = room['Ogre Fortress']

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


while True:
    #Set attributes at start of every battle
    if player.lives <=0:
        print("Your journey has ended, but we all must fade someday...try again soon!")
        break 
    print('----------------------------------------')
    print('----------------------------------------')
    print('----------------------------------------')
    print(f"You are currently in the {player.room.name}")
    print('----------------------------------------')        
    
    player.set_player_attributes(difficulty_choice)

    #lives, level, and magic level are based on experience and defeating monsters, they can not reset
    # player.lives = round((player.lives * player.level * player.magic_level),1)
    print(f"Your current level is {round(player.level, 1)}, your current magic level is {round(player.magic_level,1)}")
    print('----------------------------------------')
    print(f"You currently have {player.lives} lives left.")
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
            if escape == "yes":
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
        users_choice = input("Please choose north, east, west, south, magic, or fly: \n ")
        print('-----------------------------------------------')
    else:
        users_choice = input("Please choose north, east, west, south, magic: \n ")
        print('--------------------------------------------------')      


    print('----------------------------------------')
    
    choices = ["north", "east", "west", "south", "magic", "fly"]
       
    directions = [player.room.n_to, player.room.e_to, player.room.w_to, player.room.s_to, player.room.magic_to, player.room.fly_to]
    path_dict = dict(zip(choices, directions))


    if users_choice == "q":
        print("Your journey has ended!")
        break
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
                    #check if enemy exists
                    #check which room in to adapt the battle
                    if player.room.name  == "Foyer":
                        while player.lives > 0:
                            print(f"You have {player.lives} lives, let the battle begin!")
                            #attack is improved based on your inventory which improves attributes
                            attack = ((random.randint(0, 10)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level)
                            
                                                    
                            print(f"You prepare to battle the snakes with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage !")
                            
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.02
                                print(f"You have defeated the Snakes with {player.lives} lives left, you may continue on!")
                                print('----------------------------------------')
                                break
                            else:
                                player.lives -=1
                                print("The snakes have bitten you!")
                                print('----------------------------------------')
                                                
                        #check to see if player died during battle
                        if player.lives  <= 0:
                            print("You have died to a few wimpy snakes!")

                            break 

                    elif player.room.name == "Grand Overlook":
                        while player.lives >0:
                            print(f"You have {player.lives} lives, let the battle begin!")

                            attack = (random.randint(0, 20)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                            
                            print(f"You prepare to battle the Goblins with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.04
                                player.magic_level +=.02
                                print(f"You have defeated the Goblins with {player.lives} lives left!")
                                print('----------------------------------------')
                                break                                  
                            else:
                                player.lives -=1
                                print("The Goblins have injured you with their knives!")
                                print('----------------------------------------')
                        
                                                
                        if player.lives  <= 0:
                            print("The Goblins have smashed you to pieces!")                       
                            break 


                    elif player.room.name == "Narrow Passage":
                        while player.lives > 0:
                            print(f"You have {player.lives} lives, let the battle begin!")
                            
                            attack = (random.randint(0, 25)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                           
                            print(f"You prepare to battle the lurking mummies with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.06
                                print(f"You have defeated the Mummies with {player.lives} lives left!")
                                print('----------------------------------------')
                                break
                            else:
                                player.lives -=1
                                print("The mummies have begun to mummify you!")
                                print('----------------------------------------')
                        
                                                
                        if player.lives  <= 0:
                            print("The mummies have entombed you for eternity!")
                                            
                            break 

                    elif player.room.name == "Treasure Chamber":
                        while player.lives >0:
                            print(f"You have {player.lives} lives, let the battle begin!")

                            attack = (random.randint(0, 50)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                            
                            print(f"You prepare to battle the giant beast with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.1
                                player.magic_level +=.08
                                print(f"You have defeated the Dragon with {player.lives} lives left!")
                                print('----------------------------------------')
                                break 
                            else:
                                player.lives -=1
                                print("The monstrous claws of the red beast descend upon your head!")
                                print('----------------------------------------')
                                                
                        if player.lives  <= 0:
                            print("Fire reigns down upon your head, you have been engulfed in flames!")
                                            
                            break    
                    elif player.room.name == "Enchanted Forest":
                        while player.lives >0:
                            
                            print(f"You have {player.lives} lives, let the battle begin!")
                            attack = (random.randint(0,100)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                            
                            print(f"You prepare to battle the evil spider with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.15
                                player.magic_level +=.15
                                print(f"You have defeated the wretched monstrosity with {player.lives} lives left!")
                                print('----------------------------------------')
                                break 
                            else:
                                player.lives -=1
                                print("The spider has you trapped in her web!")
                                print('----------------------------------------')
                       
                        
                        if player.lives  <= 0:
                            print("The spider feasts upon your flesh!")
                            break    
                   
                    elif player.room.name == "Cauldron Room":
                        
                        while player.lives >0:
                            
                            print(f"You have {player.lives} lives, let the battle begin!")
                            attack = (random.randint(0,150)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                            
                            print(f"You prepare to battle the Wicked Witch with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.2
                                player.magic_level +=.2
                                print(f"You have defeated the wretched monstrosity with {player.lives} lives left!")
                                print('----------------------------------------')
                                break 
                            else:
                                player.lives -=1
                                print("The witch has poisoned you with her dark magic!")
                                print('----------------------------------------')
                       
                        
                        if player.lives  <= 0:
                            print("The witch has thrown you in her cauldron, and there you will stay!")
                            break 

                    elif player.room.name == "Wizard Training Room":

                        while player.lives >0:
                            
                            print(f"You have {player.lives} lives, let the battle begin!")
                            attack = (random.randint(0,200)) * player.attack * player.magic_attack * player.defense * player.level * player.magic_level
                           
                            print(f"You prepare to battle the mighty wizard with {player.room.enemyHP} hitpoints, you attack for {round(attack,1)} damage")
                            
                            if attack >= player.room.enemyHP:
                                player.lives +=1
                                player.level +=.25
                                player.magic_level +=.25
                                print(f"You have defeated the conjurer of doom with {player.lives} lives left!")
                                print('----------------------------------------')
                                break 
                            else:
                                player.lives -=1
                                print("The wizard has hit you with a fireball!")
                                print('----------------------------------------')
                       
                        
                        if player.lives  <= 0:
                            print("The wizard has incinerated you with his unending barrage of death!")
                            break 




                if len(player.room.item) < 1:
                    continue
                else:
                
                    print(f"You find {player.room.item}")
                    if len(player.item) >0:
                        print(f"You currently possess{player.item}")
                    print("-------------------------")
                    
                    for treasure in player.room.item:
                        player.describe_power(treasure)
                
                    item_choice = input("Which item will you pickup? Or say pass to move on: \n")
                    
                    choice = False
                    while choice == False:
                        
                        if item_choice == 'pass':
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

                                swap_choice = input("Please choose an item to swap from your bag, or pass to continue with your current bag: ")
                                choice2 = False
                                while choice2 == False:
                                    if swap_choice in player.item:
                                        player.item.remove(swap_choice)
                                        player.item.append(item_choice)
                                        choice2 = True 
                                    elif swap_choice == 'pass':
                                        choice2 = True 
                                    else:
                                        swap_choice = input("Please choose an item to swap from your bag, or pass to continue with your current bag: ")
                                        

                            choice = True                 
                    print("----------------------------------")
                    print(f"You currently possess {player.item}")

            else:
                print("----------------------------------")
                print('You can not go in that direction!')
                continue

                
            