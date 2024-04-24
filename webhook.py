import json
import requests
from settings import *
from tqdm import tqdm

from models import names_man, names_woman

# Выполняем batch-запрос
# params - словарь состоящий из команд на обновление контактов (результат работы функции generate_batch_urls)
def batch_execute(params) -> dict:
    request = requests.post(f'https://{BITRIX_URL}/rest/1/{TOKEN}/batch.json/', json=params)
    cmd = json.loads(request.request.body)
    return cmd

# Генерируем urls для отправки batch'у
# genders - список гендеров в формате [{'male': 1}, {'female': 2}, ...], где male/female - гендер, а 1 и 2 - ID пользователя в системе Битрикс 
def generate_batch_urls(genders) -> list:
    batch = {}
    result = []
    for i, item in enumerate(genders):
        for gender, id in item.items():
            if gender == 'male':
                batch['cmd_' + str(i)] = f'crm.contact.update?ID={id}&FIELDS[HONORIFIC]=HNR_RU_1'
            elif gender == 'female':
                batch['cmd_' + str(i)] = f'crm.contact.update?ID={id}&FIELDS[HONORIFIC]=HNR_RU_2'
        
        # В системе Битрикс за один запрос можно обработать только 50 записей
        if i !=0 and i % 50 == 0:
            result.append(batch_execute({'cmd': batch}))
            batch = {}

    # Обрабатываем оставшиеся запросы, не попавшие под условие выше
    if len(batch) > 0:
        result.append(batch_execute({'cmd': batch}))

    return result

# Получаем список гендеров с ID в виде ([{'male': 1}, {'female': 2}, ...])
# names - словарь имен {1: 'Имя', ...}, где 1 - ID пользователя в системе Битрикс 
def get_genders(names) -> list:
    gender = []
    
    # Проверяем какие имена являются мужскими согласно внутренней базе данных имен
    # SELECT * FROM names_man WHERE name IN ('Имя', ...)
    qs_man = names_man.select().where(names_man.name.in_(list(names.values())))
    if len(qs_man) > 0:
        for query in qs_man:
            # list(names.values()).index(query.name) - возвращаем ключ (Битрикс ID) по значению (Name)
            gender.append({'male': list(names.keys())[list(names.values()).index(query.name)]})
    
    # Делаем тоже самое для женских имен
    qs_woman = names_woman.select().where(names_woman.name.in_(list(names.values())))
    if len(qs_woman) > 0:
        for query in qs_woman:
            gender.append({'female': list(names.keys())[list(names.values()).index(query.name)]})
    
    return gender

# Устанавливаем значение г-жа/г-н для контакта
def set_genders() -> list:
    
    names = {} 
    batchs = []
    request = requests.get(f'https://{BITRIX_URL}/rest/1/{TOKEN}/crm.contact.list/', params={'start': 0})
    response = json.loads(request.content)
    
    total = response['total']
    step = 50 # В системе Битрикс за один запрос можно обработать только 50 записей

    for start in tqdm(range(0, total, step)):
        request = requests.get(f'https://{BITRIX_URL}/rest/1/{TOKEN}/crm.contact.list/', params={'start': start})
        response = json.loads(request.content)
        
        for item in response['result']:
            names[item['ID']] = item['NAME']
        
        genders = get_genders(names)
        batchs.append(generate_batch_urls(genders))
        names = {}
    return batchs


if __name__ == '__main__':
    result = set_genders()
    print(result)