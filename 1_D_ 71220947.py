print("Halo selamat datang di bioskop!")
print("Dimanakah kamu ingin menonton?")
print("1) XXI Empire")
print("2) XXI Amplaz")
print("3) XXI JCM")

a = int(input("Masukan pilihanmu: "))
if(a>=3):
 print("Pilihan tidak tersedia.")

print("Mau nonton film apa nih? Ada Film:")
print("1. Frozen")
print("2. Keramat")
print("3. KKN di Desa Penari")
b = int(input("Pilih nomor film: "))
if(b>=3):
    print("Pilihan tidak tersedia.")
print("Mau nonton layar bioskop apa:")
print("1. Reguler")
print("2. Dolby almos")
print("3. Premiere")
c = int(input("Pilih nomor tipe layar: "))
if(c>=3):
 print("Pilihan tidak tersedia.")
d = int(input("Berapa banyak tiket? "))
print("Mau nonton jam berapa:")
print("1. 12.35")
print("2. 14.45")
print("3. 16.55")
print("4. 19.05") 

e = int(input("Masukan angka pilihan anda: "))
if(e == "1"):
 print("Oke berhasil!, silahkan dinikmati di jam 12.35")
elif(e== "2"):
 print("Oke berhasil!, silahkan dinikmati di jam 14.45")
elif(e== "3"):
 print("Oke berhasil!, silahkan dinikmati di jam 16.55")
else:
 print("Oke berhasil!, silahkan dinikmati di jam 19.05")

