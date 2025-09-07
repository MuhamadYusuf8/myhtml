# Latihan Konversi Satuan temperatur

# Program Konversi celsius ke satuan lain

print("\nPROGRAM KONVERSI SATUAN\n")

# RUMUS UNTUK CELCIUS

celcius = float(input('Masukan suhu dalam celcius :'))
print("suhu adalah :", celcius, "celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah :", reamur, "reamur")

# fahrenheit
fahrenheit = (9/5) * celcius + 32
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

# kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# RUMUS UNTUK REAMUR

reamur = float(input('\nMasukan suhu dalam reamur :'))
print("suhu adalah :", reamur, "reamur")

# celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah :", celcius, "celcius")

# fahrenheit
fahrenheit = (9/4) * reamur + 32
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

# kelvin
kelvin = (5/4) * reamur + 273
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# RUMUS UNTUK FAHRENHEIT

fahrenheit = float(input('\nMasukan suhu dalam fahrenheit :'))
print("suhu adalah :", fahrenheit, "fahrenheit")

# celcius
celcius = (5/9) * fahrenheit -  32
print("suhu dalam celcius adalah :", celcius, "celcius")

# reamur
reamur = (4/9) * fahrenheit - 32
print("suhu dalam reamur adalah :", reamur, "reamur")

# kelvin
kelvin = ((5/9) * fahrenheit - 32)+ 273
print("suhu dalam kelvin adalah :", kelvin, "kelvin")

# RUMUS UNTUK KELVIN

kelvin = float(input('\nMasukan suhu dalam kelvin :'))
print("suhu adalah :", kelvin, "kelvin")

# celcius
celcius = kelvin-273
print("suhu dalam celcius adalah :", celcius, "celcius")

# reamur
reamur = (4/5) * kelvin - 273
print("suhu dalam reamur adalah :", reamur, "reamur")

# fahrenheit
fahrenheit = (9/5 *(kelvin-273)) + 32
print("suhu dalam fahrenheit adalah :", fahrenheit, "fahrenheit")

