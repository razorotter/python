spisok = input("Введите последовательность чисел через пробел: ")
spisok_list = [int(a) for a in spisok.split()]

num = int(input("Введите любое число: "))
if num % 1 == 0:
    spisok_list.append(num)
    print("Несортированный список: ", spisok_list)

def my_sort(spisok_list):
    for i in range(len(spisok_list)):
        idx_min = i
        for j in range(i, len(spisok_list)):
            if spisok_list[j] < spisok_list[idx_min]:
                idx_min = j
        if i != idx_min:
            spisok_list[i], spisok_list[idx_min] = spisok_list[idx_min], spisok_list[i]
    return spisok_list

print("Сортированный список:", my_sort(spisok_list))
