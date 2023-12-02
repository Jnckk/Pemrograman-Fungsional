import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# Data tinggi badan individu dalam sentimeter
tinggi_badan = [165, 170, 155, 172, 180, 160, 175, 165, 185, 175, 170, 160]
interval_size = 10  # Misalnya interval ukuran per 10 sentimeter

# Fungsi untuk mengelompokkan tinggi badan ke dalam interval tertentu
def kelompokkan_ke_interval(data, interval_size):
    interval_counts = {}
    for tinggi in data:
        interval_bawah = (tinggi // interval_size) * interval_size
        interval_atas = interval_bawah + interval_size
        interval = (interval_bawah, interval_atas)

        if interval in interval_counts:
            interval_counts[interval] += 1
        else:
            interval_counts[interval] = 1

    return interval_counts

# Menghitung frekuensi tinggi badan dalam interval
frekuensi_interval = kelompokkan_ke_interval(tinggi_badan, interval_size)

# Visualisasi data dalam bentuk histogram dan Menambahkan kurva pdf
# dari distribusi normal pada hasil visualisasi data

# Visualisasi Histogram
bins = [i[0] for i in frekuensi_interval.keys()]
counts = frekuensi_interval.values()

plt.bar(bins, counts, width=interval_size, edgecolor='black', align='edge', label='Data')
plt.xlabel('Interval Tinggi Badan (cm)')
plt.ylabel('Frekuensi')
plt.title('Histogram Frekuensi Tinggi Badan')

# Menambahkan kurva PDF dari distribusi normal (dengan warna merah)
mu, std = np.mean(tinggi_badan), np.std(tinggi_badan)
xmin, xmax = min(tinggi_badan), max(tinggi_badan)
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
plt.plot(x, p * len(tinggi_badan) * interval_size, 'r', linewidth=2, label='PDF (Normal Distribution)')

# Menambahkan legenda
plt.legend()

plt.show()
