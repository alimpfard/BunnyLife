import random
class Name:

    def __init__(self):
        pass
    def name(sex):
        random.seed()
        Names_m = ["Thumper","Oreo","Oliver","Charlie","Coco","Pico","Jack","Peanut","Clover","Willow","Bailey"]
        Names_f = ["Daisy","Bella","Lola","Lily","Lucy","Thumper","Peanut","Clover","Molly","Bunbun","Pepper"]
        rnd = random.randint(0,min(len(Names_m)-1 , len(Names_f)-1))
        if sex=="m" : return Names_m[rnd]
        else: return Names_f[rnd]
