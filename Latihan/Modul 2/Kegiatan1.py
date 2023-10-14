# Inisialisasi 'expenses' dengan data pengeluaran awal
expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

# 1. Fungsi untuk menambahkan pengeluaran baru ke dalam 'expenses' (pure function)


def add_expense(expenses, tanggal, deskripsi, jumlah): return expenses + \
    [{'tanggal': tanggal, 'deskripsi': deskripsi, 'jumlah': jumlah}]

# 2. Fungsi untuk menghitung total pengeluaran harian menggunakan lambda expression


def calculate_total_expenses(date): return sum(
    item['jumlah'] for item in expenses if item['tanggal'] == date)

# 3. Fungsi untuk menyaring pengeluaran berdasarkan tanggal tertentu menggunakan list comprehension


def get_expenses_by_date(date): return [
    item for item in expenses if item['tanggal'] == date]

# 4. Fungsi generator untuk menghasilkan laporan pengeluaran harian dalam bentuk string


def generate_expenses_report(): return ('\n'.join(
    [f"{item['tanggal']} - {item['deskripsi']} - {item['jumlah']}" for item in expenses]))


# Contoh penggunaan:
# Menambahkan pengeluaran baru
expenses = add_expense(expenses, '2023-07-27', 'Makan Malam', 75000)

# Menghitung total pengeluaran harian untuk tanggal tertentu
total_harian = calculate_total_expenses('2023-07-25')
print(f"Total Pengeluaran Harian: {total_harian}")

# Menyaring pengeluaran berdasarkan tanggal tertentu
pengeluaran_tanggal_tertentu = get_expenses_by_date('2023-07-25')

# Menghasilkan laporan pengeluaran harian
laporan = generate_expenses_report()
print(laporan)
