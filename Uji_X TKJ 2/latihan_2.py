'''buatlah program menghitung luas bangun datar
menggunakan fungsi.
- Segitiga
- Persegi Panjang
'''

a = float(input("masukan panjang alas: "))
t = float(input("masukan tinggi segitiga: "))
luas = 0.5*a*t
print("luas segitiga adalah : "+str(luas))

def luas_s(alas, tinggi):
    luas =1/2 * alas * tinggi
    print("luas segitiga adalah", luas)

luas_s(5, 1)

def luas_pp(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang adalah", luas)

luas_pp(7, 3)