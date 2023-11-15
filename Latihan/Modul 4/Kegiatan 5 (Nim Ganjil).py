def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_m(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1)

    x1, y1 = p1
    x2, y2 = p2

    M = calculate_m(x1, y1, x2, y2)
    C = y1 - M * x1

    return f"y = {M:.2f}x + {C:.2f}"

print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 2), point(7, 9)))  #202110370311279
