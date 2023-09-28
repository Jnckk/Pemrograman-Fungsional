import os

# Inisialisasi data peserta
data_peserta = []

# Fungsi untuk menambah data peserta oleh admin
def tambah_peserta():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    id_peserta = len(data_peserta)
    print("\nID Peserta baru:", id_peserta)  # Menampilkan ID peserta yang baru ditambahkan
    nama = input("Masukkan nama peserta: ")
    nilai_matematika = int(input("Masukkan nilai Matematika peserta: "))
    nilai_bahasa_indonesia = int(input("Masukkan nilai Bahasa Indonesia peserta: "))
    nilai_ipa = int(input("Masukkan nilai IPA peserta: "))
    nilai_ips = int(input("Masukkan nilai IPS peserta: "))
    
    rata_rata_nilai = (nilai_matematika + nilai_bahasa_indonesia + nilai_ipa + nilai_ips) / 4
    hasil_akhir = "Lolos" if rata_rata_nilai >= 75 else "Tidak Lolos"
    
    data_peserta.append([id_peserta, nama, nilai_matematika, nilai_bahasa_indonesia, nilai_ipa, nilai_ips, rata_rata_nilai, hasil_akhir])
    
    print("\nData peserta berhasil ditambahkan.")
    input("\nTekan Enter untuk kembali ke menu...")

# Fungsi untuk mengedit nilai peserta oleh admin
def edit_nilai():
    id_peserta = int(input("Masukkan ID peserta yang akan diedit: "))
    if id_peserta < len(data_peserta):
        nilai_matematika = int(input("Masukkan nilai Matematika baru untuk peserta {}: ".format(id_peserta)))
        nilai_bahasa_indonesia = int(input("Masukkan nilai Bahasa Indonesia baru untuk peserta {}: ".format(id_peserta)))
        nilai_ipa = int(input("Masukkan nilai IPA baru untuk peserta {}: ".format(id_peserta)))
        nilai_ips = int(input("Masukkan nilai IPS baru untuk peserta {}: ".format(id_peserta)))
        
        rata_rata_nilai = (nilai_matematika + nilai_bahasa_indonesia + nilai_ipa + nilai_ips) / 4
        
        data_peserta[id_peserta][2] = nilai_matematika
        data_peserta[id_peserta][3] = nilai_bahasa_indonesia
        data_peserta[id_peserta][4] = nilai_ipa
        data_peserta[id_peserta][5] = nilai_ips
        data_peserta[id_peserta][6] = rata_rata_nilai
        data_peserta[id_peserta][7] = "Lolos" if rata_rata_nilai >= 75 else "Tidak Lolos"
        
        print("\nNilai peserta berhasil diubah.")
    else:
        print("\nID peserta tidak valid.")
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menampilkan nilai dan hasil akhir peserta dalam bentuk tabel
def tampilkan_hasil_peserta(id_peserta):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    if id_peserta < len(data_peserta):
        print("\nHasil Peserta:")
        print("{:<12} {:<15} {:<10} {:<20} {:<10} {:<10}".format("ID", "Nama", "Matematika", "Bahasa Indonesia", "IPA", "IPS"))
        peserta = data_peserta[id_peserta]
        print("{:<12} {:<15} {:<10} {:<20} {:<10} {:<10}".format(peserta[0], peserta[1], peserta[2], peserta[3], peserta[4], peserta[5]))
        print("\nRata-rata Nilai: {:.2f}".format(peserta[6]))
        print("Hasil Akhir: {}".format(peserta[7]))
    else:
        print("ID peserta tidak valid.")
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menampilkan data peserta dalam bentuk tabel
def tampilkan_data_peserta_tabel():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    print("\nData Peserta:")
    print("{:<5} {:<15}".format("ID", "Nama"))
    for peserta in data_peserta:
        print("{:<5} {:<15}".format(peserta[0], peserta[1]))

# Main program
while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
    print("\nMenu:")
    print("1. Admin")
    print("2. Peserta")
    print("3. Keluar")
    
    peran = input("Pilih peran Anda (1/2/3): ")
    
    if peran == "1":  # Menu Admin
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        print("\nMenu Admin:")
        print("1. Tambah Peserta")
        print("2. Edit Nilai")
        print("3. Kembali ke Menu Utama")
        
        pilihan_admin = input("Pilih menu Admin (1/2/3): ")
        
        if pilihan_admin == "1":
            tambah_peserta()
        elif pilihan_admin == "2":
            tampilkan_data_peserta_tabel()
            edit_nilai()
        elif pilihan_admin == "3":
            continue
        else:
            print("Pilihan Admin tidak valid.")
    
    elif peran == "2":  # Menu Peserta
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear terminal
        tampilkan_data_peserta_tabel()
        id_peserta = int(input("Masukkan ID peserta Anda: "))
        tampilkan_hasil_peserta(id_peserta)
    
    elif peran == "3":  # Keluar
        break
    
    else:
        print("Pilihan tidak valid. Silakan pilih peran yang benar.")
