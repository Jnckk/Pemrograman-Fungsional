# Fungsi currying untuk mengkonversi minggu, hari, jam, dan menit menjadi menit
def convert_to_minutes(weeks):
    def next_step(days):
        def then(hours):
            def and_minutes(minutes):
                return (weeks * 7 * 24 * 60) + (days * 24 * 60) + (hours * 60) + minutes
            return and_minutes
        return then
    return next_step


data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

# Membuat fungsi currying
convert = convert_to_minutes

OutputData = []
for entry in data:
    parts = entry.split()
    weeks = int(parts[0])
    days = int(parts[2])
    hours = int(parts[4])
    minutes = int(parts[6])

    result = convert(weeks)(days)(hours)(minutes)
    OutputData.append(result)

print(OutputData)
