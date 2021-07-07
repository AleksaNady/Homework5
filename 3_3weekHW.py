with open('salary.txt', 'r', encoding='utf-8') as my_f:
    workers_dict = {line.split()[0]: float(line.split()[1]) for line in my_f}
    print(f'средняя зарплата = {round(sum(workers_dict.values()) / len(workers_dict), 3)}\n'
          f'Зарплата меньше 20000 {[e[0] for e in workers_dict.items() if e[1] < 20000]}')


