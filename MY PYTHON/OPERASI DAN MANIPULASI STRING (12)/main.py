# OPERASI DAN MANIPULASI STRING

# 1. Menyambung sring (concatenate)
nama_depan = "Muhamad"
nama_tengah = "D"
nama_belakang = "Yusuf"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

# 2. Menghitung panjang string () 
panjang = len(nama_lengkap) 
print("panjang dari", nama_lengkap + ' ', '=', str(panjang)) # Spasi DIhitung juga

# 3. Operatpr untuk string

# Mengecek apakah ada komponen char atau string di string
D = "D"
status = D in nama_lengkap
print(D + " ada di " + nama_lengkap + " = " + str(status))

c = "c"
status = c in nama_lengkap
print(c + " ada di " + nama_lengkap + " = " + str(status))

s = "s"
status = s not in nama_lengkap
print(s + " tidak ada di " + nama_lengkap + " = " + str(status))

z = "z"
status = z not in nama_lengkap
print(z + " tidak ada di " + nama_lengkap + " = " + str(status))

# Mengulang string
print(10*"wk")
print("wk"*5)

# Indexing 
print("index ke-0 :", nama_lengkap[0])
print("index ke-2 :", nama_lengkap[2])
print("index ke-7 :", nama_lengkap[7])
print("index ke-(-1) :", nama_lengkap[-1])
print("index ke-(0:5) :", nama_lengkap[0:5])
print("index ke-(0,2,4,6,8,10) :", nama_lengkap[0:10:2])

# Item paling kecil
print("paling kecil =",min(nama_lengkap))
# Item paling besar
print("paling besar =",max(nama_lengkap))

asci_code = ord("u")
print("ASCI code untuk u adalah", str(asci_code))
data = 110
print("char nya ASCI code 32 adalah", chr(data))

# Operator dalam bentuk menthod

data = "muhamad yusuf"
jumlah = data.count("u")
print("jumlah u pada", data, "=", str(jumlah))