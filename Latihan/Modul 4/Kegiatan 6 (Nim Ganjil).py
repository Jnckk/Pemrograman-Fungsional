def point(x, y):
    return x, y

def line_equation_of(x1, y1, m):
    c = y1 - m * x1  # Menghitung nilai C
    return f"y = {m:.2f}x + {c:.2f}"

print("Persamaan garis yang melalui titik (2,-7) dan bergradien -9:") #202110370311279
print(line_equation_of(2, -7, -9))
