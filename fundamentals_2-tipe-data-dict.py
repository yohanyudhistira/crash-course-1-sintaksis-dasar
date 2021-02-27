"""
Tipe data dictionary sekedar menghubungkan antara KEY dan VALUE
KVP = Key Value Pair
Dictionary = Kamus
"""

kamus_ind_eng = {'ayah': 'father', 'ibu': 'mother', 'istri': 'wife', 'anak': 'child'}
print(kamus_ind_eng)
print(kamus_ind_eng['anak'])
print(kamus_ind_eng['ayah'])

print('\nData ini dikirimkan oleh server Gojek untuk memberikan info mengenai driver di sekitar user aplikasi')
data_dari_server_gojek = {
    'tanggal': '2021-02-27',
    'driver_list': [{'nama': 'Shinra', 'jarak': 10},
                    {'nama': 'Arthur', 'jarak': 15},
                    {'nama': 'Sho', 'jarak': 20},
                    {'nama': 'Tamaki', 'jarak': 25}
                    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di sekitar Anda {data_dari_server_gojek['driver_list']}")
print(f"Driver #1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver_list'][3]}")
print(f"Driver terdekat berjarak {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
