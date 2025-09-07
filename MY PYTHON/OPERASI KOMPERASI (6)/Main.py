# operasi komperasi

a = 4
b = 2

# lebih besar dari (>)
print("===== Lebih besar dari (>)\n")
hasil = a > 3
print( a,'>',3,'=', hasil)
hasil = b > 3
print( a,'>',3,'=', hasil)
hasil = b > 2
print( b,'>',2,'=', hasil,'\n')

# kurang dari (>)
print("===== Kurang dari (<)\n")
hasil = a < 3
print( a,'<',3,'=', hasil)
hasil = b < 3
print( a,'<',3,'=', hasil)
hasil = b < 2
print( b,'<',2,'=', hasil,'\n')

# lebih dari sama dengan (>=)
print("===== Lebih dari sama dengan (>=)\n")
hasil = a >= 3
print( a,'>=',3,'=', hasil)
hasil = b >= 3
print( a,'>=',3,'=', hasil)
hasil = b >= 2
print( b,'>=',2,'=', hasil,'\n')

# kurang dari sama dengan (<=)
print("===== kurang dari sama dengan (<=)\n")
hasil = a <= 3
print( a, '<=',3,'=', hasil)
hasil = b <= 3
print( a, '<=',3,'=', hasil)
hasil = b <= 2
print( b,'<=',2,'=', hasil,'\n')

# Sama dengan (==)
print("===== sama dengan (==)\n")
hasil = a == 4
print( a,'==',4,'=', hasil)
hasil = b == 4
print( a,'==',4,'=', hasil,'\n')

# Tidak sama dengan (!=)
print("===== Tidak sama dengan (!=)\n")
hasil = a != 4
print( a,'!=',4,'=', hasil)
hasil = b != 4
print( a,'!=',4,'=', hasil,'\n')

# Komperasi
# >,<,>=,<=,==,!= ini dapat bekerja pada syntax literal

# Literal adalah angka yang tidak memakan memori

# IS 
print("===== IS\n")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,', id =', hex(id(x)))
print('nilai y =',y,', id =', hex(id(y)))
hasil = x is y
print('x is y =', hasil,'\n')

# IS NOT
print("===== IS NOT\n")
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,', id =', hex(id(x)))
print('nilai y =',y,', id =', hex(id(y)))
hasil = x is not y
print('x is not y =', hasil,'\n')