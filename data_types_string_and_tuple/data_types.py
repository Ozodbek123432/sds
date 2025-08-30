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
class Ozodbek:

    def __init__(self, name):
        self.talaba = name
        self.yoshi = 15
        self.kurs = "03-25"

    def get_info(self):
        return self.talaba, self.kurs, self.yoshi

obj = Ozodbek("Ozod")
print(f"kitob malumot", obj.get_info() )
