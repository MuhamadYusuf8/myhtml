# input data dari user
# Contoh :
data = input("masukan data = ")

print("data =", data,"type =", type(data))
# Untuk typenya pasti string(str)

# jika ingin typenya jadi integer(int) atau float(float)
#  Kita harus casting jadi type yang kita inginkan

# contoh integer(int)
data_int = int(input("masukan angka ="))

print("data =", data_int,"type =", type(data_int))

# contoh float
data_float = float(input("masukan koma ="))

print("data =", data_float,"type =", type(data_float))

# Contoh Boolean 
data_bool = bool(int(input("masukan biner =")))

print("data =", data_bool,"type =", type(data_bool))
