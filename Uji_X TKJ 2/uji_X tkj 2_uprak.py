# buatlah pemrograman while untuk mencetak setiap huruf yang di masukan


mystr = input("masukan nama: ")
for x in mystr:
    print(x)


#buatlah sebuah program untuk menampilkan bilangan genap diatas angka 65

while True:
    genap = int(input("masukan nilai genap: "))
    if genap % 66:
        print("salah, masukan nilai genap")
    else:
        ganjil = genap 
        print("benar, nilai %i = %i" %(genap, ganjil))
        genap 
        break 
    continue
