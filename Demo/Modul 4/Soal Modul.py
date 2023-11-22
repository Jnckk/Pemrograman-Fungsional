import math

def translasi(tx, ty):
    def inner_translasi(x, y):
        return x + tx, y + ty
    return inner_translasi

def rotasi(sudut):
    def inner_rotasi(x, y):
        sudut_rad = math.radians(sudut)
        x_baru = x * math.cos(sudut_rad) - y * math.sin(sudut_rad)
        y_baru = x * math.sin(sudut_rad) + y * math.cos(sudut_rad)
        return x_baru, y_baru
    return inner_rotasi

def dilatasi(sx, sy):
    def inner_dilatasi(x, y):
        return x * sx, y * sy
    return inner_dilatasi

def line_equation_of(x1, y1, m):
    c = y1 - m * x1
    return f"y = {m:.2f}x + {c:.2f}"

# Titik awal
titik_awal = (3, 4)
gradien_awal = 2

# Transformasi
translasi_2_minus3 = translasi(2, -3)
rotasi_60_derajat = rotasi(60)
dilatasi_1p5_2 = dilatasi(1.5, 2)

# Titik setelah transformasi
titik_setelah_transformasi = dilatasi_1p5_2(*rotasi_60_derajat(*translasi_2_minus3(*titik_awal)))

# Persamaan garis awal
persamaan_awal = line_equation_of(titik_awal[0], titik_awal[1], gradien_awal)

# Persamaan garis setelah transformasi
persamaan_transformasi = line_equation_of(titik_setelah_transformasi[0], titik_setelah_transformasi[1], gradien_awal)

# Output
print(f"Persamaan garis yang melalui titik {titik_awal} dan bergradien {gradien_awal}: {persamaan_awal}")
print(f"Persamaan garis baru setelah transformasi: {persamaan_transformasi}")
