import random

print('*********************************************')
print('***** ЛОГИЧЕСКАЯ ИГРА "КРЕСТИКИ-НОЛИКИ" *****')
print('******** ДА НАЧНЕТСЯ БИТВА РАЗУМОВ! *********')
print('*********************************************\n')

field = [i for i in range(1, 10)]
win_step = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def field_show():
    print()
    print('-------------')
    for i in range(0, 3):
        print(f'| {field[0 + i * 3]} | {field[1 + i * 3]} | {field[2 + i * 3]} |')
        print('-------------')
    print()


def step_player():
    while True:
        player_step = input('Выберите клетку для хода. Введите число от 1 до 9:\n')
        if not player_step.isdigit():
            print('Номер клетки введен не корректно\n')
            continue
        player_step = int(player_step)
        if 10 < player_step or player_step < 1:
            print('Номер клетки введен не корректно\n')
            continue
        if field[player_step - 1] == 'X' or field[player_step - 1] == '0':
            print('Клетка занята\n')
            continue

        return player_step


def step_ai(difficulty):
    if difficulty == 'easy':
        while True:
            ai_step = random.randint(0, 8)
            if field[ai_step] != 'X' and field[ai_step] != '0':
                return ai_step
    else:
        ai_step = 0
        if field[4] == 'X' and field[0] != '0' and field[2] != '0' and field[6] != '0' and field[8] != '0':
            ai_step = random.choice([0, 2, 6, 8])
            return ai_step
        if field[4] != 'X' and field[4] != '0':
            ai_step = 4
            return ai_step

        for i in win_step:
            if field[i[0]] == field[i[1]] == '0' and field[i[2]] != 'X':
                ai_step = i[2]
                return ai_step
            if field[i[1]] == field[i[2]] == '0' and field[i[0]] != 'X':
                ai_step = i[0]
                return ai_step
            if field[i[0]] == field[i[2]] == '0' and field[i[1]] != 'X':
                ai_step = i[1]
                return ai_step

        for i in win_step:
            if field[i[0]] == field[i[1]] == 'X' and field[i[2]] != '0':
                ai_step = i[2]
                return ai_step
            if field[i[1]] == field[i[2]] == 'X' and field[i[0]] != '0':
                ai_step = i[0]
                return ai_step
            if field[i[0]] == field[i[2]] == 'X' and field[i[1]] != '0':
                ai_step = i[1]
                return ai_step

        while True:
            ai_step = random.randint(0, 8)
            if field[ai_step] != 'X' and field[ai_step] != '0':
                return ai_step


def win(ai):
    win_step = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (2, 5, 8), (1, 4, 7), (0, 3, 6), (0, 4, 8), (2, 4, 6))
    for i in win_step:
        if field[i[0]] == field[i[1]] == field[i[2]] == 'X':
            field_show()
            print(f'Победил(a) {player_1}!\n')
            return True

        if field[i[0]] == field[i[1]] == field[i[2]] == '0':
            field_show()
            if ai:
                print('Победил компьюетр\n')
            else:
                print(f'Победил(a) {player_2}!\n')
            return True
    return False


def game(ai, difficulty):
    counter = 0
    while True:
        field_show()
        counter += 1
        if counter % 2 != 0:
            print(f'Ходит {player_1} (X)')
            player_step = step_player()
            field[player_step - 1] = 'X'
        else:
            if ai:
                print(f'Ходит компьютер (0)')
                player_step = step_ai(difficulty)
                field[player_step] = '0'
            else:
                print(f'Ходит {player_2} (0)')
                player_step = step_player()
                field[player_step - 1] = '0'

        if counter > 4:
            if win(ai):
                break
        if counter == 9:
            print('Ничья')
            break


def choice_ai_player():
    while True:
        choice_game = input('Выберите тип игры:\n'
                            '1. Против человека\n'
                            '2. Против компьютера\n')
        if choice_game == '1':
            ai = False
            break
        elif choice_game == '2':
            ai = True
            break
        else:
            print('Не верный ввод')
    return ai


def choice_difficulty_ai():
    print()
    while True:
        choice_difficulty = input('Выберите уровень сложности:\n'
                                  '1. Легкий\n'
                                  '2. Сложный\n')
        if choice_difficulty == '1':
            difficulty = 'easy'
            break
        elif choice_difficulty == '2':
            difficulty = 'hard'
            break
        else:
            print('Не верный ввод')
    return difficulty


ai = choice_ai_player()
if ai:
    player_1 = input('Введите имя игрока (ходит X):\n')
    player_2 = None
    difficulty = choice_difficulty_ai()
else:
    player_1 = input('Введите имя 1-го игрока (ходит X):\n')
    print()
    player_2 = input('Введите имя 2-го игрока (ходит 0):\n')
    difficulty = None

game(ai, difficulty)

while True:
    exit = False
    field = [i for i in range(1, 10)]

    if not ai:
        while True:
            repeat = input('Выберите:\n'
                           '1. Сыграть еще раз\n'
                           '2. Сменить тип игры\n'
                           '3. Выход\n')
            if repeat == '1':
                game(ai, difficulty)
                break
            elif repeat == '2':
                print('Выбрана игра с компьюетром\n')
                ai = True
                difficulty = choice_difficulty_ai()
                game(ai, difficulty)
                break
            elif repeat == '3':
                exit = True
                break
            else:
                print('Не верный ввод')
        if exit:
            break
    else:
        while True:
            repeat = input('Выберите:\n'
                           '1. Сыграть еще раз\n'
                           '2. Cменить уровень сложности\n'
                           '3. Сменить тип игры\n'
                           '4. Выход\n')
            if repeat == '1':
                game(ai, difficulty)
                break
            elif repeat == '2':
                difficulty = choice_difficulty_ai()
                game(ai, difficulty)
                break
            elif repeat == '3':
                print('Выбрана игра с человеком\n')
                if not player_2:
                    player_2 = input('Введите имя 2-го игрока (ходит 0):\n')
                ai = False
                difficulty == None
                game(ai, difficulty)
                break
            elif repeat == '4':
                exit = True
                break
            else:
                print('Не верный ввод')
        if exit:
            break
