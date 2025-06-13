def num_tusk(a):
    if a == 1:
        #1
        import json

        str_json ='''
        {
          "products": [
            {
             "name": "Шоколад",
             "price": 50,
             "available": true,
             "weight": 100
            },
            {
             "name": "Кофе",
             "price": 100,
             "available": false,
             "weight": 250
            },
            {
             "name": "Чай",
             "price": 70,
             "available": true,
             "weight": 50
            }
          ]
         }
             '''                                  #утстановить скобки

        x = json.loads(str_json)

        for i in x['products']:
            print(f"Название: {i['name']}")
            print(f"Цена: {i['price']}")
            if i['available']:
                print("В наличии\n")
            else:
                print("Нет в наличии!\n")
            print(f"Вес: {i['weight']}")


    if a == 2:
        #2
        import json

        str_json ='''
        {
          "products": [
            {
             "name": "Шоколад",
             "price": 50,
             "available": true,
             "weight": 100
            },
            {
             "name": "Кофе",
             "price": 100,
             "available": false,
             "weight": 250
            },
            {
             "name": "Чай",
             "price": 70,
             "available": true,
             "weight": 50
            }
          ]
         }
             '''                                 #утстановить скобки

        x = json.loads(str_json)
        y1 = input('введите название продукта - ')
        y2 = input('введите цену продукта - ')
        y3 = input('введите наличие продукта (true/false)- ').lower()
        if y3 == 'true':
            y3 = True
        else:
            y3 = False
        y4 = input('введите вес продукта - ')

        new_product = {
            'name':y1,
            'price':y2,
            'available':y3,
            'weight':y4
        }

        x['products'].append(new_product)

        for i in x['products']:
            print('\n')
            print(f"Название: {i['name']}")
            print(f"Цена: {i['price']}")
            if i['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print(f"Вес: {i['weight']}")


    if a == 3:
        #3
        ru_en = {}

        with open('en-ru.txt','r',encoding='utf-8') as f:
            for i in f:
                i = i.strip()
                if not i or ' - ' not in i:
                    continue

                en, ru = i.split(' - ')
                en_w = [j.strip() for j in en.split(',')]
                ru_w = [j.strip() for j in ru.split(',')]

                for i in ru_w:
                    if i not in ru_en:
                        ru_en[i] = set()
                    for j in en_w:
                        ru_en[i].add(j)

        with open('ru-en.txt','w',encoding='utf-8') as f:
            for i in sorted(ru_en.keys()):
                y = sorted(ru_en[i])
                f.write(f"{i} - {', '.join(y)}\n")


while True:
    x = int(input('     Введите номер задания: '))
    if x == 0:
        break
    else:
        num_tusk(x)
'''
#ru_en = {}
#
#with open('en-ru.txt', 'r', encoding='utf-8') as f:
#    for line in f:
#        line = line.strip()
#        if not line or ' - ' not in line:
#            continue
#
#        en_part, ru_part = line.split(' - ', 1)
#        en_words = [w.strip() for w in en_part.split(',')]
#        ru_words = [w.strip() for w in ru_part.split(',')]
#
#        for ru_word in ru_words:
#            if ru_word not in ru_en:
#                ru_en[ru_word] = set()
#            for en_word in en_words:
#                ru_en[ru_word].add(en_word)
#
#sorted_ru_words = sorted(ru_en.keys())
#
#with open('ru-en.txt', 'w', encoding='utf-8') as f:
#    for ru_word in sorted_ru_words:
#        en_translations = sorted(ru_en[ru_word])
#        f.write(f"{ru_word} - {', '.join(en_translations)}\n")
'''
