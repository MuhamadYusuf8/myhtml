# OPERATOR BITWES

# BITWES DALAM BAHASA INDONESIA ADALAH MASING MASING BITE

a = 9
b = 5

# BITWES OR (|)
c = a | b
print('=======OR========')
print('nilai :',a,',  binary :', format(a,'08b'))
print('nilai :',b,',  binary :', format(b,'08b'))
print('-------------------------------(|)')
print('nilai :',c,',  binary :', format(c,'08b'))

# BITWES AND (&)
c = a & b
print('=======AND========')
print('nilai :',a,',  binary :', format(a,'08b'))
print('nilai :',b,',  binary :', format(b,'08b'))
print('-------------------------------(&)')
print('nilai :',c,',  binary :', format(c,'08b'))

# BITWES XOR (^)
c = a ^ b
print('=======XOR========')
print('nilai :',a,',  binary :', format(a,'08b'))
print('nilai :',b,',  binary :', format(b,'08b'))
print('-------------------------------(^)')
print('nilai :',c,',  binary :', format(c,'08b'))

# BITWES NOT (^)
c = ~a
print('=======NOT========')
print('nilai :',a,',  binary :', format(a,'08b'))
print('-------------------------------(~)')
print('nilai :',c,',  binary :', format(c,'08b'))
d = 0b0000001001
e = 0b1111111111
print('-------------------------------(^)')
print('nilai :',e^d,',  binary :', format(e^d,'08b'))