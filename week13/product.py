class Product:
    def __init__(self,brand,name,price,stock):
        self.brand = brand
        self.name = name
        self.__price = price
        self.__stock = stock

    def edit(self,val):
        if val == "editstock" :
            print('แก้ไขจำนวน')
            val_stock = int(input(f'{self.brand} ใส่จำนวน : '))
            self.__stock += val_stock
        
        elif val == "editprice":
            print('แก้ไขราคา')
            val_price = int(input(f'{self.brand} ใส่ราคา : '))
            self.__price = val_price

    def showinfo(self):
        return f"ชื่อแบรด์สินค้า: {self.brand} สินค้าชื่อ: {self.name} ราคา: {self.__price} บาท มีจำนวน: {self.__stock} ชิ้น"
    
class Mobile(Product):
    def __init__(self,brand, name, price, stock,system):
        super().__init__(brand,name, price, stock)
        self.system = system
    def showmobile(self):
        return f"{super().showinfo()}\nระบบปฏิบัติการ : {self.system}\n--------------------------------------------------------------------------------------"
    
class Notebook(Product):
    def __init__(self,brand, name, price, stock,Graphics):
        super().__init__(brand,name, price, stock)
        self.Graphics = Graphics
    def shownotebook(self):
        return f"{super().showinfo()}\nGraphics : {self.Graphics}\n--------------------------------------------------------------------------------------"
    
class Cothes(Product):
    def __init__(self,brand,name, price, stock,color):
        super().__init__(brand,name, price, stock)
        self.color = color
    def showclothes(self):
        return f"{super().showinfo()}\nสีผ้า : {self.color}\n--------------------------------------------------------------------------------------"
    
urs1 = Mobile("IPhone",15,34000,60,"IOS")
urs2 = Notebook("acer","one14",20000,10,"NVIDIA GeForce RTX 3050 Ti Laptop GPU")
urs3 = Cothes("Stussy","8 Ball Tee White",4000,1200,"White")

while True:
    print(f"ข้อมูลของ{urs1.showmobile()}")
    print(f"ข้อมูลของ{urs2.shownotebook()}")
    print(f"ข้อมูลของ{urs3.showclothes()}")
    choiec = input('จะแก้ไขข้อมูลพิมพ์ edit หรือ exit : ')
    if choiec == 'edit':
        urs1.edit("editstock")
        urs1.edit("editprice")
        urs2.edit("editstock")
        urs2.edit("editprice")
        urs3.edit("editstock")
        urs3.edit("editprice")
    elif choiec == 'exit':
        print(f"ข้อมูลของ{urs1.showmobile()}")
        print(f"ข้อมูลของ{urs2.shownotebook()}")
        print(f"ข้อมูลของ{urs3.showclothes()}")
        break
    else:
        print('ลองใหม่อีกครั้ง')