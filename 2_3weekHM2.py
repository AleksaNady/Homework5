my_f = open("txt2.txt", "r", encoding = "UTF-8")
content = my_f.readlines()
count_str = len(content)
print("количество строк: ", count_str)

my_f = open("txt2.txt", "r", encoding = "UTF-8")
content = my_f.read()
content = content.split()
print(f'количество слов:  {len(content)}')
my_f.close()


