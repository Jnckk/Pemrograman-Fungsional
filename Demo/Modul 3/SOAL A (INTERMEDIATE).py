from functools import reduce
import os  # Import modul os

def main():
    while True:
        # Daftar transaksi pembelian produk
        transactions = [
            {"product": "Buku", "price": 10000, "quantity": 2},
            {"product": "Pensil", "price": 2000, "quantity": 5},
            {"product": "Pensil", "price": 2000, "quantity": 3},
            {"product": "Pulpen", "price": 5000, "quantity": 2},
            {"product": "Buku", "price": 12000, "quantity": 1},
            {"product": "Pulpen", "price": 6000, "quantity": 4}
        ]

        # Fungsi untuk menghitung total harga transaksi menggunakan lambda
        calculate_transaction_total = lambda transaction: transaction["price"] * transaction["quantity"]

        # Fungsi untuk menyaring transaksi hanya untuk produk tertentu dengan Higher Order Function (filter)
        def filter_transactions_by_product(product_name, transactions):
            return list(filter(lambda transaction: transaction["product"] == product_name, transactions))

        # Fungsi untuk menghitung jumlah item yang terjual
        def calculate_total_items_sold(transactions):
            return reduce(lambda x, y: x + y["quantity"], transactions, 0)

        # Membersihkan layar terminal
        os.system('clear' if os.name == 'posix' else 'cls')

        # Input nama produk yang ingin disaring
        product_filter_input = input("Masukkan nama produk yang ingin disaring: ")

        # Menggunakan filter() untuk menyaring transaksi sesuai input produk
        filtered_transactions = filter_transactions_by_product(product_filter_input, transactions)

        # Menampilkan transaksi pembelian produk yang disaring
        print(f"\nTransaksi Pembelian Produk {product_filter_input}:")
        for transaction in filtered_transactions:
            print(transaction)

        # Menggunakan map() untuk menghitung total harga untuk setiap transaksi yang tersaring
        total_prices = list(map(calculate_transaction_total, filtered_transactions))

        # Menampilkan total harga untuk setiap transaksi produk yang tersaring
        print("\nTotal Harga untuk Setiap Transaksi Produk", product_filter_input + ":")
        for price in total_prices:
            print(price)

        # Menggunakan reduce() untuk menghitung total Pendapatan dari semua transaksi yang tersaring
        total_revenue = reduce(lambda x, y: x + y, total_prices, 0)

        # Menampilkan total pendapatan dan total jumlah item terjual
        print("\nTotal Pendapatan dari Transaksi Produk", product_filter_input + ":", total_revenue)
        total_items_sold = calculate_total_items_sold(filtered_transactions)
        print("Total Jumlah Item Terjual dari Produk", product_filter_input + ":", total_items_sold)

        # Pertanyaan untuk mengulang program
        repeat = input("\nApakah Anda ingin mengulang program (Y/N)? ").strip().lower()
        if repeat != 'y':
            break

if __name__ == "__main__":
    main()
