import random
import math

# print("��������:", *sorted(random.sample(range(1, 18), 4)))
# >>> ��������: 2 7 9 14

# ����������:
# 2 --- �����������
# 7 --- ������
# 9 --- �������������
# 14 --- �����������

# �����
int_numbers = [i for i in range(1000000)]
random.shuffle(int_numbers)

# ������������
float_numbers = [random.randrange(-1000, 1001) / 1000 for i in range(99999)]

# �����������
complex_numbers = []
r = 21 / 9
for i in range(42000):
    angle = random.uniform(0, 2 * math.pi)

    x = r * math.cos(angle)
    y = r * math.sin(angle)

    complex_number = complex(x, y)

    if complex_number not in complex_numbers:
        complex_numbers.append(complex_number)

# ������
with open("mumu.txt", "r") as f:
    strings = f.read().split()


# ����������� - �����
def radix_sort(mas):
    max_length = len(str(max(mas)))

    tmp_mas = [str(num).zfill(max_length) for num in mas]

    for i in reversed(range(max_length)):
        buckets = [list() for _ in range(10)]

        for num in tmp_mas:
            index = int(num[i])
            buckets[index].append(num)

        tmp_mas = [num for bucket in buckets for num in bucket]

    return [int(num) for num in tmp_mas]


# ������������� - ������������
def heap_sort(mas):
    n = len(mas)
    tmp_mas = mas[:]

    for i in range(n // 2 - 1, -1, -1):
        heapify(tmp_mas, n, i)

    for i in range(n - 1, 0, -1):
        tmp_mas[0], tmp_mas[i] = tmp_mas[i], tmp_mas[0]
        heapify(tmp_mas, i, 0)

    return tmp_mas


def heapify(mas, n, i):
    largest = i

    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and mas[i] < mas[l]:
        largest = l

    if r < n and mas[largest] < mas[r]:
        largest = r

    if largest != i:
        mas[i], mas[largest] = mas[largest], mas[i]

        heapify(mas, n, largest)


# ����������� - �����������
def bubble_sort(mas):
    n = len(mas)
    tmp_mas = mas[:]

    for i in range(n - 1):
        swap = False
        for j in range(n - i - 1):
            if tmp_mas[j].real > tmp_mas[j + 1].real:
                tmp_mas[j], tmp_mas[j + 1] = tmp_mas[j + 1], tmp_mas[j]
                swap = True
        if not swap:
            break

    return tmp_mas


# ������ - ������
def gnome_sort(mas):
    n = len(mas)
    tmp_mas = mas[:]

    i = 0
    while i < n:
        if i == 0 or tmp_mas[i] >= tmp_mas[i - 1]:
            i += 1
        else:
            tmp_mas[i], tmp_mas[i - 1] = tmp_mas[i - 1], tmp_mas[i]
            i -= 1

    return tmp_mas


sorted_int = radix_sort(int_numbers)
sorted_float = heap_sort(float_numbers)
sorted_complex = bubble_sort(complex_numbers)
sorted_string = gnome_sort(strings)

print("���������� ����� �����:", sorted(int_numbers) == sorted_int)
print("���������� ������������ �����:", sorted(float_numbers) == sorted_float)
print("���������� ����������� �����:", sorted(complex_numbers, key=lambda x: x.real) == sorted_complex)
print("���������� �����:", sorted(strings) == sorted_string)

