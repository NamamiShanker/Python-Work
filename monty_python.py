import numpy as np
import random

def create_doors(n=4):     ## Creates n doors
    k=1
    prize = random.sample(range(n), k)
    doors = np.zeros(n, dtype=bool)
    doors[prize] = True
    return (doors, prize)


def choose_stay(doors):         ## Chooses a door and doesn't change the decision later                     ###Returns true if won
    return random.choice(doors) # Since we are not changing choice there is no need to
                                # simulate opening a door
                                

def choose_switch(doors, prize, k):      ##  Choose a door and switches after k doors are opened           ###Returns true if won
    if k>len(doors)-2:
        raise Exception("ERROR: Wrong number of doors opened")
    choice = random.randrange(len(doors))   # Choosing a random door
    temp = np.arange(len(doors))
    temp = temp[temp!=choice]
    temp = temp[temp!=prize]
    doors_opened = random.sample(list(temp), k)
    for door in doors_opened:
        temp = temp[temp!=door]
    temp = np.append(temp, prize)
    choice = random.choice(temp)
    return choice==prize
    
    
    
def main():                     ## A code to compare 100 samples
    t = int(input("Enter the no. of times the test to run: "))
    
    counter_stay = 0
    counter_switch_1 = 0
    counter_switch_2 = 0
    
    for i in range(t):
        doors, prize = create_doors()
        if(choose_stay(doors)):
            counter_stay+=1
        if(choose_switch(doors, prize, 1)):
            counter_switch_1+=1
        if(choose_switch(doors, prize, 2)):
            counter_switch_2+=1

    print("No. of times won when not switching:", counter_stay)
    print("No. of times won when switching with 1 doors opened:", counter_switch_1)
    print("No. of times won when switching with 2 doors opened:", counter_switch_2)
        

if __name__ == "__main__":
    main()
