print ("ประวัติส่วนตัว")
name = str(input('กรุณากรอกชื่อ-นามสกุล : '))
nickname = str(input('กรุณากรอกชื่อเล่น :'))
age = int(input('กรุณากรอกอายุ : '))
ID = int(input('กรุณากรอกเลขประจำตัวนักศึกษา :'))
level = int(input('กรุณากรอกระดับชั้น : '))
height = float(input('กรุณากรอกส่วนสูง : '))
weight = float(input(' กรุณากรอกน้ำหนัก : '))
result = height+weight
print(f"ชื่อ: {name} , ชื่อเล่น: {nickname}")
print(f"อายุ: {age} , รหัสประจำตัวนักศึกษา: {ID} , ระดับชั้น: {level}")
print(f"ส่วนสูง: {height} , น้ำหนัก: {weight}")
print(f"ส่วนสูง + น้ำหนัก = {result}")