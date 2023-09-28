random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi variabel untuk menyimpan hasil pemisahan
int_dict = {}
float_tuple = ()
string_list = []

# Iterasi melalui daftar acak
for item in random_list:
    if isinstance(item, int):
        # Memisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item % 100) // 10
        ratusan = item // 100
        
        # Menyimpan dalam bentuk dictionary
        int_dict[item] = (ratusan, puluhan, satuan)
    elif isinstance(item, float):
        # Menyimpan dalam bentuk tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Menyimpan dalam bentuk list
        string_list.append(item)

# Cetak hasilnya
print("Data int dalam bentuk dictionary:", int_dict)
print("Data float dalam bentuk tuple:", float_tuple)
print("Data string dalam bentuk list:", string_list)
