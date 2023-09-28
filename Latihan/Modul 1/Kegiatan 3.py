# Sistem penilaian mahasiswa

# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(uts, uas):
    return (uts + uas) / 2

# Fungsi untuk menghitung semua nilai akhir
def hitung_semua_nilai_akhir(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai['uts'], nilai['uas'])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan hasil nilai akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("Nama: {}\tNilai Akhir: {:.2f}".format(nama, nilai_akhir))

# Program utama
def main():
    data_mahasiswa = {
        # Data mahasiswa (nama sebagai kunci dan nilai UTS serta UAS sebagai nilai dalam bentuk dictionary)
        'Mahasiswa1': {'uts': 85, 'uas': 90},
        'Mahasiswa2': {'uts': 78, 'uas': 88},
        'Mahasiswa3': {'uts': 92, 'uas': 87},
    }

    data_nilai_akhir = hitung_semua_nilai_akhir(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
