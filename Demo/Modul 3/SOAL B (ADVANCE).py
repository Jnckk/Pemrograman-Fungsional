import os

# Data film
movies = [
    {"title": "Avengers: Endgame", "year": 2019, "rating": 8.4, "genre": "Action"},
    {"title": "Parasite", "year": 2019, "rating": 8.6, "genre": "Drama"},
    {"title": "Nomadland", "year": 2020, "rating": 7.3, "genre": "Drama"},
    {"title": "Dune", "year": 2021, "rating": 7.9, "genre": "Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "year": 2021,
        "rating": 7.6, "genre": "Action"},
    {"title": "The French Dispatch", "year": 2021, "rating": 7.0, "genre": "Comedy"},
    {"title": "A Quiet Place Part II", "year": 2020,
        "rating": 7.4, "genre": "Horror"},
    {"title": "No Time to Die", "year": 2021, "rating": 6.8, "genre": "Action"},
    {"title": "The Power of the Dog", "year": 2021, "rating": 7.3, "genre": "Drama"},
    {"title": "Eternals", "year": 2021, "rating": 6.4, "genre": "Action"},
    {"title": "The Last Duel", "year": 2021, "rating": 7.0, "genre": "Drama"},
]

# Fungsi untuk menghitung jumlah film berdasarkan genre


def count_movies_by_genre(movies):
    genre_counts = {}
    for movie in movies:
        genre = movie['genre']
        if genre in genre_counts:
            genre_counts[genre] += 1
        else:
            genre_counts[genre] = 1
    return genre_counts

# Fungsi untuk menghitung rata-rata rating film berdasarkan tahun rilis


def average_rating_by_year(movies):
    year_ratings = {}
    year_counts = {}
    for movie in movies:
        year = movie['year']
        rating = movie['rating']
        if year in year_ratings:
            year_ratings[year] += rating
            year_counts[year] += 1
        else:
            year_ratings[year] = rating
            year_counts[year] = 1
    average_ratings = {
        year: year_ratings[year] / year_counts[year] for year in year_ratings}
    return average_ratings

# Fungsi untuk mencari film dengan rating tertinggi


def find_highest_rated_movie(movies):
    highest_rated_movie = max(movies, key=lambda x: x['rating'])
    return highest_rated_movie

# Fungsi untuk mencari film berdasarkan judul


def find_movie_by_title(movies, title):
    movie = next((movie for movie in movies if movie['title'] == title), None)
    return movie


os.system('cls' if os.name == 'nt' else 'clear')
# Program utama
while True:
    print("Pilih tugas yang ingin dilakukan:")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    choice = input("Masukkan nomor tugas (1/2/3/4/5): ")

    if choice == '1':
        print("Jumlah Film Berdasarkan Genre:")
        genre_counts = count_movies_by_genre(movies)
        print(genre_counts)
    elif choice == '2':
        print("Rata-rata Rating Film Berdasarkan Tahun Rilis:")
        average_ratings = average_rating_by_year(movies)
        print(average_ratings)
    elif choice == '3':
        print("Film dengan Rating Tertinggi:")
        highest_rated_movie = find_highest_rated_movie(movies)
        print(f"Informasi Film: {highest_rated_movie['title']}")
        print(f"Rating: {highest_rated_movie['rating']}")
        print(f"Tahun Rilis: {highest_rated_movie['year']}")
        print(f"Genre: {highest_rated_movie['genre']}")
    elif choice == '4':
        title = input("Masukkan judul film yang ingin dicari: ")
        movie = find_movie_by_title(movies, title)
        if movie is None:
            print("Film dengan judul tersebut tidak ditemukan.")
        else:
            print(f"Informasi Film: {movie['title']}")
            print(f"Rating: {movie['rating']}")
            print(f"Tahun Rilis: {movie['year']}")
            print(f"Genre: {movie['genre']}")
    elif choice == '5':
        print("Program selesai.")
        break

    user_input = input("Apakah Anda ingin melanjutkan program? (Y/N): ")
    if user_input.lower() != 'y':
        break

    os.system('cls' if os.name == 'nt' else 'clear')
