import random
from Names import Name as Name
import time
import bunny

class GridBunny:

        def __init__(self, sex, name, color,coords, parents = []):
            self.sex = sex
            self.name = name
            self.color = color
            self.age = 0
            self.parents = parents
            self.coords = coords
            #print (parents)
            try:
                self.id = (parents[1].id + parents[0].id + 1)
            except:
                self.id = 0

        def Grid():
            grid = {}
            for x in range(0,80):
                for y in range(0,80):
                    grid[(x,y)] = GridBunny("U","","",(x,y),[])
            return grid

        def emptycells(self,grid):
            emptycells_list = []
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    try:
                        if (self.coords[0]+i,self.coords[1]+j) in grid and grid[(self.coords[0]+i,self.coords[1]+j)].sex == "U": emptycells_list.append((self.coords[0]+i,self.coords[1]+j))
                    except Exception as e: print(str(e))
            return emptycells_list

        def assign(self,other,grid):
            grid[self.coords].sex = other.sex
            grid[self.coords].name = other.name
            grid[self.coords].color = other.color
            grid[self.coords].age = other.age
            grid[self.coords].parents = other.parents
            if other.parents!=[] : grid[self.coords].id = (other.parents[1].id + other.parents[0].id + 1)
            else: grid[self.coords].id = 0
            return grid

        def GridMove(self,grid):
            assign = GridBunny.assign
            emptycells = GridBunny.emptycells
            emptycell_list = grid[self.coords].emptycells(grid)
            cell = (-1,-1)
            if emptycell_list != [] :
                try:
                    cell = random.choice(emptycell_list)
                    grid = grid[cell].assign(self,grid)
                    grid = grid[self.coords].move_kill(grid)
                except Exception as e: print(str(e))
            return (grid,cell)

        def occupied_cells(grid):
            emptycells_list = []
            for bunnie in grid:
                if grid[bunnie].sex != "U": emptycells_list.append(grid[bunnie].coords)
            return emptycells_list

        def Rad(self,grid):
            random.seed()
            if random.randint(0,100) in range(0,2):
                self.sex = "X"
                grid[random.choice(GridBunny.occupied_cells(grid))].sex = "X"
            return grid

        def bunny_pop(grid,bunnie):
            for i in range(0,len(grid)-1):
                try:
                    grid = grid[bunnie.coords].assign(GridBunny("U","","",obj.coords,[]),grid)
                except Exception as e: pass
            return grid

        def Recreation(mal,female,grid):
            random.seed(time.clock())
            random.seed(random.randint(0,1000))
            f,F,m,M,X="f","F","m","M","X"
            male = grid[mal]
            fem = grid[female]
            #print("female is "+str(fem)+"and male is "+str(male))
            color = fem.color
            if fem :
                    #print("female exists")
                    emptycells = GridBunny.emptycells
                    cells_2b = fem.emptycells(grid)
                    if cells_2b != []:
                        #print("cells exist")
                        cell = random.choice(cells_2b)
                        random.seed(random.randint(0,1000))
                        sex = random.choice(["m","f"])
                        if cell:
                            #print("single cell acquired")
                            child = GridBunny(sex,Name.name(sex),color,cell,[fem,male])
                            #print("child born: "+str(child))
                            grid = child.Rad(grid)
                            grid = grid[cell].assign(child,grid)
            return grid

        def kill(self,grid):
            return GridBunny.bunny_pop(grid,self)

        def move_kill(self,grid):
            return GridBunny.bunny_pop(grid,self)

        def tick(self,grid):
                try:
                    i+=1
                except Exception as e:
                    i=random.randint(0,100)
                random.seed(i)
                kill = GridBunny.kill
                if self.sex != "U" :
                    #grid[self.coords].age += 1
                    self.age+=1
                    moved = self.GridMove(grid)
                    if not moved[1] == (-1,-1):
                        grid = moved[0]
                        self.coords = moved[1]
                len_g = len(GridBunny.occupied_cells(grid))
                try:
                    if len_g > 1000 :
                        for i in range(0,int(len_g/2)):
                            GridBunny.bunny_pop(grid,random.choice(GridBunny.occupied_cells(grid)))
                except Exception as e: print(str(e))
                if self.sex != "X" and self.sex != "U":
                            if self.age >= 2 :
                                self.sex = self.sex.upper()
                                #grid[self.coords].sex = grid[self.coords].sex.upper()
                            if grid[self.coords].age > 10 : self = GridBunny("U","","",self.coords,[])
                elif self.sex == "X":
                    if self.age > 50:
                         self = GridBunny("U","","",self.coords,[])
                grid = grid[self.coords].assign(self,grid)
                return grid
