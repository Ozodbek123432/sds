dicta = {
         "a": 1,
         "b": 2,
         "c": 3
}
#malumot qoshadi
s = dicta.update({"d": 4})
print(s)
#baarchasini olibb keladi
v = dicta.items()
print(v)
#farat velo ni olib keladi
e=dicta.get("a")
print(e)
#kesib oladi
r = dicta.pop("b")
print(r)

f = dicta.popitem()
print(f)
y = dicta.setdefault("t", "salom")
print(dicta)
print(y)