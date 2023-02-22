plat = str(input('masukkan plat nomor: ')).split()
try:
    nomor = int(plat[1])
    if nomor <= 3000:
        print('Plat nomor tersebut diperuntukan untuk mobil')
    elif nomor <= 4000:
        print('Plat nomor tersebut diperuntukkan untuk motor')
    elif nomor <= 5000:
        print('Plat nomor tersebut diperuntukkan untuk angkutan umum')
    else:
        print('Plat nomor tersebut tidak terindikasi ketiga angkutan tersesbut')
except:
    print('Plat nomor ridak terindikasi, setelah kode daerah harus berupa nomor kendaraan')
