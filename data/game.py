# Импортируем необходимую нам библиотеку
import numpy as np

def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла если угадали
    
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0 # Число попыток
    
    predict = np.random.randint(1, 101) # Предполагаемое число
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # Создаём список, состоящий из будущего количества попыток отгадок 
    
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(10000)) # Загадываем список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
# Запускаем тест эффективности всех созданных алгоритмов 
if __name__ == '__main__':
    print('Run benchmarking for random_predict: ', end='')
    score_game(random_predict)

if __name__ == '__main__':
    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_core_v2)