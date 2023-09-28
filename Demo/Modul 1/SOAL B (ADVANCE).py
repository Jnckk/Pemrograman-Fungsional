import os

class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.dipinjam = False

class AkunAdmin:
    def __init__(self):
        self.buku = {}

    def tambah_buku(self, judul, pengarang):
        if judul not in self.buku:
            self.buku[judul] = Buku(judul, pengarang)
            print(f"Buku '{judul}' oleh {pengarang} telah ditambahkan.")

class AkunUser:
    def __init__(self):
        self.peminjaman = []

    def pinjam_buku(self, buku, buku_dict):
        if buku in buku_dict:
            if not buku_dict[buku].dipinjam:
                buku_dict[buku].dipinjam = True
                self.peminjaman.append(buku)
                print(f"Anda telah meminjam buku '{buku}'.")
            else:
                print(f"Buku '{buku}' sudah dipinjam oleh pengguna lain.")
        else:
            print(f"Buku '{buku}' tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, buku, buku_dict):
        if buku in self.peminjaman:
            buku_dict[buku].dipinjam = False
            self.peminjaman.remove(buku)
            print(f"Anda telah mengembalikan buku '{buku}'.")
        else:
            print(f"Anda tidak meminjam buku '{buku}'.")

    def tampilkan_buku_tersedia(self, buku_dict):
        print("\nBuku Tersedia:")
        print("{:<5} {:<30} {:<30}".format("No.", "Judul Buku", "Pengarang"))
        for idx, buku in enumerate(buku_dict, start=1):
            if not buku_dict[buku].dipinjam:
                print("{:<5} {:<30} {:<30}".format(idx, buku, buku_dict[buku].pengarang))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inisialisasi akun admin dan akun user
admin = AkunAdmin()
user = AkunUser()

while True:
    clear_screen()  # Membersihkan terminal sebelum menampilkan menu
    print("PERPUSTAKAAN NEWBIE")
    print("Menu:")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Keluar")
    
    login_choice = input("Pilih jenis login: ")

    if login_choice == "1":
        while True:
            clear_screen()  # Membersihkan terminal sebelum menampilkan menu admin
            print("Menu Admin:")
            print("1. Tambah Buku")
            print("2. Kembali ke Menu Utama")
            
            admin_choice = input("Pilih menu admin: ")

            if admin_choice == "1":
                judul = input("Masukkan judul buku: ")
                pengarang = input("Masukkan nama pengarang: ")
                admin.tambah_buku(judul, pengarang)
                input()
            
            elif admin_choice == "2":
                break
            
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
                input()
    
    elif login_choice == "2":
        while True:
            clear_screen()  # Membersihkan terminal sebelum menampilkan menu user
            print("Menu User:")
            print("1. Tampilkan Buku Tersedia")
            print("2. Pinjam Buku")
            print("3. Kembalikan Buku")
            print("4. Kembali ke Menu Utama")
            
            user_choice = input("Pilih menu user: ")

            if user_choice == "1":
                user.tampilkan_buku_tersedia(admin.buku)
                input()
            
            elif user_choice == "2":
                buku = input("Masukkan judul buku yang ingin dipinjam: ")
                user.pinjam_buku(buku, admin.buku)
                input()
            
            elif user_choice == "3":
                buku = input("Masukkan judul buku yang ingin dikembalikan: ")
                user.kembalikan_buku(buku, admin.buku)
                input()
                
            
            elif user_choice == "4":
                break
            
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
                input()
    
    elif login_choice == "3":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih jenis login yang sesuai.")
        input()
