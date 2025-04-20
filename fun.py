import random
import string
import statistics  
class Soldier:
    def __init__(self, name):
        self.name = name
        self._generate_random_attributes()
    def _generate_random_attributes(self):
        self.random_int = random.randint(1, 100)
        self.random_float = random.random()
        self.random_char = random.choice(string.ascii_lowercase)
        self.random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
        self.random_bool = random.choice([True, False])
        return      
Try_Dict = {}
for k in range(5):
    Tries = []
    for i in range(5):
        Count = 'low'
        tries = 0
        while Count =='low':
            count = 0
            for i in range(50):
                s = Soldier('james')
                if s.random_bool == True:
                    count +=1 
            tries +=1        
                
            if count >=35:
                Count ='high'
                print(s.__dict__)
                Tries.append(tries)
    Try_Dict[k]=sum(Tries)/len(Tries)         
print(Try_Dict)
print(f'mean is {sum(Try_Dict.values())/len(Try_Dict)}')
print(f'standard deviation is {statistics.stdev(Try_Dict.values())}')  