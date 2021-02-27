print('Tipe data skalar => tipe data sederhana')
anak_1 = 'Ichika'
anak_2 = 'Nino'
anak_3 = 'Miku'
anak_4 = 'Yotsuba'
anak_5 = 'Itsuki'

print(anak_1)
print(anak_2)
print(anak_3)
print(anak_4)
print(anak_5)

print('\nTipe data list/daftar/array')
anak = ['Ichika', 'Nino', 'Miku', 'Yotsuba', 'Itsuki']
print(anak)
anak.append('Fuutarou')
print(anak)

print('\nSapa anak ke-2')
print(f'Hai {anak[1]}!')

print('\nSapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak: cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}. Hai {anak[a]}!')