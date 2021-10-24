# Задание 1
def num_translate():
    text=(input('Введите число на Аглийском--> '))
    print('Перевод слова на Русском--> ' + russian_dict[text])




russian_dict = {
    'one':'один',
    'two':'два',
    'three':'три',
    'four':'четыре',
    'five':'пять',
    'six':'шесть',
    'seven':'семь',
    'eight':'восемь',
    'nine':'девять',
    'ten':'десять'
}
num_translate()

