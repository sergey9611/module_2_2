print('Ввод в консоль:')
first = int(input())
second = int(input())
third = int(input())
if first != second and first != third and second != third:
    print(0)
elif first == second and first == third and second == third:
    print(3)
else:
    print(2)
