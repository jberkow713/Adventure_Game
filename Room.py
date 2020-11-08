# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description,  enemies, enemyHP, item=[] ,enemy_description=[]  ):
        self.name = name
        self.description = description
        self.item = item
        self.enemies = enemies
        self.enemyHP = enemyHP
        self.enemy_description = enemy_description
        self.n_to = None
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.magic_to = None
        self.fly_to = None   
    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__) 

class Monster:
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)             