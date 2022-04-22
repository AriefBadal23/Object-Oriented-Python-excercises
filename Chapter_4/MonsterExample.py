import random


class Monster():
    def __init__(self, n_rows, n_cols, max_speed):
        self.n_rows = n_rows # save away
        self.n_cols = n_cols # save away
        self.my_Row = random.randrange #chooses a random row
        self.my_Col = random.randrange(self.n_cols) # choose a random col
        self.my_SpeedX = random.randrange(-max_speed, max_speed + 1) #choose a Y speed
        # Set other instance variables like health, power, etc.

        def move(self):
            self.my_Row = (self.my_Row + self.mySpeedY) % self.n_rows
            self.my_Col = (self.my_Col + self.mySpeedX) % self.n_cols


N_MONSTERS = 20
N_ROWS = 100
N_COLS = 200
MAX_SPEED = 4



monsterlist = [] # start with an empty list
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_ROWS, MAX_SPEED) # create a monster
    monsterlist.append(oMonster) # add Monster to our list


for oMonster in monsterlist:
    oMonster.move()





