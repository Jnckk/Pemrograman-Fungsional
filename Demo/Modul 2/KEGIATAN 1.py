import os


class Buku:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        self.dipinjam = False


class AkunAdmin:
    def __init__(self):
        self.buku = {}

    def tambah_buku(self, buku_dict, judul, pengarang): return (
        (buku_dict, f"Buku '{judul}' oleh {pengarang} telah ditambahkan.")
        if judul not in buku_dict
        else (buku_dict, f"Buku '{judul}' sudah ada.")
    )

    def edit_judul_buku(self, buku_dict, judul, judul_baru): return (
        (buku_dict,
         f"Judul buku '{judul}' telah diubah menjadi '{judul_baru}'.")
        if judul in buku_dict
        else (buku_dict, f"Buku '{judul}' tidak ditemukan.")
    )

    def edit_pengarang_buku(self, buku_dict, judul, pengarang_baru): return (
        (buku_dict,
         f"Pengarang buku '{judul}' telah diubah menjadi '{pengarang_baru}'.")
        if judul in buku_dict
        else (buku_dict, f"Buku '{judul}' tidak ditemukan.")
    )


class AkunUser:
    def __init__(self):
        self.peminjaman = []

    def pinjam_buku(self, buku_dict, buku): return (
        (self.peminjaman, f"Anda telah meminjam buku '{buku}'.")
        if buku in buku_dict and not buku_dict[buku].dipinjam
        else (self.peminjaman, f"Buku '{buku}' sudah dipinjam oleh pengguna lain.")
    )

    def kembalikan_buku(self, buku_dict, buku): return (
        (self.peminjaman, f"Anda telah mengembalikan buku '{buku}'.")
        if buku in self.peminjaman
        else (self.peminjaman, f"Anda tidak meminjam buku '{buku}'.")
    )

    def tampilkan_buku_tersedia(self, buku_dict): return [
        (judul, buku_dict[judul].pengarang)
        for judul in buku_dict if not buku_dict[judul].dipinjam
    ]

    def cari_buku(self, buku_dict, keyword): return [
        judul for judul in buku_dict if keyword.lower() in judul.lower()
    ]


def clear_screen(): return os.system('cls' if os.name == 'nt' else 'clear')


admin = AkunAdmin()
user = AkunUser()

user_credentials = {
    "admin": "admin123",
    "user": "user123"
}

while True:
    clear_screen()
    print("\nMenu:")
    print("1. Login Admin")
    print("2. Login User")
    print("3. Keluar")

    login_choice = input("Pilih jenis login: ")

    if login_choice == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in user_credentials and user_credentials[username] == password:
            while True:
                clear_screen()
                print("\nMenu Admin:")
                print("1. Tambah Buku")
                print("2. Edit Judul Buku")
                print("3. Edit Pengarang Buku")
                print("4. Kembali ke Menu Utama")

                admin_choice = input("Pilih menu admin: ")

                if admin_choice == "1":
                    judul = input("Masukkan judul buku: ")
                    pengarang = input("Masukkan nama pengarang: ")
                    admin.buku, pesan = admin.tambah_buku(
                        admin.buku, judul, pengarang)
                    print(pesan)
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif admin_choice == "2":
                    judul = input("Masukkan judul buku yang ingin diedit: ")
                    judul_baru = input("Masukkan judul baru: ")
                    admin.buku, pesan = admin.edit_judul_buku(
                        admin.buku, judul, judul_baru)
                    print(pesan)
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif admin_choice == "3":
                    judul = input("Masukkan judul buku yang ingin diedit: ")
                    pengarang_baru = input("Masukkan nama pengarang baru: ")
                    admin.buku, pesan = admin.edit_pengarang_buku(
                        admin.buku, judul, pengarang_baru)
                    print(pesan)
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif admin_choice == "4":
                    break

                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
                    input("Tekan Enter untuk kembali ke Menu User...")
        else:
            print("Username atau password salah. Silakan coba lagi.")
            input("Tekan Enter untuk kembali ke Menu User...")

    elif login_choice == "2":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in user_credentials and user_credentials[username] == password:
            while True:
                clear_screen()
                print("\nMenu User:")
                print("1. Pinjam Buku")
                print("2. Kembalikan Buku")
                print("3. Tampilkan Buku Tersedia")
                print("4. Cari Buku")
                print("5. Kembali ke Menu Utama")

                user_choice = input("Pilih menu user: ")

                if user_choice == "1":
                    buku = input("Masukkan judul buku yang ingin dipinjam: ")
                    user.peminjaman, pesan = user.pinjam_buku(admin.buku, buku)
                    print(pesan)
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif user_choice == "2":
                    buku = input(
                        "Masukkan judul buku yang ingin dikembalikan: ")
                    user.peminjaman, pesan = user.kembalikan_buku(
                        admin.buku, buku)
                    print(pesan)
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif user_choice == "3":
                    buku_tersedia = user.tampilkan_buku_tersedia(admin.buku)
                    if buku_tersedia:
                        print("\nBuku Tersedia:")
                        print("{:<5} {:<30} {:<30}".format(
                            "No.", "Judul Buku", "Pengarang"))
                        for idx, (judul, pengarang) in enumerate(buku_tersedia, start=1):
                            print("{:<5} {:<30} {:<30}".format(
                                idx, judul, pengarang))
                    else:
                        print("Tidak ada buku yang tersedia.")
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif user_choice == "4":
                    keyword = input("Masukkan kata kunci untuk mencari buku: ")
                    hasil_pencarian = user.cari_buku(admin.buku, keyword)
                    if hasil_pencarian:
                        print("\nHasil Pencarian:")
                        for idx, judul in enumerate(hasil_pencarian, start=1):
                            print(f"{idx}. {judul}")
                    else:
                        print(
                            f"Tidak ditemukan buku dengan kata kunci '{keyword}'.")
                    input("Tekan Enter untuk kembali ke Menu User...")

                elif user_choice == "5":
                    break

                else:
                    print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
                    input("Tekan Enter untuk kembali ke Menu User...")
        else:
            print("Username atau password salah. Silakan coba lagi.")
            input("Tekan Enter untuk kembali ke Menu User...")

    elif login_choice == "3":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih jenis login yang sesuai.")
        input("Tekan Enter untuk kembali ke Menu User...")
