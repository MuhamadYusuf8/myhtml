# cara membuat string

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

#. 1} dengan menggunakan single quote '...'
contoh = 'ini adalah contoh single quote'
print(contoh)

#. 2} dengan menggunakan double quote "..."
contoh = "ini adalah contoh double quote"
print(contoh)

print('"hallo, apa kabar?"')
print("'hallo, apa kabar?'")

# 2. Menggunakan tanda \ menjadi string
#contoh : \
print('mari shalat jum\'at')

#contoh : Backslash \\
print('C:\\Users\\user\\Document')

#contoh : TAB (\t)
print('ucup\t ganteng')

#contoh : backspace (\b)
print('ucup\b ganteng')

# NEWLINE (\n)
print('baris pertama\n baris kedua') # LF
print('baris pertama\r baris kedua') # CR

# STRING LITERAL / RAW (r)
print(r'c:\new\folder')

# Multilane literal string (""")
print("""
      nama : muhamad yusuf
      kelas : 3 sma
      """)

# multiline literal dan raw
print(r"""
      nama : ucup
      kelas : 3 sma
      web : www.ucup.com\newID
      """)
