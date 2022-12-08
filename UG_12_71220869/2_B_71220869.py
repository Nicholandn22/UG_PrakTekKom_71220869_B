print('~ Selamat Datang di Kalkulator Sederhana ~')
abc = input('Masukkan operator matematika yang ingin Anda hitung: ')
while True:
    if abc == '+':
        a1 = int(input('Mau penjumlahan berapa: '))
        a2 = int(input('Print berapa banyak: '))
        for i in range(a2):
            print(f'{i+1} + {a2-i} = {(i+1)+(a2-i)}')
    elif abc == '-':
        a1 = int(input('Mau pengurangan berapa: '))
        a2 = int(input('Print berapa banyak: '))
        for i in range(a2):
            print(f'{i+1} + {a2-i} = {(i+1)-(a2-i)}')
    elif abc in ('x', 'X'):
        a1 = int(input('Mau perkalian berapa: '))
        a2 = int(input('Print berapa banyak: '))
        for i in range(a2):
            print(f'{i+1} X {a2-i} = {(i+1)*(a2-i)}')
    elif abc == ':':
        a1 = int(input('Mau pembagian berapa: '))
        a2 = int(input('Print berapa banyak: '))
        for i in range(2):
            print(f'{i+1} : {a2-i} = {(i+1)/(a2-i)}')
    else:
        print('Maaf, Operator Matematika yang Anda cari  belum tersedia.')
        break
    jwbn = input('Apakah Anda Ingin Menghitung Lagi? (Y/T): ')
    if jwbn in ('T', 't'):
        print('Terima Kasih dan Sampai Jumpa Lagi!')
        break
    elif jwbn in ('Y', 'y'):
        continue
    else:
        print('ERROR\nPilih Y atau T\nUlangi Program')
        break