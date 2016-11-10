import random
from Names import Name as Name
from time import sleep
class Bunny:
    def __init__(self, sex, name, color, parents = []):
        self.sex = sex
        self.name = name
        self.color = color
        self.age = 0
        self.parents = parents
    def Rad(self,list):
        random.seed()
        if random.randint(0,100) in range(0,2):
            self.sex = "X"
    def choose(list):
        random.seed()
        #if r_index : return list.index(list[random.randint(0,len(list)-1)])
        return list[random.randint(0,len(list)-1)]
    def Recreation(self,other,list):
        f,F,m,M,X="f","F","m","M","X"
        if (self.sex == F or self.sex == M) and (other.sex == F or other.sex == M):
            if (self.sex == F): color = self.color
            elif other.sex == F: color = other.color
            random.seed()
            sex = f if random.randint(1,2) == 1 else m
            child = Bunny(sex,Name.name(sex),color,[self,other])
            child.Rad(list)
            print((" -> Radioactive Mutant Vampire" if self.sex == "X" else " -> " )+ "Bunny "+child.name+" Was born.")
            list.append(child)
    def kill(self,list):
        print((" -> Radioactive Mutant Vampire" if self.sex == "X" else " -> " )+ "Bunny "+ self.name  + " died.")
        list.pop(list.index(self))
    def tick(self,list):
        self.age+=1
        if len(list) > 1000 :
            for i in range(0,int(len(list)/2)):
                list.pop(list.index(Bunny.choose(list)))
        if self.sex != "X":
            if self.age>=2 : self.sex = self.sex.upper()
            if self.age > 10 : self.kill(list)
        else:
            if self.age > 50:
                self.kill(list)
            else:
                Bunny.choose(list).sex = "X"
        sleep(0.1)
