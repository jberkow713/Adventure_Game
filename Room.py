# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, number, world,  name, description,  enemies, enemyHP, enemy_diff, companion=[], item=[] ,enemy_description=[]  ):
        self.number = number 
        self.name = name
        self.world = world 
        self.description = description
        self.item = item
        self.enemies = enemies
        self.enemyHP = enemyHP
        self.enemy_description = enemy_description
        self.enemy_diff = enemy_diff 
        self.companion = companion 
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.magic_to = None
        self.fly_to = None   
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__) 

class Monster:
    def __init__(self, name,  ability):
        self.name = name
        self.ability = ability 

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)             
class MagicRoom(Room):
    def __init__(self, name, description, enemies, enemyHP, enemy_diff, companion, item=[] ,enemy_description=[]):
        super().__init__ (name, description,  enemies, enemyHP, enemy_diff, item=[], enemy_description=[] )
        self.companion = companion
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.magic_to = None
        self.fly_to = None   
        




Map = { 1: [2,0,0,0,0,0], 2: [3,1,4,0,0, 0], 3: [0,2,0,0,0, 0], 4: [5,0,0,2,0, 0], 5: [6,4,0,0,0, 0], 6: [0,5,7,0,0, 0], \
     7: [0,0,0,6,8, 0], 8: [9,0,10,0,7, 0], 9: [0,8,0,0,0, 11], 10: [0,0,0,8,0, 0], 11: [0,0,12,0,0, 9], 12: [14,0,0,0,13, 0], \
         13: [0,0,0,0,0, 0], 14: [15,12,0,0,0, 0], 15: [16,14,0,0,0, 0], 16: [0,15,0,0,0, 0], 17: [18,0,0,0,0, 0], 18: [0,17,0,0,0, 0]\
}





