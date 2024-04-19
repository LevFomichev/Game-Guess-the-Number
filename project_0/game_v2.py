# Импортируем необходимую нам библиотеку
import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Напишем функцию, которая принимает на вход загаданное число и возвращает число попыток угадывания.
       Нахождение загаданного числа будет происходить путём соединения двух предыдущих методов,
       которые предполагали последовательное сужение диапазона поиска и выбор следующего числа в зависимости от того,
       больше оно или меньше загаданного.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток

    predict_number = np.random.randint(1, 101) # Предполагаемое число
    
    while True:
        count += 1
        if predict_number > number:
            more_predict_number = predict_number
            predict_number = np.random.randint(1, more_predict_number)
        if predict_number < number:
            less_predict_number = predict_number
            predict_number = np.random.randint(less_predict_number, 101)
        else:
            break  # Выход из цикла если угадали
    return count 


def score_game_v2(game_core_v3) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Создаём список, состоящий из будущего количества попыток отгадок 
    
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(1000))  # Загадываем список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# Запускаем тест эффективности для game_core_v3
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game_v2(game_core_v3)   