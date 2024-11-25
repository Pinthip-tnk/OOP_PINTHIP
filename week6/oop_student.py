import random as pinpin
class Student:
    def __init__(self,ชื่อ,ชื่อเล่น,คะแนนสอบ):
        self.name = ชื่อ
        self.nickname = ชื่อเล่น
        self.score = คะแนนสอบ
    def random(self):
        r = pinpin.randint(1,10)
        self.score += r
    def grade(self):
        if self.score >= 5 :
            print("สอบผ่าน")
        else:
            print("สอบตก")
std1 = Student(ชื่อ="รังสิมา พิเดช",ชื่อเล่น="วา",คะแนนสอบ=0)
std2 = Student(ชื่อ="ปิ่นทิพย์ รุ่งศรี",ชื่อเล่น="ปิ่น",คะแนนสอบ=0)
std3 = Student(ชื่อ="ไลลา รัตติกาล",ชื่อเล่น="ไลลา",คะแนนสอบ=0)
std4 = Student(ชื่อ="วิลัยภรณ์ กัญจนกาญจน์",ชื่อเล่น="เป้",คะแนนสอบ=0)
std5 = Student(ชื่อ="ชนันพร พิมเสนา",ชื่อเล่น="ใบมิ้น",คะแนนสอบ=0)

std1.random()
std2.random()
std3.random()
std4.random()
std5.random()

print(std1.name,std1.nickname,std1.score)
std1.grade()
print(std2.name,std2.nickname,std2.score)
std2.grade()
print(std3.name,std3.nickname,std3.score)
std3.grade()
print(std4.name,std4.nickname,std4.score)
std4.grade()
print(std5.name,std5.nickname,std5.score)
std5.grade()