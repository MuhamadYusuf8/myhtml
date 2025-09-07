# Episode latihan logika dan koperasi

# Membuat gabungan area rentang dari angka


# +++++++3------10+++++++
inputUser = float(input("Masukkan angka yang kurang dari 3\n atau\n lebih dari 10\n ="))

# -------3++++++
isKurangDari = (inputUser<3)
print('kurang dari 3 =',isKurangDari)

# +++++++10------
isLebihDari = inputUser>10
print('lebih besar dari 10 =',isLebihDari)

isCorrect = (isKurangDari or isLebihDari)
print ('angka yang anda masukan =',isCorrect,'\n')

print(10*'=','\n')

# --------3+++++++10-------
# Kasus arisam
inputUser = float(input("Masukkan angka yang lebih dari 3\n  dan\n kurang dari 10\n ="))

# --------3
isLebihDari = (inputUser>3)
print('lebih dari 3 =',isLebihDari)

# +++++++10-------
isKurangDari = inputUser<10
print('kurang dari 10 =',isKurangDari)

# --------3+++++++10-------
isCorrect = (isLebihDari and isKurangDari)
print ('angka yang anda masukan =',isCorrect)

