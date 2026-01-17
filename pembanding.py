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

# OPERATOR IS DAN IN
a = 1
b = 1.0
print(a == b)  # output : true
print(a is b)  # output : false
"""output
Baris ketiga menggunakan operator == untuk memeriksa apakah kedua nilai tersebut sama. 
Karena kedua nilai sama, sehingga hasilnya adalah True.
Baris keempat memeriksa apakah kedua objek itu sama. 
Karena a adalah bilangan integer sedangkan b adalah bilangan float, kedua objek tidak sama.
Dengan kata lain, mereka disimpan dalam memori yang berbeda dan oleh karena itu, hasilnya adalah False."""

"""Operator in memeriksa untuk melihat apakah kedua string cocok sebagian.
Operator in sering digunakan untuk menentukan apakah ada karakter yang cocok di dalam string,
apabila terdapat kecocokan maka akan mengembalikan nilai True dan jika tidak akan mengembalikan nilai False."""

print('aaa' in 'aaa-bbb-ccc')  # output : true
print('bbb' in 'aaa-bbb-ccc')  # output : true
print('ddd' in 'aaa-bbb-ccc')  # output : false

# LOGICAL OPERATORS
"""Terdapat 3 logical operator yang sering digunakan pada Python yaitu and, or, dan not."""
x = True
y = False
print(x and y)  # output: false
print(x or y)  # output: true
print(not x)  # output: false
print(not y)  # output: true
