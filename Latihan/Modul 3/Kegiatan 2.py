data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
formatted_values = []

for item in data:
    parts = item.split()
    filtered_values = [f"'{value}'" for value in parts if value.isdigit()]
    formatted_values.append(f"[{', '.join(filtered_values)}]")

for values in formatted_values:
    print(values)
