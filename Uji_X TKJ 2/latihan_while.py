i = 0

while i < 5:
    print(i)
    i += 1


var_list = ["joko", "anwar", "suprapto", "andhika"]
x = 0
y = len(var_list)

print("========== while Extract Data ==========")
while x < y:
    print(var_list[x])
    x += 1

# buatlah program yang hanya menampilkan bilangan ganjil yang tidak lebih dari 50 

i = 1

while i <= 5:

    print("*"*i)
    i+=1

i = 4

while i >= 1:

    print("*"*i)
    i-=1

#latihan while : ncontinue, pass, break

number = 0 
while True:
    number += 1
    print("kuda terbang %i" %number)
    if number >= 5:
        break

nilai = int(input("masukan nilai genap: "))

while nilai % 2 !=0:
    nilai = int(input("salah dong masa begitu!!, masukan nilai genap: "))

print("nah yang ini baru benar!! nilai = %i" %nilai)

# buatlah sebuah program yang dimana merubah nilai ganjil menjadi genap, yang tidak jauh 3 nilai dari nilai asli

while True:
    gjl = int(input("masukan nilai ganjil: "))
    if gjl % 2 == 0:
        print("salah, nilai bukan ganjil")
    else:
        gnp = gjl + 3
        print("nilai %i = %i" %(gjl, gnp))
        break 

# buatlah sebuah konsep program while versi kalian !! 
# jelaskan