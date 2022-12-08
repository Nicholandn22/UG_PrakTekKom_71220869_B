print('SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERLUBANG')
q = int(input('Masukan Angka : '))
print('')
print(' '*(q-2),'*')
for w in range ((q-2),0,-1):
    print(' '*(w-1),'**')
print('**'*q)