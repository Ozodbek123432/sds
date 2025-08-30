#funkslaylar 2 turga bolinadi
#key - orqali yaratiladigan funksyalar
#nomsiz -funksayalar: lamta
# kvadrat = lambda a : a * a
# print(kvadrat(5))
# keyboard = lambda a ,b: a * a
# print(keyboard(5,4))
# --- Oddiy (def) funksiyalar ---

# 1. Sonning kvadratini hisoblash
def kvadratini_hisobla(son):
    """Berilgan sonning kvadratini hisoblab qaytaradi."""
    return son ** 2

# 2. Uchta sonning eng kattasini topish
def eng_kattasini_top(son1, son2, son3):
    """Uchta son ichidan eng kattasini qaytaradi."""
    return max(son1, son2, son3)

# 3. Ism va yoshga asoslangan salomlashish
def salomlash(ism, yosh):
    """Ism va yoshni olib, salomlashish matnini qaytaradi."""
    return f"Salom {ism}, siz {yosh} yoshdasiz"

# 4. Ro'yxatdagi barcha sonlar yig'indisini hisoblash
def royxat_yigindisi(raqamlar_royxati):
    """Ro'yxatdagi barcha sonlarning yig'indisini hisoblab qaytaradi."""
    return sum(raqamlar_royxati)

# 5. Sonning juft yoki toq ekanligini aniqlash
def juft_yoki_toq(son):
    """Sonning juft yoki toq ekanligini aniqlab qaytaradi."""
    if son % 2 == 0:
        return "Juft"
    else:
        return "Toq"

# --- Lambda funksiyalar ---

# 1. Berilgan sonning kvadratini hisoblaydigan lambda funksiya
kvadrat_lambda = lambda son: son ** 2

# 2. Ikki sonni qo'shib natijani qaytaradigan lambda funksiya
qoshish_lambda = lambda son1, son2: son1 + son2

# 3. Ismni qabul qilib, uni katta harflarda qaytaradigan lambda funksiya
katta_harf_lambda = lambda ism: ism.upper()

# 4. Ro'yxatdagi sonlarni ikki barobar oshiradigan lambda funksiya (map bilan)
# Misol ro'yxat: [1, 2, 3, 4, 5]
# Natija: [2, 4, 6, 8, 10]
ikki_barobar_oshir_lambda = lambda royxat: list(map(lambda x: x * 2, royxat))

# 5. Ro'yxatdan faqat juft sonlarni ajratib beradigan lambda funksiya (filter bilan)
# Misol ro'yxat: [1, 2, 3, 4, 5, 6]
# Natija: [2, 4, 6]
juft_sonlarni_filter_lambda = lambda royxat: list(filter(lambda x: x % 2 == 0, royxat))


# --- Funksiyalarni sinab ko'rish ---

print("--- Oddiy Funksiyalar Natijalari ---")
print(f"Kvadrat: {kvadratini_hisobla(7)}") # Natija: 49
print(f"Eng katta son: {eng_kattasini_top(10, 25, 15)}") # Natija: 25
print(f"Salomlashuv: {salomlash('Ali', 30)}") # Natija: Salom Ali, siz 30 yoshdasiz
print(f"Ro'yxat yig'indisi: {royxat_yigindisi([1, 2, 3, 4, 5])}") # Natija: 15
print(f"Juft yoki toq: {juft_yoki_toq(4)}") # Natija: Juft
print(f"Juft yoki toq: {juft_yoki_toq(7)}") # Natija: Toq

print("\n--- Lambda Funksiyalar Natijalari ---")
print(f"Lambda kvadrat: {kvadrat_lambda(6)}") # Natija: 36
print(f"Lambda qo'shish: {qoshish_lambda(8, 12)}") # Natija: 20
print(f"Lambda katta harf: {katta_harf_lambda('python')}") # Natija: PYTHON
print(f"Lambda ikki barobar: {ikki_barobar_oshir_lambda([1, 2, 3])}") # Natija: [2, 4, 6]
print(f"Lambda juft sonlar: {juft_sonlarni_filter_lambda([1, 2, 3, 4, 5, 6])}") # Natija: [2, 4, 6]
