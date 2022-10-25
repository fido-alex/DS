"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Угадываем число.
    1. Делим интервал в котором находится загаданное число на половинки, получается 50.
    2. Смотрим, загаданное число больше 50 или меньше 50 и находим тот деляток в котором находится загаданное число.
    3. Перебераем десяток с загаданным числом и находим его.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict_number = 50   # устанавлива предпологаемое число в половину от 100
    flag_b = 0
    flag_m = 0

    while True:
        count += 1

        if number < predict_number:    # если предпологаемое число больше загаданого уменьшаем предпологаемое число на 10
            predict_number = predict_number - 10
            flag_b_old = flag_b
            flag_b = 1                 # если предпологаемое число больше загаданого устанавливаем флаг flag_b   
        else:                          # в противном случае уменьшаем загаданное число на 10
            predict_number = predict_number + 10
            flag_m_old = flag_m
            flag_m = 1                 # если предпологаемое число меньше загаданого устанавливаем флаг flag_m
            
        if flag_b and flag_m:          # если поменялось направление с большего на меньшее или наоборот то мы нашли десяток в котором находится загаданное число
            if flag_b_old:             # смотрим направление чтоб понять в каком десятке загаданное число
                for i in list(range(predict_number - 10, predict_number + 1)):
                    count += 1
                    if i == number:
                        return count
            else:
                for i in list(range(predict_number, predict_number + 11)):
                    count += 1
                    if i == number:
                        return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    #print(random_predict(50))
