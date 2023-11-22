import math
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def translasi(tx, ty):
    def inner_translasi(x, y):
        return x + tx, y + ty
    return inner_translasi, f"Translasi: x' = x + {tx}, y' = y + {ty}"

def rotasi(sudut):
    def inner_rotasi(x, y):
        sudut_rad = math.radians(sudut)
        x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return x_baru, y_baru
    return inner_rotasi, f"Rotasi sejajar sumbu X: x' = x * cos({sudut}), y' = x * sin({sudut}) + y * cos({sudut})"

def dilatasi(sx, sy):
    def inner_dilatasi(x, y):
        return x * sx, y * sy
    return inner_dilatasi, f"Perbesaran Skala: x' = x * {sx}, y' = y * {sy}"

def line_equation_of(x1, y1, m):
    c = y1 - m * x1
    return f"y = {m:.2f}x + {c:.2f}"

# Titik awal
titik_awal = (2, 7)
gradien_awal = 2

# Transformasi
translasi_7_minus9, rumus_translasi = translasi(7, -9)
rotasi_60_derajat, rumus_rotasi = rotasi(60)
dilatasi_1p5_2, rumus_dilatasi = dilatasi(1.5, 2)

# Hitung titik setelah transformasi
titik_setelah_transformasi = dilatasi_1p5_2(*rotasi_60_derajat(*translasi_7_minus9(*titik_awal)))

# Persamaan garis awal
persamaan_awal = line_equation_of(titik_awal[0], titik_awal[1], gradien_awal)

# Persamaan garis setelah transformasi
persamaan_transformasi = line_equation_of(titik_setelah_transformasi[0], titik_setelah_transformasi[1], gradien_awal)

# Output
clear_terminal()
print("Rumus untuk persamaan garis yang melalui titik (x1, y1) dengan gradien m adalah: y−y1=m⋅(x−x1)")
print("Dalam hal ini, untuk titik (2, 7) dan gradien 2, kita dapat menggunakan: y−7=2⋅(x−2)")
print("Selanjutnya, kita dapat menyederhanakan persamaan tersebut untuk mendapatkan bentuk umum y=mx+c")
print("y−7=2x−4")
print("y=2x+3")
print(f"jadi, Persamaan garis yang melalui titik {titik_awal} dan bergradien {gradien_awal}: {persamaan_awal}")
print("\nRumus Transformasi:")
print(rumus_translasi)
print(rumus_rotasi)
print(rumus_dilatasi)
print(f"\nPersamaan garis baru setelah transformasi: {persamaan_transformasi}")
