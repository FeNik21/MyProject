import random as r

#камень бьет ножницы к > н 6, 7
#бумага бьет камень б > к 6, 6
#ножницы бьет бумагу н > б 7, 6
# list = ['камень','ножницы', 'бумага']
# a = r.choice(list)
# print(a)
# b = str(input('Player: '))
# if a == b:
#     print('Ничья')
# elif a <= b:
#     print('player')
# elif a >= b:
#     print('comp')

list1 = ['кот','собака','ножницы','лестница','компьютер',
         'гамбургер','слон','нога','питон','телефон']
#выбор рандомного слова из списка и подсчет кол-ва симоволов
word = r.choice(list1)
num_word = len(word)
print(word)
life = 4
print('_' * num_word)
#цикл ввода буквы
for let in word:
    letter = str(input('Введите латинскую букву: '))
    print(letter+ '_' )
    if letter == let:
        print(letter + '_' * num_word)
    elif letter != let:
        print("Не угадал")
        life -= 1
        print("Потратил  1 попытку осталось: " , life)
    if life == 0:
        print('Игра окончена')
        break
        print('Ты выиграл')
    continue
#на данном моменте если делаешь ошибку то надо ввести через букву то есть т_ле_он

