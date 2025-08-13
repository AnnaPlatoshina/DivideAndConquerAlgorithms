import time
import random


# Задача 01: Рекурсивная функция для вычисления n-го числа Фибоначчи
def fibonacci(n):
    """Рекурсивная функция для вычисления n-го числа Фибоначчи"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Задача 02: Рекурсивный поиск максимума с использованием "Разделяй и властвуй"
def find_max(arr, start, end):
    """Рекурсивная функция для нахождения максимального элемента"""
    # Базовый случай: если в подмассиве один элемент
    if start == end:
        return arr[start]

    # Разделяем массив на две части
    mid = (start + end) // 2
    max_left = find_max(arr, start, mid)
    max_right = find_max(arr, mid + 1, end)

    # Возвращаем максимальное из двух частей
    return max(max_left, max_right)


# Задача 03: Реализация быстрой сортировки (QuickSort)
def quicksort(arr):
    """Реализация быстрой сортировки"""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


# Задача 04: Сравнение производительности быстрой сортировки и сортировки вставками
def insertion_sort(arr):
    """Сортировка вставками для сравнения"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def test_sorting_algorithms():
    """Тестирование производительности сортировок"""
    lengths = [10, 100, 1000]

    for length in lengths:
        arr = [random.randint(0, 1000) for _ in range(length)]

        # Тестируем быструю сортировку
        start = time.time()
        quicksort(arr.copy())
        quick_time = time.time() - start

        # Тестируем сортировку вставками
        start = time.time()
        insertion_sort(arr.copy())
        insertion_time = time.time() - start

        print(f"\nДля {length} элементов:")
        print(f"Быстрая сортировка: {quick_time:.6f} сек")
        print(f"Сортировка вставками: {insertion_time:.6f} сек")


def main():
    print("=" * 50)
    print("Задача 01: Рекурсивное вычисление числа Фибоначчи")
    n = 5
    print(f"Fibonacci({n}): {fibonacci(n)}")
    print("Примечание: стек вызовов для n=5 будет иметь глубину 5")

    print("\n" + "=" * 50)
    print("Задача 02: Поиск максимального элемента (разделяй и властвуй)")
    arr = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"Исходный массив: {arr}")
    print(f"Максимальный элемент: {find_max(arr, 0, len(arr) - 1)}")

    print("\n" + "=" * 50)
    print("Задача 03: Быстрая сортировка (QuickSort)")
    unsorted_list = [3, 6, 8, 10, 1, 2, 1]
    print(f"Несортированный список: {unsorted_list}")
    sorted_list = quicksort(unsorted_list)
    print(f"Отсортированный список: {sorted_list}")

    print("\n" + "=" * 50)
    print("Задача 04: Сравнение производительности сортировок")
    test_sorting_algorithms()


if __name__ == "__main__":
    main()