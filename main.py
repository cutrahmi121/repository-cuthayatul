

pengambilan_prodak = int(input('Masukkan nilai pengambilan produk: '))
kendaraan = int(input('Masukkan nilai Kendaraan: '))

if pengambilan_prodak>= 1000000:
  if (kendaraan > 8):
    print('Selamat Pengambilan produk dan mobil lulus')
  else:
    print('tidak dapat Pengambilan produk dan mobil dikarenakan salah satu kurang')
else:
  if (pengambilan_prodak <= 1000000):

    print('jumlah pengambilan produk kurang ')
  else:
    print('jumlah pengambilan produk cukup ')

  if (kendaraan >8):
    print('jumlah mobil cukup ')
  else:
    print('jumlah mobil kurang ')

