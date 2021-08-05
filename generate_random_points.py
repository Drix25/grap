import random
import json

INT_SIZE = 1000000
DICT_PTS = []

def randInt(maxVal=2000):
    return random.randint(0,maxVal+1)

for i in range(INT_SIZE+1):
    DICT_PTS[i] = {"x":randInt(),"y":randInt()}
    
with open("data.json","w") as fp:
    json.dump(DICT_PTS,fp)