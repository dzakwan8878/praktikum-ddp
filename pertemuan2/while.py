# angka = 1

# while angka > 0 and angka < 11:
#     angka = int(input("Masukkan Bilangan Bulat: "))

#     if angka >=1:
#         print("Bilangna Positif")
#     elif angka < 0:
#         print("Bilangan Negatif")
#     else:
#         print("Bilangan Nol")

while True:
    nama = input("Masukkan Nama Anda:   ")
    if nama == "x":
        break
    elif nama == "Daus":
        continue
    
    print("Selamat Datang", nama)