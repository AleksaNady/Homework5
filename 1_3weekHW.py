#открытия файла на запись - файл не сущетвует
fname = input('Файл: ')
f = open(fname,'w', encoding = "UTF-8")
while True:
    s = input("Ввод данных в файл: ")
    #если была введена пустая строка, то цикл должен прерываться
    if s == '': break
    f.writelines(f"{s}\n")

f.close()

