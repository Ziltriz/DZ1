tabel = list(range(1, 10))

def draw_table(table):
    print("  | 0 | 1 | 2")
    print("-"*13)
    for i in range(3):

        print(i, "|", tabel[0+i*3], "|", tabel[1+i*3], "|", tabel[2+i*3])
        print("-"*13)


def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= 9:
            if str(tabel[player_answer - 1]) not in "XO":
                tabel[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")


def check_win(tabel):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if tabel[each[0]] == tabel[each[1]] == tabel[each[2]]:
            return tabel[each[0]]
    return False


def main(tabel):
    counter = 0
    win = False
    while not win:
        draw_table(tabel)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1

        tmp = check_win(tabel)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    draw_table(tabel)


main(tabel)

input("Нажмите Enter для выхода!")