a1 = int(input('Masukkan awal deret: '))
a2 = int(input('Masukkan akhir deret: '))
j = 0

while j < a2:
    if a1 % 6 != 0 and a1 % 8 != 0:
        print(a1, end=' ')
        j += 1
    a1 += 1
    if a1 == a2:
        break
