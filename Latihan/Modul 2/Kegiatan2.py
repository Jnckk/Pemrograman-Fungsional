# TODO 1: Buatlah Fungsi add_expense disini
def add_expense(expenses, date, description, amount):
    # Fungsi ini digunakan untuk menambahkan pengeluaran ke daftar expenses
    new_expense = {'tanggal': date, 'deskripsi': description, 'jumlah': amount}
    expenses.append(new_expense)
    return expenses

# TODO 2: Buatlah fungsi calculate_total_expenses disini


def calculate_total_expenses(expenses):
    # Fungsi ini menghitung total pengeluaran harian dari daftar expenses
    total = sum(expense['jumlah'] for expense in expenses)
    return total

# TODO 3: Buatlah fungsi get_expenses_by_date disini


def get_expenses_by_date(expenses, date):
    # Fungsi ini mengembalikan daftar pengeluaran berdasarkan tanggal tertentu
    expenses_on_date = [
        expense for expense in expenses if expense['tanggal'] == date]
    return expenses_on_date

# TODO 4: Buatlah fungsi generate_expenses_report disini


def generate_expenses_report(expenses):
    # Fungsi ini menghasilkan laporan pengeluaran harian dalam bentuk string
    report = []
    for expense in expenses:
        report.append(
            f"{expense['tanggal']} - {expense['deskripsi']} - Rp {expense['jumlah']}")
    return report

# TODO 5: Pastikan semua fungsi yang ada sudah berupa pure function
# Semua fungsi yang telah dibuat adalah pure function karena tidak memiliki efek samping.


# TODO 6: Ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command): return int(input(command))


def main():
    expenses = []
    while True:
        print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
        print("1. Tambah Pengeluaran")
        print("2. Total Pengeluaran Harian")
        print("3. Lihat Pengeluaran berdasarkan Tanggal")
        print("4. Lihat Laporan Pengeluaran Harian")
        print("5. Keluar")
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")
        if choice == 1:
            date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD): ")
            description = input("Masukkan deskripsi pengeluaran: ")
            amount = int(input("Masukkan jumlah pengeluaran: "))
            expenses = add_expense(expenses, date, description, amount)
            print("Pengeluaran berhasil ditambahkan.")
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            date = input("Masukkan tanggal (YYYY-MM-DD): ")
            expenses_on_date = get_expenses_by_date(expenses, date)
            print(f"\nPengeluaran pada tanggal {date}:")
            for expense in expenses_on_date:
                print(f"{expense['deskripsi']} - Rp {expense['jumlah']}")
        elif choice == 4:
            print("\nLaporan Pengeluaran Harian:")
            expenses_report = generate_expenses_report(expenses)
            for entry in expenses_report:
                print(entry)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")


if __name__ == "__main__":
    main()
