

my_dic = {}
with open("text_6.txt", encoding="utf-8") as my_f:
    for line in my_f:
        #формирование списка
        key, value = line.split(':')
        # i for i перебор каждого симлова в строке, важно учитывать проблем для исключ больших чисел
        # строка без проблемов, сплит уберет проблемы
        key_sum = sum(map(int, "".join([i for i in value if i == ' ' or '9' >= i >= '0']).split()))
        my_dic[key] = key_sum
print(f"{my_dic}")

