import json

with open('text_177.json', 'w', encoding='utf-8') as new_f:
    with open('text_7.txt', encoding='utf-8') as f_obj:
        #формирование списка
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_obj}
        # значение profit
        result = [profit, {"avarage_profit": round(sum([int(i) for i in profit.values() if int(i) > 0]) /
                                                   len([int(i) for i in profit.values() if int(i) > 0]))}]

    #ensure_ascii=False - преобразует кириллицу в ascii, indent - отстуы
    json.dump(result, new_f, ensure_ascii=False, indent=4)
