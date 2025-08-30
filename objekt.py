#objekt (class)
#objeckt
class Ozodbek:
    name = "<NAME>"
    def __init__(self, name):
        self.name = name
    def spped(self, name):
        return f"mening isim {name}"

obj = Ozodbek("kesha")
print(Ozodbek.name)
#self bu kaltit
# agar clasni ichida konsturuk tir boladigan bolsa bu obeyt hsiboladigan boladi
#agar clasni ichida konstuuktir bomas bu shunchakb obeyk
#obj 2 tuga bolaind
#1 -  class atribuut
#2 - excamplary
# konsturuuktir fuksayni ichidagi malumotlarni uzatish uchun malumot klarni
#clasni ichida funksayalr
#2 xuuxuyat
#konstruktirga malumoti 3 hil yool bilanbersa boladi
class mashina:
    def __init__(self, name):
        self.brend = "car"
    def show_info(self):
        print(self.brend)