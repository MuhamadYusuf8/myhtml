# OPERATOR ASSIGMENT

# OPERASI KABATAKU DENGAN ASSIGNMENT 
a = 5
print('nilai a =', a)
a += 1
print('nilai a += 1',',nilai a menjadi', a)
a -= 2
print('nilai a -= 2',',nilai a menjadi', a)
a *= 5
print('nilai a *= 5',',nilai a menjadi', a)
a /= 2
print('nilai a /= 2',',nilai a menjadi', a)

# OPERASI MODULUS DAN FLOOR DIVISION
b = 10
print('\nnilai b =', b)
b %= 3
print('nilai b %= 3',',nilai b menjadi', b)
b = 10
print('\nnilai b =', b)
b //= 3
print('nilai b //= 3',',nilai b menjadi', b)
b = 5
print('\nnilai b =', b)
b **= 3
print('nilai b **= 3',',nilai b menjadi', b)

# OPERASI BITWISE

# OR
c = True
print('\nnilai C =', c)
c |= False
print('nilai c |= false',',nilai c menjadi', c)
c = False
print('nilai C =', c)
c |= False
print('nilai c |= false',',nilai c menjadi', c)

# AND
c = True
print('\nnilai C =', c)
c &= False
print('nilai c &= false',',nilai c menjadi', c)
c = True
print('nilai C =', c)
c &= True
print('nilai c &= True',',nilai c menjadi', c)

# XOR
c = True
print('\nnilai C =', c)
c ^= False
print('nilai c ^= false',',nilai c menjadi', c)
c = True
print('nilai C =', c)
c ^= True
print('nilai c ^= True',',nilai c menjadi', c)

# GESER GESER
d = 0b0100
print('\nnilai d =', format(d,'04b'))
d >>= 2
print('nilai d >>= 2',',nilai d menjadi', format(d,'04b'))
d <<= 1 
print('nilai d <<= 1',',nilai d menjadi', format(d,'04b'))