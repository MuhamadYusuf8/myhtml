# operasi algoritma atau boolean

# not, or, and, xor

# NOT ( kebalikan dari angka awal)
a = True
b = False
c = not a
print ( 'data a =', c)
print ('====== NOT')
print ('data c =', c,'\n')

# OR ( JIKA SALAH SATU TRUE MAKA HASILNYA TRUE)
print ('====== OR')
a = False
b = False
c = a or b
print (a,'or',b,' =',c)
a = False
b = True
c = a or b
print (a,'or',b,'  =',c)
a = True
b = False
c = a or b
print (a,'or',b,'  =',c)
a = True
b = True
c = a or b
print (a,'or',b,'   =',c,'\n')

# AND ( JIKA SALAH SATU FALSE MAKA HASILNYA FALSE)
print ('====== AND')
a = False
b = False
c = a and b
print (a,'AND',b,'=',c)
a = False
b = True
c = a and b
print (a,'AND',b,' =',c)
a = True
b = False
c = a and b
print (a,'AND',b,' =',c)
a = True
b = True
c = a and b
print (a,'AND',b,'  =',c,'\n')

# XOR ( JIKA BERBEDA MAKA HASILNYA TRUE)
print ('====== XOR')
a = False
b = False
c = a ^ b
print (a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print (a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print (a,'XOR',b,' =',c)
a = True
b = True
c = a ^ b
print (a,'XOR',b,'  =',c,'\n')