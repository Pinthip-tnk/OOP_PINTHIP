class Cat:
    def __init__(self, ชื่อ,อายุ, เพศ,สี):
       self.name = ชื่อ
       self.age = อายุ
       self.gender = เพศ
       self.color = สี
    def old(self):
       self.age += 1
cat1 = Cat (ชื่อ = 'ศรีทอง', อายุ = 4 , เพศ = 'ตัวผู้' , สี = 'สีดำ')
cat2 = Cat ("ศรีเงิน" , 5 ,"ตัวเมีย" , "สีขาว")
#cat2.name = "ศรี"
#cat2.age += 5
cat2.old()
print(cat2.age)