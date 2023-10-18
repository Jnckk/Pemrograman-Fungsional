import os
import random


def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')


def create_board(width):
    return [[' ' for _ in range(width)] for _ in range(width)]


def print_board(board):
    for i in range(len(board)):
        print('+---' * len(board) + '+')
        for j in range(len(board[i])):
            print('| {} '.format(board[i][j]), end='')
        print('|')
    print('+---' * len(board) + '+')


def generate_positions(width):
    bidak_x, bidak_y = random.randint(
        0, width - 1), random.randint(0, width - 1)
    goals_x, goals_y = random.randint(
        0, width - 1), random.randint(0, width - 1)
    return (bidak_x, bidak_y), (goals_x, goals_y)


def is_game_over(bidak, goals):
    return bidak == goals


def move_bidak(x, y, direction): return (x + direction[0], y + direction[1])


def main():
    while True:
        clear_terminal()
        width = int(input("Masukkan lebar board: "))
        board = create_board(width)
        bidak, goals = generate_positions(width)
        board[bidak[0]][bidak[1]] = 'A'
        board[goals[0]][goals[1]] = 'O'

        print("Selamat datang di permainan!")

        while not is_game_over(bidak, goals):
            clear_terminal()
            print_board(board)
            navigasi = input("Masukkan navigasi (contoh: WASSDD): ").upper()

            for direction in navigasi:
                try:
                    if direction == "W":
                        bidak_x, bidak_y = bidak
                        bidak = move_bidak(bidak_x, bidak_y, (-1, 0))
                    elif direction == "S":
                        bidak_x, bidak_y = bidak
                        bidak = move_bidak(bidak_x, bidak_y, (1, 0))
                    elif direction == "A":
                        bidak_x, bidak_y = bidak
                        bidak = move_bidak(bidak_x, bidak_y, (0, -1))
                    elif direction == "D":
                        bidak_x, bidak_y = bidak
                        bidak = move_bidak(bidak_x, bidak_y, (0, 1))
                    else:
                        print("Arah tidak valid. Gunakan 'W', 'A', 'S', atau 'D'.")
                        continue

                    board[bidak_x][bidak_y] = ' '
                    board[bidak[0]][bidak[1]] = 'A'
                    board[goals[0]][goals[1]] = 'O'
                except IndexError:
                    print("Bidak bergerak di luar batas board.")
                    continue

        clear_terminal()
        print_board(board)

        if is_game_over(bidak, goals):
            board[goals[0]][goals[1]] = 'A'
            clear_terminal()
            print_board(board)
            print("Selamat, Anda menang!")
        else:
            print("Maaf, Anda kalah!")

        play_again = input("Apakah Anda ingin bermain lagi? (Y/N): ").upper()
        if play_again != 'Y':
            break


if __name__ == "__main__":
    main()
