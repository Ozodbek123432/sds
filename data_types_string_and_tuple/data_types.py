# class Ozodbek:
#
#     def __init__(self, name):
#         self.mualif = name
#         self.book_name = "tarix"
#         self.yer_old = 2019
#
#     def get_info(self):
#         return self.mualif, self.book_name, self.yer_old
#
# obj = Ozodbek("Ozod")
# print(f"kitob malumot", obj.get_info() )
# class Ozodbek:
#
#     def __init__(self, name):
#         self.talaba = name
#         self.yoshi = 15
#         self.kurs = "03-25"
#
#     def get_info(self):
#         return self.talaba, self.kurs, self.yoshi
#
# obj = Ozodbek("Ozod")
# print(f"kitob malumot", obj.get_info() )c
# class Bank_akkount:
#     def __init__(self, name):
#         self.name = "ozodbek"
#         self.bans = 100
#     def depzit(self):
#         self.__totl_blans = self.bans + 10
#         return "ballansga 10 qoshildi "
#     def  withdraw(self):
#         return f"sizni balsingiz {self.__totl_blans} "
# obj = Bank_akkount(10000)
# print(obj.depzit())
# print(obj.withdraw())
#
# class Student:
#     def __init__(self):
#         self.__grade = 0
#
#     def set_grade(self):
#         self.__total_grade = self.__grade + 70
#         return self.__total_grade
#
#     def get_grade(self):
#         return f"sizni jami balingiz {self.__total_grade}"
#
# obj = Student()
# # print(obj.get_grade())
# class Animal:
#
#     def __init__(self):
#         self.dog = "gaf gaf"
#         self.cat = "miov miov"
#     def sound(self):
#         vov = self.dog
#         miyu = self.cat
#
# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#
#     def speak(self):
#         return f"It ning ovozi {self.speak()}"
#     def speak(self):
#         return f"cat ning ovozi {self.speak()}"