from os import path

# Формируем пути до файлов со списком имен 
path_names_man = path.join(path.dirname(__file__), 'names', 'male_names_rus.txt')
path_names_woman = path.join(path.dirname(__file__), 'names', 'female_names_rus.txt')

# Получаем список мужских имен
def get_names_man() -> list:
    names = []
    path = path_names_man
    with open(path, mode='r', encoding='UTF-8') as file:
        for line in file:
            names.append({'name': line.strip()})

    return names
    
# Получеам список женских имен
def get_names_woman() -> list:
    names = []
    path = path_names_woman
    with open(path, mode='r', encoding='UTF-8') as file:
        for line in file:
            names.append({'name': line.strip()})

    return names
