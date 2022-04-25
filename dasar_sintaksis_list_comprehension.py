print('\nPerintah del')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
del book_list [0]
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nPerintah del dengan list comprehension')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
del book_list [:]
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nPerintah del dengan list comprehension dengan variable')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
del book_list [0:-2] #START:END
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nPerintah del dengan list comprehension dengan variable dan step')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
del book_list [0::2] #START:END:STEP
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nMembuat list baru atau new_book_list dengan daftar buku yang sama')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
new_book_list = book_list [:]
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nMenghapus book_list lama dan mengganti dengan book_list baru dengan daftar buku yang sama')
del book_list [:]
for i in range (0, len(new_book_list)):
    print(new_book_list[i])

print('\nMembuat list baru dengan comprehension: ganjil')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
new_book_list = book_list [0::2] #START:END:STEP
for i in range (0, len(new_book_list)):
    print(new_book_list[i])

print('\nMembuat list baru dengan comprehension: genap')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
new_book_list = book_list [1::2] #START:END:STEP
for i in range (0, len(new_book_list)):
    print(new_book_list[i])

print('\nMembuat list baru dengan comprehension: -1/-2 atau membuang dari belakang')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
new_book_list = book_list [0:-1:2] #START:END:STEP
for i in range (0, len(new_book_list)):
    print(new_book_list[i])

print('\nMembuat list baru dengan comprehension: ganjil dengan perintah print sederhana')
book_list = ['1.Seven Habits', '2.How To Influnce People', '3.First Things First', '4.4DX']
print (book_list [0::2])
