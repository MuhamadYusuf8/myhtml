# PR Latihan logika dan komperasi

# Soal Nomor 1.
# ----- 0 ++++++ 5 ----- 8 ++++++ 11 -------
inputUser = float(input('masukkan angka lebih dari 0\n dan\n kurang dari 5\n atau\n lebih dari 8\n dan\n kurang dari 11\n ='))

#------0++++++
islebihdari0 = inputUser>0
print('lebih dari 0 =', islebihdari0)

#++++++5------
iskurangdari5 = inputUser<5
print('kurang dari 5 =', iskurangdari5)

#------8+++++++
islebihdari = inputUser>8
print('lebih dari 8 =', islebihdari)

#+++++++11-------
iskurangdari = inputUser<11
print('kurang dari 11 =', iskurangdari)

# ----- 0 ++++++ 5 ----- 8 ++++++ 11 -------
iscorrect = islebihdari0 and iskurangdari5 or islebihdari and iskurangdari
print('angka yang anda masukkan =', iscorrect)

print('\n',10*'=','\n')

# Soal Nomor 2.
#  ++++++ 0 ----- 5 ++++++ 8 ----- 11 ++++++
inputUser = float(input('masukkan angka kurang dari 0\n atau\n lebih dari 5\n dan\n kurang dari 8\n atau\n lebih dari 11\n ='))

# ++++++ 0 -----
iskurangdari = inputUser<0
print('kurang dari 0 =', iskurangdari)

# ----- 5 ++++++
islebihdari5 = inputUser>5
print('lebih dari 5 =', islebihdari5)

# ++++++ 8 -----
iskurangdari8 = inputUser<8
print('kurang dari 8 =', iskurangdari8)

# ----- 11 ++++++
islebihdari = inputUser>11
print('lebih dari 11 =', islebihdari)

# ++++++ 0 ----- 5 ++++++ 8 ----- 11 ++++++
iscorrect = iskurangdari or islebihdari5 and iskurangdari8 or islebihdari
print('angka yang anda masukkan =', iscorrect)