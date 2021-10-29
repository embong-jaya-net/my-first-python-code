# KONSTRUKSI DASAR PYTHON
# SEQUENTIAL: Eksekusi berurutan
print('Ibu memerintahkan Budi pergi ke toko membeli 1 botol susu atau jika ada telur makan beli 1 botol susu dan 6 butir telur')
print('Budi menjawab, "Siap Mami"')
print('Budi pergi ke toko')

# PERCABANGAN : Eksekusi Melompat
ada_susu = False
ada_telur = True
if ada_susu:
    if ada_telur:
        print('Budi membeli 1 botol susu dan 6 butir telur')
    else:
        print('Budi membeli 1 botol susu')
else:
    print('Budi tidak membeli apapun')

