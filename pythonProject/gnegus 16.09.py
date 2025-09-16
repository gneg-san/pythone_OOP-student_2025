# for i in range(0, 10): # условие цикла
# выполнение внутренного кода
'''
for i in range(0, 10):
    print("Hello", i)
'''
# while (условие)
# while true:
# print("*")
'''
value_user = 1
sum_user = 0
while value_user != 0: # пока выполняется условие
    value_user = int(input("Введите число для суммирования: "))
    sum_user = sum_user + value_user
print("Сумма чисел пользователя: ", sum_user)

for i in range(0, 6):
    print("*" * i)

for i in range(0, 6):
    for j in range(0, i+1):
        print("*", end=' ')
    print()
'''
# Пользователь вводит строку. необходимо проверить ее на палиндром
user_string = input("Введите строку: \n")
counter_user = len(user_string) # функция подсчета кол-ва элементов
value_user = True # переменая для проверки палиндром
for letter_begin in range (0, counter_user):
    for letter_end in  range(0, -1):
        print("проверяется буква: ", user_string[letter_begin])
        print("проверяется буква: ", user_string[letter_end])
        if letter_begin != letter_end:
            break
    if value_user == False:
        print("слово не является палиндромом")
        break