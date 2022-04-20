"""
Program perulangan membaca buku dengan while
"""

book_count = 10
print('Mother said, "Read all your books"')
read_count = 0

understood_count = 0
print(f'books read and understood count is {understood_count} book')

while read_count < book_count * 2:
    read_count = read_count + 1
    if understood_count == 9:
        print(f'book {understood_count + 1} is not understand yet')
    else:
        understood_count = understood_count + 1
        print(f"book {understood_count} is understood")

print(f'books read and understood count is {understood_count}')
if understood_count == book_count:
    print('"Mom, All books have been read and understood')
else:
    print (f'"Mom, not all books can be understood, Budi only understand {understood_count} book"')