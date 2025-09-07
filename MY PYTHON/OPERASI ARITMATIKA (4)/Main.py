# Operasi Aritmstika

a = 10
b = 3

# Operasi tambah (+)
hasil = a + b
print(a,'+',b,'=', hasil)

# Operasi pengurangan (-)
hasil = a - b
print(a,'-',b,'=', hasil)

# Operasi perkalian (*)
hasil = a * b
print(a,'*',b,'=', hasil)

# Operasi pembagian (/)
hasil = a / b
print(a,'/',b,'=', hasil)

# Operasi eksponen / Pangkat (**)
hasil = a ** b
print(a,'**',b,'=', hasil)

# Operasi Modulus (%)
# adalah sisa dari pembagian
hasil = a % b
print(a,'%',b,'=', hasil)

# Operasi floor division (//) 
# adalah operasi pembagian yang membulatkan ke bawah
hasil = a // b
print(a,'//',b,'=', hasil)

## Prioritas Operasi
'''
1. operasi dalam kurung ()
2. eksponen (**)
3. Perkalian/Pembagian/Modulus/floor (*,/,%,//)
4. penambahan/pengurangan
'''

# Contoh
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x, '=', hasil)

hasil = (x + y) * z
print('(',x,'+',y,')*',z,'=', hasil)