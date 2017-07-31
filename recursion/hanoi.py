
def move_tower(height, from_pole, with_pole, to_pole):
    if height >= 1:
        move_tower(height-1, from_pole, to_pole, with_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, from_pole, to_pole)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        move_disk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def move_disk(from_pole, to_pole):
    print("move disk from %s to % s"%(from_pole, to_pole))

def main():
    move_tower(5, 'A', 'B', 'C')  
    print("====")
    moveTower(5, 'A', 'C', 'B')  

if __name__ == '__main__':
    main()
