''' fungsi pada python di definisikan dengan def '''

''' def nama_fungsi(): '''

def salam():
    print("asalammualaikum !! akhi ukhty")

salam()
salam()
salam()

''' buatlah sebuah fungsi veri kalian '''

def hallo():
    print("hallo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! ")

hallo()
hallo()
hallo()

'''FUNGSI DENGAN PARAMETER'''
'''def nama_fungsi(p1, p2)'''

def say_hi(nama):
    print("hallo perkenalkan nama saya", nama)

say_hi("agoy")
say_hi("pihh")

'''buatlah fungsi dengan 3 parameter'''

def nama_fungsi(p1, p2, p3):
    print("orang paling tolol adalah" + " " + p1,p2,p3)

nama_fungsi(p1 = "ryan!! ", p2 = "alul!!", p3 = "kebot!!")

def perkenalan(nama, alamat, umur):
    print("nama saya:", nama)
    print("alamat saya:", alamat)
    print("umur saya:", umur)
perkenalan("oji", "depok", "16")
print("\n\n========== BATAS ==========\n\n")
perkenalan("bila", "depok", "15")