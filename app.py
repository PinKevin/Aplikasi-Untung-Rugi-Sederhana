print('\n==== PROGRAM PENGHITUNG KEUNTUNGAN ====\n')

hargaBeliInput = float(input("Masukkan harga beli barang anda = Rp"))
hargaJualInput = float(input("Masukkan harga jual barang anda = Rp"))


def hitungUntung(hargaBeli, hargaJual):
    untung = hargaJual - hargaBeli
    persenUntung = (untung/hargaBeli)*100
    pesan = print(
        f'\nAnda untung sebesar Rp{untung} \nPersen Keuntungan = {persenUntung}%'
    )
    return pesan


def hitungRugi(hargaBeli, hargaJual):
    rugi = hargaBeli - hargaJual
    persenRugi = (rugi/hargaBeli)*100
    pesan = print(
        f'\nAnda rugi sebesar Rp{rugi} \nPersen Keuntungan = {persenRugi}%'
    )
    return pesan


def pesanTidakUntungRugi():
    pesan = print(f'\nAnda tidak mengalami keuntungan maupun kerugian')
    return pesan


def hitungUntungBaru(persenUntung, hargaBeli):
    untungBaru = (persenUntung * hargaBeli)/100
    hargaJualBaru = hargaBeli + untungBaru
    pesan = print(
        f'\nAnda akan mengalami keuntungan sebesar Rp{untungBaru}. \nHarga jual yang baru = Rp{hargaJualBaru}'
    )
    return pesan


def pesanTerimaKasih():
    pesan = print(f'\nTerima kasih telah menggunakan aplikasi ini!')
    return pesan


untung = hargaBeliInput < hargaJualInput
rugi = hargaBeliInput > hargaJualInput
tidakUntungRugi = hargaBeliInput == hargaJualInput

if untung:
    hitungUntung(hargaBeliInput, hargaJualInput)
elif tidakUntungRugi:
    pesanTidakUntungRugi()
else:
    hitungRugi(hargaBeliInput, hargaJualInput)

if rugi or tidakUntungRugi:
    inginUntung = input(f'\nApakah anda ingin untung? (Y/N) : ').lower()
    if inginUntung == 'y':
        persenUntungBaruInput = float(
            input(f'\nMasukkan persentase keuntungan yang ingin anda peroleh = ')
        )
        hitungUntungBaru(persenUntungBaruInput, hargaBeliInput)
        pesanTerimaKasih()
    elif inginUntung == 'n':
        pesanTerimaKasih()
else:
    pesanTerimaKasih()



   
