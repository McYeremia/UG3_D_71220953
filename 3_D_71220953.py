a1 = int(input('Masukkan awal deret: '))
a2 = int(input('Masukkan akhir deret: '))
j = 0

for i in range(a1,a2):
    j+= 1 and print(a1, end=' ') if a1 % 6 != 0 and a1 % 8 != 0 else print() 
    a1 += 1
