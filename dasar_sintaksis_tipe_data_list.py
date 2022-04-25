book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
print('Tampilkan Variable Daftar Buku')
print(book_list)

print('\nProses semua book_list dengan for in')
for j in book_list:
    print(j)

print('\nTampilkan isi book_list pada indeks tertentu')
print(book_list[0])
print(book_list [2])

print('\nTampilkan dengan for in range menggunakan len')
for i in range (0, len(book_list)):
    print(book_list[i])

book_list_2 = [1, 'Kenji Volume 2', -313, 3.14]
print('\nTampilkan dengan for in range, dimana tipe data tiap elemen berbeda-beda')
for i in range (0, len(book_list_2)):
    print(book_list_2[i])

print('\nKembalikan nilai awal book_list')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
print('\nPenambahan 1 buku baru dalam list')
book_list .append('5.Dunia matematik kelas 5')
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nClear list')
book_list.clear()
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nGanti elemen pertama')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
book_list [0] = '1.Eight Habits'
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nPerintah mengambil elemen ke 2 dari list')
buku = book_list.pop(1)
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nMenampilkan buku yang diambil oleh perintah pop')
print(buku)

print('\nPop jika dipakai dengan variable dikosongkan maka akan menghilangkan list paling akhir')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
book_list.pop()
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nPerintah Pop -1 untuk menghilangkan list dari belakang')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
book_list.pop(-1)
for i in range (0, len(book_list)):
    print(book_list[i])
