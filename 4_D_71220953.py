nama_mahasiswa = str(input('Masukan Nama Lengkap Anda: '))
prodi = str(input('Masukan Prodi Anda: '))
nile = str(input('Masukan Nilai(dalam Huruf) yang anda dapat: '))

try:
    nilai = str(nile.lower())
    if nilai == 'a':
        print('Nilai anda adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai == 'a-':
        print('Nilai anda adalah 3.75, kamu keren!')
    elif nilai == 'b+':
        print('Nilai anda adalah 3.25')
    elif nilai == 'b':
        print('Nilai anda adalah 3.0')
    elif nilai == 'b-':
        print('Nilai anda adalah 2.75, kurang semangat belajar nihh')
    elif nilai == 'c+':
        print('Nilai anda adalah 2.25')
    elif nilai == 'c':
        print('Nilai anda adalah 2.0')
    elif nilai == 'd':
        print('Nilai anda adalah 1, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai == 'e':
        print('Nilai anda adalah 0, niat kuliah nggak sih??')
    else:
        print('Inputan nilai yang anda masukkan tidak valid')
except:
    print('Input salah')