import json


def convert_txt_to_json():
    ar = []

    with open('Lists\\cenz.txt', encoding='utf-8') as r:
        for i in r:
            n = i.lower().split('\n')[0]
            if n != '':
                ar.append(n)

    with open('Lists\\cenz.json', 'w',  encoding='utf-8') as e:
        json.dump(ar, e)
    e.close()
    print('Дамп мата завершен')
