import bunny
import bunnygrid_rev2 as bunnygrid
import Names
import random
import msvcrt

def main():
    juv_sexes = ["m","f"]
    juv_colors = ["White","Brown","Black","Spotted"]
    bunnies = []
    females = []
    males = []
    kill = bunnygrid.GridBunny.kill
    grid = bunnygrid.GridBunny.Grid()
    assign = bunnygrid.GridBunny.assign
    for i in range(0,5):
        random.seed()
        sex_temp = random.choice(juv_sexes)
        random.seed()
        color_temp = random.choice(juv_colors)
        grid[(i,0)].assign(bunnygrid.GridBunny(sex_temp,Names.Name.name(sex_temp),color_temp,(i,0)),grid)
    #print(grid)
    while not is_grid_empty(grid):
        print("-"*200)
        for gridbunnie in grid:
                grid = grid[gridbunnie].tick(grid)
                if grid[gridbunnie].sex == "F" : females.append(grid[gridbunnie].coords)
                if grid[gridbunnie].sex == "M" : males.append(grid[gridbunnie].coords)

        #print(str(bunnygrid.GridBunny.occupied_cells(grid)))
        for male in males:
            for female in females:
                #print("Recreation")
                grid = bunnygrid.GridBunny.Recreation(male,female,grid)
        print('\n'.join([','.join([str(grid[(i,j)].sex) for i in range(0,80)]) for j in range(0,80)]).replace("U"," "))
        #print ([str(i) for i in map(lambda x: grid[x].sex, grid)])
        females =[]
        males = []
        if msvcrt.kbhit():
                occupied_cells = bunnygrid.GridBunny.occupied_cells
                if ord(msvcrt.getch()) == 107:
                    print ("killing half the bunnies")
                    kill = bunnygrid.GridBunny.kill
                    for i in range(0,int((len(GridBunny.occupied_cells(grid))/2))):
                        bunco = random.choice(occupied_cells(grid))
                        grid[bunco].kill(grid)
def is_grid_empty(grid):
    res=True
    for index in grid:
        if grid[index].sex != "U":
            res = False
            break
    return res
if __name__ == "__main__":
    main()
