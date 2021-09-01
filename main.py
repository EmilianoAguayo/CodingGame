import sys
import math
import numpy as np

class Coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def get_coordinate(self):
        return self.x,self,y


class Geometry():
    def __init__(self):
        pass
    
    def distance_calculation(self,automaton1,automaton2):
        dist = math.sqrt((automaton2.coordinate.x-automaton1.coordinate.x) ** 2+(automaton2.coordinate.y-automaton1.coordinate.y) ** 2)
        return dist


class Automaton():
    def __init__(self,coordinate,coordinate_next):
        self.coordinate = coordinate
        self.coordinate_next = coordinate_next

    def get_coordinates(self):
        return self.coordinate
    

class Human(Automaton):
    def __init__(self,coordinate,id_human):
        super().__init__(coordinate,coordinate)
        self.id_human = id_human
        
class Zombie(Automaton):
    def __init__(self,coordinate,coordinate_next,id_zombie):
        super().__init__(coordinate,coordinate_next)
        self.id_zombie = id_zombie
        self.coordinate_next = coordinate_next

class Hunter(Automaton):
    def __init__(self,coordinate):
        super().__init__(coordinate,coordinate)

# Save humans, destroy zombies!
def straight_line(ash_x,ash_y,dest_x,dest_y):

    return dest_x,dest_y

# game loop
dist_human_ash = []
dist_zombie_human = []
geometry = Geometry()
humans = []
zombies = []
centinela = 0

while True:
    x, y = [int(i) for i in input().split()]
    hunter = Hunter(Coordinate(x,y))
    print("Hunter coordinates... {} {}".format(x,y), file=sys.stderr, flush=True)
    human_count = int(input())
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        coordinate = Coordinate(human_x,human_y)
        human = Human(coordinate,human_id)
        humans.append(human)

    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        coordinate = Coordinate(zombie_x,zombie_y)
        coordinate_next = Coordinate(zombie_xnext,zombie_ynext)
        zombie = Zombie(coordinate,coordinate_next,zombie_id)
        zombies.append(zombie)

    
    closest_zombie_list =[]
    human_to_save_list = []
    zombies_ids = []
    for i in range(zombie_count):
        min_dist = 18000
        for zombie in zombies:
            for human in humans:

                if zombie.id_zombie not in zombies_ids:
                    dist = geometry.distance_calculation(zombie,human)
                    if dist <= min_dist:
                        min_dist = dist
                        closest_zombie = zombie
                        human_to_save = human
        closest_zombie_list.append(closest_zombie)
        zombies_ids.append(closest_zombie.id_zombie)
        human_to_save_list.append(human_to_save)

    #iterate throguh possible human-zombie 
    for ii in range(len(human_to_save_list)):
        human= human_to_save_list[ii]
        zombie= closest_zombie_list[ii]
        dist_1 = geometry.distance_calculation(hunter,human)
        dist_2 = geometry.distance_calculation(zombie,human)
 
        # condition to check if hunter ash can save at least one (will break if not)
        if float((dist_1-2000)/1000) < float((dist_2+400)/400):
            #it can save human
            midpoint = [round((human.coordinate.x+zombie.coordinate.x)/2),round((human.coordinate.y+zombie.coordinate.y)/2)]
            midpoint = [round((midpoint[0]+zombie.coordinate.x)/2),round((midpoint[1]+zombie.coordinate.y)/2)]
            break
            
    print("trying to save human id {}".format(human.id_human), file=sys.stderr, flush=True)
    print("Midpoint... {}".format(midpoint), file=sys.stderr, flush=True)
    print("{} {}".format(midpoint[0],midpoint[1]))
    
    centinela += 1
    zombies.clear()
    humans.clear()