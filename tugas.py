'''
buat kode program untuk 
menghitung luas dan
keliling lingkaran
menggunakan python
'''
from math import pi

r = input("jari-jari lingkaran =...")
d = input("diameter lingkaran =...")
a = input("pilih keliling atau luas? ")
r = int(r)
d = int(d)
pi = 3.14

if a =='keliling':
    b = input("dengan r atau d? ")
    if b =='r':
        k = 2 * pi * r
        print("hasil keliling lingkaran adalah", k)
    elif b =='d':
        k = pi * d
        print("hasil keliling lingkaran adalah", k)
elif a =='luas':
    l = pi * r * r
    print("hasil luas lingkaran adalah: ", l)