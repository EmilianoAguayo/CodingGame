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
    
    # def distance_calculation(self,coordinate1,coordinate2):
    #     dist = math.sqrt((coordinate1.x-coordinate2.x) ** 2+(coordinate1.y-coordinate2.y) ** 2)
    #     return dist
    
    def distance_calculation(self,automaton1,automaton2):
        dist = math.sqrt((automaton2.coordinate.x-automaton1.coordinate.x) ** 2+(automaton2.coordinate.y-automaton1.coordinate.y) ** 2)
        return dist


class Automaton():
    def __init__(self,coordinate):
        self.coordinate = coordinate

    def get_coordinates(self):
        return self.coordinate
    

class Human(Automaton):
    def __init__(self,coordinate,id_human):
        super().__init__(coordinate)
        self.id_human = id_human
        
class Zombie(Automaton):
    def __init__(self,coordinate,id_zombie):
        super().__init__(coordinate)
        self.id_zombie = id_zombie

class Hunter(Automaton):
    def __init__(self,coordinate):
        super().__init__(coordinate)

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
        zombie = Zombie(coordinate,zombie_id)
        zombies.append(zombie)

    
    # Get distances
    # zombies to humans
    dist_z_h = []
    
    closest_zombie_list =[]
    human_to_save_list = []
    zombies_ids = []
    for i in range(zombie_count):
        min_dist = 18000
        for zombie in zombies:
            for human in humans:
                #dist = geometry.distance_calculation(zombie.coordinate,human.coordinate)

                if zombie.id_zombie not in zombies_ids:
                    dist = geometry.distance_calculation(zombie,human)
                    if dist < min_dist:
                        min_dist = dist
                        closest_zombie = zombie
                        human_to_save = human
        closest_zombie_list.append(closest_zombie)
        zombies_ids.append(zombie.id_zombie)
        human_to_save_list.append(human_to_save)
        # print("Min distance in humanid {} and zombieid {}".format(human.id_human,zombie.id_zombie), file=sys.stderr, flush=True)
        # array ordered by distance                

    # print("Human coordinates 1... {} {}".format(human_to_save_list[0].coordinate.x,human_to_save_list[0].coordinate.y), file=sys.stderr, flush=True)
    # print("Zombies coordinates 1... {} {}".format(closest_zombie_list[0].coordinate.x,closest_zombie_list[0].coordinate.y), file=sys.stderr, flush=True)
    # check if Ash reaches
    # dist_1 = geometry.distance_calculation(hunter,human_to_save_list[0])
    # print("Hunter to humans... {}".format(dist_1), file=sys.stderr, flush=True)
    # dist_2 = geometry.distance_calculation(closest_zombie_list[0],human_to_save_list[0])
    # print("Zombie to humans... {}".format(dist_2), file=sys.stderr, flush=True)
    
    #for array ordered by distance
    #condition
    for ii in range(len(human_to_save_list)):
        human= human_to_save_list[ii]
        zombie= closest_zombie_list[ii]
        dist_1 = geometry.distance_calculation(hunter,human)
        dist_2 = geometry.distance_calculation(zombie,human)
        print("Zombies coordinates ... {} {}".format(zombie.coordinate.x,zombie.coordinate.y), file=sys.stderr, flush=True)
        print("Human coordinates ... {} {}".format(human.coordinate.x,human.coordinate.y), file=sys.stderr, flush=True)
        print("dist 1  {}".format((dist_1-2000)/1000), file=sys.stderr, flush=True)
        print("dist_2. {}".format((dist_2+400)/400), file=sys.stderr, flush=True)
 
        if float((dist_1-2000)/1000) < float((dist_2+400)/400):
            #it can save human
            midpoint = [round((human.coordinate.x+zombie.coordinate.x)/2),round((human.coordinate.y+zombie.coordinate.y)/2)]
            break
            
    print("trying to save human id {}".format(human.id_human), file=sys.stderr, flush=True)
    print("Midpoint... {}".format(midpoint), file=sys.stderr, flush=True)
    print("{} {}".format(midpoint[0],midpoint[1]))
    
    centinela += 1
    zombies.clear()
    humans.clear()


    


    
