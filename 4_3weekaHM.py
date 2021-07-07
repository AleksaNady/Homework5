#with open ('text4.txt', 'r', encoding='utf-8') as my_f:

rus_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('text_44.txt', 'w', encoding='utf-8') as f_new:
    with open('text_4.txt', encoding='utf-8') as f_open:
        f_new.writelines([line.replace(line.split()[0], rus_dic.get(line.split()[0])) for line in f_open])




