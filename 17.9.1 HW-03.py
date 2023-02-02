def sort_list(numbers_list_mod):
    for i in range(len(numbers_list_mod)):
        for j in range(len(numbers_list_mod) - i - 1):
            if numbers_list_mod[j] > numbers_list_mod[j + 1]:
                numbers_list_mod[j], numbers_list_mod[j + 1] = numbers_list_mod[j + 1], numbers_list_mod[j]
    return numbers_list_mod

def search_bin(numbers_list_mod, number_user, left, right):
    if left > right:
        return False
    middle = (right + left) // 2
    if numbers_list_mod[middle] == number_user:
        return middle
    elif number_user < numbers_list_mod[middle]:
        return search_bin(numbers_list_mod, number_user, left, middle - 1)
    else:
        return search_bin(numbers_list_mod, number_user, middle + 1, right)

message = True
while message:
    try:
        numbers_list = input("Введите последовательность чисел через пробел:").split()

        numbers_list_mod = [int(x) for x in numbers_list]

        numbers_list_mod = sort_list(numbers_list_mod)
        print("После сортировки:", numbers_list_mod)

        number_user = input("Введите число для определения индекса:")
        number_user = int(number_user)

        message = False
    except ValueError:
        print(f"Ошибка {ValueError}")
        print("Введено недопустимое значение!")
        message = input("Повторить ввод? y/n:")
        if message != 'y':
            print("Завершение")
            message = False
            exit(1)
        else:
            print("В следующий раз будьте внимательнее!")

if number_user not in numbers_list_mod:
    print(f"Нет числа {number_user} в последовательности {numbers_list_mod}")
    if number_user < min(numbers_list_mod):
        print(f"Число {number_user} меньше минимального в последовательности {min(numbers_list_mod)}")
    if number_user > max(numbers_list_mod):
        print(f'Число {number_user} больше максимального в последовательности {max(numbers_list_mod)}')
        exit(1)

number_index = search_bin(numbers_list_mod, number_user, 0, len(numbers_list_mod) - 1)

print("Индекс введенного числа в списке:", number_index)

if number_index == 0:
    print(f"Число {number_user} первое в последовательности, следующее {numbers_list_mod[number_index + 1]}")
elif number_index == int(len(numbers_list_mod) - 1):
    print(f"Число {number_user} последнее в последовательности, предыдущее {numbers_list_mod[number_index - 1]}")
else:
    print(f"Предыдущее значение {numbers_list_mod[number_index - 1]}, следующее {numbers_list_mod[number_index + 1]}")


