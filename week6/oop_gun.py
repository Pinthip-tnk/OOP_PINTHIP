class Gun:
    def __init__(self,name,ammo,hp):
       self.ชื่อ = name
       self.กระสุน = ammo 
       self.พลังชีวิต = hp
    def add_ammo(self,ammo):
        self.กระสุน += ammo
    def frie_ammo(self):
        if self.กระสุน > 0:
            self.กระสุน -= 1
        else:
            print('กระสุนหมด')
    def fire_gun(self,enemy):
        self.กระสุน -= 1
        enemy.พลังชีวิต -= 3



#gun1 = Gun("t1",2)
#gunz = Gun ("t2",0)
#gun3 = Gun("t3",5)
#gun1.add _ammo(5)
#gun2.frie_ammo()
#print(gun2.กระสุน)