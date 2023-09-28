# Fungsi penjumlahan
def add(a, b):
    return a + b

# Fungsi pengurangan
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Fungsi untuk mengevaluasi pohon ekspresi
def tree(node):
    if isinstance(node, tuple):
        left, operator, right = node
        if operator == '+':
            return add(tree(left), tree(right))
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return node

# Contoh pohon ekspresi: (2 + 3) * (5 - 1)
expression_tree = ((2, '+', 3), '*', (5, '-', 1))


result = tree(expression_tree)

print("Hasil evaluasi pohon ekspresi:", result)