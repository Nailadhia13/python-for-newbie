# COMPARISON OPERATOR BASIC
"""Comparison operators memeriksa hubungan ukuran dua operan yang sebanding, 
seperti angka dan string, dalam istilah seperti lebih besar dari atau kurang dari.
Hasil dari operasi ini dikembalikan sebagai Benar atau Salah. 
Tipe data yang memiliki nilai True atau False disebut Boolean."""

print('Result of 10 > 5: ', 10 > 5)  # output: Result of 10 > 5: True
print('Result of 5 < 1: ', 5 < 1)  # output: Result of 5 < 1: False
print('Result of 5 == 5:', 5 == 5)  # output: Result of 5 == 5: True
print('Result of 5 != 5:', 5 != 5)  # output: Result of 5 != 5: False
print("Result of 'a' > 'b': ", 'a' > 'b')  # output: Result of 'a' > 'b': False

# PENERAPAN COMPARISON OPERATOR
n = int(input('Masukan sebuah integer: '))
print('Apakah integer tersebut genap?', n % 2 == 0)

"""output:
Masukan sebuah integer: 60
Apakah integer tersebut genap? True"""

# STRING COMPARISON
print('aaa' == 'aaa')  # output: true
print('aaa' == 'bbb')  # output: false
print('aaa' != 'aaa')  # output: false
print('aaa' != 'bbb')  # output: true
