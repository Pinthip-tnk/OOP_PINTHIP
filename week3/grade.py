print("โปรแกรมคำนวณเกรดเฉลี่ย")
score = int(input("ใส่คะแนน  : "))
if score <= 0 :
    print('กรอกคะแนนใหม่อีกครั้ง !')
elif score > 100:
    print('กรอกคะแนนใหม่อีกครั้ง !')
elif score >= 80:
    print('คุณได้เกรด 4')
elif score >= 70:
    print('คุณได้เกรด 3')
elif score >= 60:
    print('คุณได้เกรด 2')
elif score >= 50:
    print('คุณได้เกรด 1')
else :
    print('คุณได้เกรด 0')
    
    print("คุณอยากสอบแก้ไหม ถ้าสอบแก้ พิมพ์ 1 ไม่สอบแก้พิมพ์ 2")
    click = int(input("กรุณาเลือก : "))
    if click == 1:
        print("คุณต้องการคะแนนอีก", 50 - score, "คะแนน ถึงคุณจะผ่าน")
    elif click == 2:
        print("คุณสอบตก")
    else :
        print("กรุณาเลือก 1 หรือ 2")
