Python sinflari va ob'ektlari
Python sinflari/ob'ektlari
Python - bu ob'ektga yo'naltirilgan dasturlash tili.

Python-da deyarli hamma narsa o'zining xususiyatlari va usullari bilan ob'ektdir.

Sinf ob'ekt konstruktori yoki ob'ektlarni yaratish uchun "loyiha"ga o'xshaydi.

Sinf yaratish
Sinf yaratish uchun class kalit so'zidan foydalaning:

Misol o'z Python serveringizni oling
X nomli xususiyatga ega MyClass nomli sinf yarating:

MyClass sinfi: 
x = 5
Ob'ekt yaratish
Endi biz obyektlarni yaratish uchun MyClass nomli sinfdan foydalanishimiz mumkin:

Misol
p1 nomli ob'ekt yarating va x qiymatini chop eting:

p1 = MyClass()
chop etish (p1.x)
__init__() usuli
Yuqoridagi misollar eng oddiy shakldagi sinflar va ob'ektlar bo'lib, ular haqiqiy hayotda qo'llanilmaydi.

Sinflarning ma'nosini tushunish uchun biz o'rnatilgan __init__() usulini tushunishimiz kerak.

Barcha sinflarda __init__() deb nomlangan usul mavjud bo'lib, u har doim sinf ishga tushirilganda bajariladi.

Ob'ekt xususiyatlariga qiymatlarni belgilash yoki ob'ekt yaratilayotganda bajarilishi kerak bo'lgan boshqa operatsiyalar uchun __init__() usulidan foydalaning:

Misol
Person nomli sinf yarating, ism va yosh uchun qiymatlarni belgilash uchun __init__() usulidan foydalaning:

sinf odami: 
def __init__ (o'zini, ismi, yoshi): 
self.name = ism 
self.age = yosh

p1 = Shaxs("Jon", 36)

chop etish (p1.name)
chop etish (p1.yosh)
Eslatma: __init__() usuli har safar yangi ob'ekt yaratish uchun sinfdan foydalanilganda avtomatik ravishda chaqiriladi.

REKLAMA

__str__() usuli
__str__() usuli sinf obyekti satr sifatida taqdim etilganda nima qaytarilishi kerakligini nazorat qiladi.

Agar __str__() usuli o'rnatilmagan bo'lsa, ob'ektning satr tasviri qaytariladi:

Misol
Ob'ektning __str__() usuli YO'Q string tasviri:

sinf odami: 
def __init__ (o'zini, ismi, yoshi): 
self.name = ism 
self.age = yosh

p1 = Shaxs("Jon", 36)

chop etish (p1)
Misol
__str__() usuli BILAN ob'ektning satr tasviri:

sinf odami: 
def __init__ (o'zini, ismi, yoshi): 
self.name = ism 
self.age = yosh 

def __str__(self): 
f"{self.name}({self.age})"ni qaytaring

p1 = Shaxs("Jon", 36)

chop etish (p1)
Usullarni yaratish
Ob'ektlar ichida o'z uslublaringizni yaratishingiz mumkin. Ob'ektlardagi usullar ob'ektga tegishli funktsiyalardir.

Keling, Person sinfida usul yarataylik:

Misol
Salomni chop etuvchi funksiyani kiriting va uni p1 obyektida bajaring:

sinf odami: 
def __init__ (o'zini, ismi, yoshi): 
self.name = ism 
self.age = yosh 

def myfunc(self): 
print("Salom mening ismim " + self.name)

p1 = Shaxs("Jon", 36)
p1.myfunc()
Eslatma: Self parametri sinfning joriy nusxasiga havola bo'lib, sinfga tegishli o'zgaruvchilarga kirish uchun ishlatiladi.

O'z-o'zidan parametr
Self parametri sinfning joriy nusxasiga havola bo'lib, sinfga tegishli o'zgaruvchilarga kirish uchun ishlatiladi.

U o'zini deb nomlanishi shart emas, siz uni xohlaganingizcha chaqirishingiz mumkin, lekin u sinfdagi har qanday funktsiyaning birinchi parametri bo'lishi kerak:

Misol
Self o‘rniga mysillyobject va abc so‘zlarini ishlating:

sinf odami: 
def __init__ (mysillyobject, ism, yosh): 
mysillyobject.name = ism 
mysillyobject.age = yosh 

def myfunc(abc): 
print("Salom mening ismim" + abc.name)

p1 = Shaxs("Jon", 36)
p1.myfunc()
Ob'ekt xususiyatlarini o'zgartirish
Quyidagi kabi ob'ektlardagi xususiyatlarni o'zgartirishingiz mumkin:

Misol
p1 yoshini 40 ga belgilang:

p1.yosh = 40
Ob'ekt xususiyatlarini o'chirish
Del kalit so'zidan foydalanib, ob'ektlardagi xususiyatlarni o'chirishingiz mumkin:

Misol
p1 ob'ektidan age xususiyatini o'chiring:

del p1.age
Ob'ektlarni o'chirish
Ob'ektlarni del kalit so'zidan foydalanib o'chirishingiz mumkin:

Misol
p1 ob'ektini o'chirish:

del p1
O'tish bayonoti
sinf ta'riflari bo'sh bo'lishi mumkin emas, lekin agar sizda biron sababga ko'ra kontentsiz sinf ta'rifi mavjud bo'lsa, xatolikka yo'l qo'ymaslik uchun pass bayonotini kiriting.

Misol
sinf odami: 
o'tish