## Casting Data
# Merubah satu tipe ke tipe lain

data_int = 9
print("data =", data_int)
print("bertipe =", type(data_int))

#Kita Casting Ke Data integer
print("=====INTEGER=====")
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data =", data_float)
print("bertipe =", type(data_float))
print("data =", data_str)
print("bertipe =", type(data_str))
print("data =", data_bool) #AKAN FALSE JIKA INT NYA 0
print("bertipe =", type(data_bool))

# FLOAT
data_float = 9.0
print("data =", data_float)
print("bertipe =", type(data_float))

print("=====FLOAT=====")
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data =", data_int)
print("bertipe =", type(data_int))
print("data =", data_str)
print("bertipe =", type(data_str))
print("data =", data_bool) 
print("bertipe =", type(data_bool))

# BOOL
data_bool = True
print("data =", data_bool)
print("bertipe =", type(data_bool))

print("=====BOOL=====")
data_int = int(data_bool)
data_float = float(data_bool)
data_str = str(data_bool)
print("data =", data_int)
print("bertipe =", type(data_int))
print("data =", data_float)
print("bertipe =", type(data_float))
print("data =", data_str) 
print("bertipe =", type(data_str))

# STRING
data_str = "10"
print("data =", data_str)
print("bertipe =", type(data_str))

print("=====STRING=====")
data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str)
print("data =", data_int)
print("bertipe =", type(data_int))
print("data =", data_float)
print("bertipe =", type(data_float))
print("data =", data_bool) 
print("bertipe =", type(data_bool))