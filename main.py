import matplotlib.pyplot as plt

sizes = [500, 600, 700, 800, 900, 1000, 2000, 5000, 10000]

merge_sort_random = [441, 537, 541, 633, 707, 783, 1643, 4172, 7864]
hybrid_sort_random = [57, 68, 69, 81, 92, 106, 251, 579, 1152]

merge_sort_desc = [286, 338, 399, 462, 520, 553, 1109, 3069, 6457]
hybrid_sort_desc = [22, 28, 34, 42, 49, 44, 96, 311, 581]

merge_sort_nearly_sorted = [260, 313, 370, 429, 479, 534, 1111, 2838, 5741]
hybrid_sort_nearly_sorted = [17, 19, 21, 24, 27, 34, 73, 184, 390]

plt.figure(figsize=(14, 10))

plt.subplot(2, 2, 1)
plt.plot(sizes, merge_sort_random, label='Merge Sort', marker='o', color='b')
plt.plot(sizes, hybrid_sort_random, label='Hybrid Merge Sort', marker='o', color='r')
plt.title("Случайный массив")
plt.xlabel("Размер массива")
plt.ylabel("Время (микросекунды)")
plt.legend()

# Массив, отсортированный по невозрастанию
plt.subplot(2, 2, 2)
plt.plot(sizes, merge_sort_desc, label='Merge Sort', marker='o', color='b')
plt.plot(sizes, hybrid_sort_desc, label='Hybrid Merge Sort', marker='o', color='r')
plt.title("Массив, отсортированный по невозрастанию")
plt.xlabel("Размер массива")
plt.ylabel("Время (микросекунды)")
plt.legend()

# Почти отсортированный массив
plt.subplot(2, 2, 3)
plt.plot(sizes, merge_sort_nearly_sorted, label='Merge Sort', marker='o', color='b')
plt.plot(sizes, hybrid_sort_nearly_sorted, label='Hybrid Merge Sort', marker='o', color='r')
plt.title("Почти отсортированный массив")
plt.xlabel("Размер массива")
plt.ylabel("Время (микросекунды)")
plt.legend()

# Общий график для всех типов массивов
plt.subplot(2, 2, 4)
plt.plot(sizes, merge_sort_random, label='Merge Sort (Random)', marker='o', color='b')
plt.plot(sizes, hybrid_sort_random, label='Hybrid Merge Sort (Random)', marker='o', color='r')
plt.plot(sizes, merge_sort_desc, label='Merge Sort (Descending)', marker='o', color='g')
plt.plot(sizes, hybrid_sort_desc, label='Hybrid Merge Sort (Descending)', marker='o', color='y')
plt.plot(sizes, merge_sort_nearly_sorted, label='Merge Sort (Nearly Sorted)', marker='o', color='c')
plt.plot(sizes, hybrid_sort_nearly_sorted, label='Hybrid Merge Sort (Nearly Sorted)', marker='o', color='m')

plt.title("Сравнение всех типов массивов")
plt.xlabel("Размер массива")
plt.ylabel("Время (микросекунды)")
plt.legend()

plt.tight_layout()
plt.show()
