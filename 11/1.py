mas = []
mas_need = []

while len(mas) < 10:
    mas.append(int(input()))

for i in range(len(mas) - 1):
    mas_need.append(mas[i] + mas[i + 1])
print(mas_need)