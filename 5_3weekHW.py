from random import randint

with open("tesk_5_2.txt", mode="w+",encoding="utf-8") as my_f:
    # создаем список и делаем each el строковой, конкатенируем с проблемом ""
    my_f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
    #поднятие курсора на верх
    my_f.seek(0)
    # приоритет действий, считываеми и сплиту из-за проблемов = > делаем each el с помощью map int, затем sum
    print(sum(map(int, my_f.readline().split())))


