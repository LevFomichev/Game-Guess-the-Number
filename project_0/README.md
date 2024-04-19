# Проект 0. Угадай число

## Оглавление

[1. Описание проекта](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Какой-кейс-решаем)

[3. Краткая информация о данных](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Краткая-информация-о-данных)

[4. Этапы работы над данными](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Этапы-работы-над-данными)

[5. Результат](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Результат)

[6. Выводы](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Выводы)

---

### Описание проекта
Создать программу угадывающую загаданное компьютером число за минимальное число попыток.

:arrow_up:[к оглавлению](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Оглавление)

---

### Какой кейс решаем
Нужно написать программу, которая угадает число за минимальное число попыток.

**Условия задания**
- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».

- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.

- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрика качества**
- Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем?**
- Учимся писать хороший код на Python.

- Учимся работать с IDE.

- Учимся работать с GitHub.

:arrow_up:[к оглавлению](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Оглавление)

---

### Краткая информация о данных
Компьютер загадываем число - для этого используется функция random из библиотеки NumPy, которая будет 1000 раз генерировать случайное число от 1 до 100.

:arrow_up:[к оглавлению](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Оглавление)

---

### Этапы работы над данными
Импортируем библиотеку, которая нам пригодится для генерации случайных чисел.

- **Подход 1: Случайное угадывание**

Простейший способ решения - научить программу случайным образом выбирать число до тех пор, пока оно не будет угадано. Этот способ не дает хорошего результата, однако будет для нас хорошей стартовой точкой:

```py
import numpy as pn

def random_predict(number: int = 1) -> int:
    count = 0 # Число попыток

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Предполагаемое число
        if number == predict_number:
            break # Выход из цикла если угадали
    
    return count
```

- **Подход 2: Угадывание с коррекцией**

Сначала устанавливаем любое случайное число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного:

```py
import numpy as np

def game_core_v2(number: int = 1) -> int:
    count = 0 # Число попыток
    
    predict = np.random.randint(1, 101) # Предполагаемое число
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count
```

- **Функция для оценки качества**

Создаём функцию, необходимую для определения числа попыток «угадывания» загаданного числа программой:

```py
import numpy as np

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
    
```

- **Оценка работы алгоритмов**

Определяем, какой из подходов лучше:

```py
if __name__ == '__main__':
    print('Run benchmarking for random_predict: ', end='')
    score_game(random_predict)

if __name__ == '__main__':
    print('Run benchmarking for game_core_v2: ', end='')
    score_game(game_core_v2)

# Ваш алгоритм угадывает число в среднем за: 100 попытки

# Ваш алгоритм угадывает число в среднем за: 32 попытки
```

- **Подход 3: Алгоритм минимального и максимального порога**

Напишем функцию, которая принимает на вход загаданное число и возвращает число попыток угадывания. Нахождение загаданного числа будет происходить путём `добавления минимального и максимального порога для нового создаваемого числа по предложенному к ответу числу` а так же всё того же `последовательного сужения диапазона поиска и выбора следующего числа в зависимости от того, больше оно или меньше загаданного`:

```py
# Импортируем необходимую нам библиотеку
import numpy as np

def game_core_v3(number: int = 1) -> int:
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
    
    count_ls = [] # Создаём список, состоящий из будущего количества попыток отгадок 
    
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(1000))  # Загадываем список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

# Запускаем тест для game_core_v3
if __name__ == '__main__':
    print('Run benchmarking for game_core_v3: ', end='')
    score_game_v2(game_core_v3)

# Ваш алгоритм угадывает число в среднем за: 6 попытки   
```

:arrow_up:[к оглавлению](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Оглавление)

---

### Результат
Результатом проделанной работы стало успешное сокращение среднего числа количества попыток при 1000 повторений - со 100 `до всего 6!` Что является отличным результатом при столь минимальных модификаций функций.

:arrow_up:[к оглавлению](https://github.com/LevFomichev/sf_data_science/blob/main/project_0/README.md#Оглавление)

---

### Выводы
Подводя итоги проделанной работы, можно смело утверждать, что самым эффективным методом отгадывания случайного числа из всех предложенных вариантов будет являться именно метод, основанный на `алгоритме создания минимального и максимального порога` для всех следующих чисел, в зависимости от того, больше они или меньше искомого.