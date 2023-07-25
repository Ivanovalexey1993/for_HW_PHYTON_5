'''
Задание №5
✔ Доработаем предыдущую задачу.
✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
✔ Расширения и количество файлов функция принимает в качестве параметров.
✔ Количество переданных расширений может быть любым.
✔ Количество файлов для каждого расширения различно.
✔ Внутри используйте вызов функции из прошлой задачи.
'''

from Seminar_7.Task_HW.Homework.Module.Module_Task_4 import new_file


def expansion_files(data: dict):
    for key, value in data.items():
        new_file(key, amount_file=value)


if __name__ == '__main__':
    my_dict = {'.txt': 1, '.doc': 1, '.bin': 1, '.pdf': 1, '.md': 2}
    expansion_files(my_dict)