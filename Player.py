# Write a class to hold player information, e.g. what room they are in
# currently.
from Room import Room, Monster
import random
from texttest import text_box

class Player:
    def __init__(self, name, level,  defense, magic_level, room, companion=[], item=[]):
        self.room = room 
        self.name = name
        self.item = item
        self.level = level
        # self.attack = attack
        # self.magic_attack = magic_attack 
        self.magic_level = magic_level
        # self.lives = 0
        self.defense = defense
        self.invisibility = False 
        self.firebreathing = False
        self.deafening = False  
        self.companion = companion
        
        # self.size = size 
        # self.fortune = fortune
         
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)  

    def set_lives(self, difficulty_choice):
        
        difficulty_levels = ["easy", "medium", "hard", "expert"]
        lives_choices = [15, 10, 6, 3]
        lives_dict = dict(zip(difficulty_levels, lives_choices))
        for key, value in lives_dict.items():
            if difficulty_choice == key:
                Player.lives = value  
                        
    def set_initial_fortune_and_defense(self):
        # roll_1 = (random.randint(0, 100))
        roll_2 = (random.randint(0, 100))
        # roll_3 = (random.randint(0, 100))
        roll_4 = (random.randint(0, 100))
        # roll_5 = (random.randint(0, 100))

        
        Player.fortune = round(roll_2/ 50, 1)        
        Player.defense = round(roll_4/ 10, 1)
        
    def set_player_attributes(self, difficulty_choice):
            
        Player.attack = 1
        # Player.fortune = 1
        Player.magic_attack = 1    
        # Player.defense = 1 
        Player.magic_level = 1

        difficulty_levels = ["easy", "medium", "hard", "expert"]
        difficulty_multiplier = [1.2, 1.0, .8, .6]
        difficulty_dict = dict(zip(difficulty_levels, difficulty_multiplier))
        
        for key, value in difficulty_dict.items():
            if difficulty_choice == key:
                Player.attack = Player.attack * value
                
                
        
        if "Body Armor" in self.item:
            Player.lives = Player.lives * 1.1
        if "sword" in self.item:
            Player.attack = Player.attack * 1.1
        if "helmet" in self.item:
            Player.defense = Player.defense * 1.1  
        if "bomb" in self.item:
            Player.attack = Player.attack * 1.1
        if "bow" in self.item:
            Player.attack = Player.attack * 1.1
        if "arrows" in self.item:
            Player.attack = Player.attack *1.1    
        if "diamond" in self.item:
            Player.fortune = Player.fortune * 1.1
        if "Arkenstone" in self.item:
            Player.magic_attack = Player.magic_attack * 1.15
        if "Spear" in self.item:
            Player.attack = Player.attack * 1.1
        if "Ocarina" in self.item:
            Player.magic_level = Player.magic_level * 1.15
        if "Bag of marbles" in self.item:
            Player.fortune = Player.fortune * 1.1
        if "Magic Cloak" in self.item:
            Player.magic_attack = Player.magic_attack * 1.1
        if "Crystal Sword" in self.item:
            Player.attack = Player.attack * 1.2
        if "Wand of Death" in self.item:
            Player.magic_attack = Player.magic_attack * 1.2
        if "Glowing Candle" in self.item:
            Player.magic_level = Player.magic_level * 1.1
        if "Enchanted Staff" in self.item:
            Player.magic_attack = Player.magic_attack * 1.2
        if "Boomerang" in self.item:
            Player.attack = Player.attack * 1.1
              
        
        if 'Golden Axe' in self.item:
            Player.attack = Player.attack * 1.15
        
        if 'Draconis' in self.companion:
            self.firebreathing = True
                    
        if 'Archimedes' in self.companion:
            self.deafening = True     
            
            


                 

                        

    def describe_power(self, item):
        item_list = ["Body Armor", "sword", "helmet", "bomb", "bow", "arrows", "diamond", "Arkenstone", "Spear", "Ocarina",\
            "Bag of marbles", "Magic Cloak", "Crystal Sword", "Wand of Death", "Glowing Candle", "Enchanted Staff", \
                "Boomerang", "Broomstick", "Glowing Orb", 'Mysterious looking Brownie','Golden Axe',\
                    'Diamond Sword', 'Ring of invisibility'
                     ]
        item_benefit = ["Lives * 1.1", "Attack * 1.1", "Defense * 1.1", "Attack * 1.1",\
            "Attack * 1.1", "Attack *1.1 ", "Fortune * 1.1", "Magic_attack * 1.15", \
                "Attack * 1.1", "Magic_level * 1.15","Fortune * 1.1", "Magic_attack *1.1", "Attack * 1.2", \
                    "Magic_attack * 1.2", "Magic_level * 1.1", "Magic_attack * 1.2", "Attack * 1.1",\
                        "the ability to fly!", "Who knows what this does...", "miniature size", "Attack * 1.15",\
                            "The second piece towards creating a powerful weapon!", 'the ability to become invisible!'       ]
        
        
        power_dict = dict(zip(item_list, item_benefit))

        for key, value in power_dict.items():
            if item == key:
                print(f" {item} gives you {value}")
                
    

                