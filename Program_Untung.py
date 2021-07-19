print('\n==== PROGRAM PENGHITUNG KEUNTUNGAN ====\n')

hargaBeli = float(input("Masukkan harga beli barang anda = Rp"))
hargaJual = float(input("Masukkan harga jual barang anda = Rp"))

untung = hargaJual - hargaBeli
rugi = hargaBeli - hargaJual

persenUntung = ((hargaJual - hargaBeli)/hargaBeli)*100
persenRugi = ((hargaBeli - hargaJual)/hargaBeli)*100

if hargaJual > hargaBeli:
   print('\nAnda akan untung sebesar = Rp \b',untung,'\nPersentase keuntungan =', persenUntung,'%\n')
elif hargaJual == hargaBeli:
   print('\nAnda tidak akan mengalami keuntungan maupun kerugian\n') 
else:
   print('\nAnda akan rugi sebesar = Rp \b',rugi,'\nPersentase kerugian =', persenRugi,'%\n')


if hargaJual < hargaBeli or hargaJual == hargaBeli:
   inginUntung = bool(int(input('Apakah anda ingin mengganti harga jual anda sehingga mengalami keuntungan? (Jawab dengan 0 untuk TIDAK dan 1 untuk YA) : ')))
   if inginUntung == True:
      targetUntung = float(input('\nMasukkan persentase keuntungan yang anda inginkan dari harga beli produk anda = '))
      untungBaru = (targetUntung*hargaBeli)/100
      hargaJualBaru = hargaBeli + untungBaru
      print('\nAnda akan mendapatkan untung sebesar = Rp',untungBaru,'\nHarga jual barang anda yang baru = Rp',hargaJualBaru,'\n')
      print('==== TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI! ====\n')
   else:
      print('\n==== TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI! ====\n')
else:
   print('==== TERIMA KASIH SUDAH MENGGUNAKAN PROGRAM INI! ====\n')


   
