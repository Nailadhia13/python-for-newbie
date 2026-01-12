# Halo semua! Aku Nailadhia Martafani
# aku mahasiswa ilmu komputer di UNILA
# aku baru saja belajar new language, yaitu python setelah sebelumnya belajar c++
# untuk kalian yang juga baru belajar, boleh pahami kode-kode di bawah ini ya
# awal mula dibuat tanggal 9/1/26

print("====================================")
print("             PYTHON DASAR           ")
print("====================================")

# SYNTAX
print("hello world")            # akan menampilkan output dalam()
print("hello " * 3)             # akan mencetak hello sebanyak 3 kali (looping)
# akan mencetak  kalimat yang sama seperti yang di line 1, "" dan '' sama fungsinya
print('hello world')
# akan mencetak kalimat yg sama seperti line sebelumnya
print('Hello ' + 'world')
# print("Hello" * "world") ,, ini akan error karena perkalian tidak bisa digunakan dalam tipe data string

"""ERROR
1. syntax error ketika salah dalam penulisan kode
2. runtime error ketika pengguna menginputkan data yang salah """

"""DATA TYPE
int = 3
string = 'naila cantik'
float = 155.5 
Boolean = true or false
Kompleks = 5 + 6j
List and Tuple= [2, 10, 12]
Dictionary = {'name' = 'nai', 'age' = 18, 'height' = 155.5}"""

type(100)
type('nai')
type(15.5)
type(5 + 6j)

# CARA MENGUBAH TIPE DATA
int('10') / 2
# ubah string '10' menjasi bilbul dan dibagi dengan 2
'i like number' + str(13)
# ubah angka 13 menjadi string dan gunakan operator +

"""TIPE DATA STRING
- String Characteristics
    Dalam Python, string disebut sebagai urutan karakter
    >>> Nama pengguna, ID, dan kata sandi dapat dinyatakan sebagai string.
- String dalam Python adalah bentuk di mana setiap huruf terhubung.
- Operasi penjumlahan dan perkalian dimungkinkan untuk string dalam Python.
- Huruf dan spasi dalam sebuah string juga disebut sebagai character."""

# STRING INDEXING (digunakan untuk mengakses satu  karakter tertentu dalam sebuah string)
# >>>Positive indexing
"halow"[0]  # output = h
# >>>Negative indexing (untuk dapet character terakhir)
"halow"[-1]  # output = w

# STRING BUILT-IN FUNCTION
# >>> split() = untuk memisahkan string sesuai dengan separator yang diinginkan
teks = "halo, nama saya, nai"
x = teks.split(", ")
print(x)
# output = ['halo', 'nama saya', 'naii']

# >>> islower() = ngecek apakah all of element in string itu huruf kecil
a = "HaLo"
b = "halo"

print(a.islower())
print(b.islower())
# output = line 1 > False, line 2 > true

# >>> count()  = menghitung berapa kali sebuah value muncul dalam string
teks = "Halo semuanya, disini saya bersama dengan budi semuanya"
x = teks.count("semuanya")
print(x)
# output = 2

# OPERATOR
print(100 + 13)  # penjumlahan
print(100 - 13)  # pengurangan
print(100 * 13)  # perkalian
print(100 / 13)  # pembagian
print(100 % 13)  # modulo atau sisa bagi
print(100 // 13)  # pembulatan ke bawah (flooring)
print(2 ** 3)  # perpangkatan

"""urutan prioritas operator
1. () = tanda kurung
2. ** = power
3. ~, +, - = monadic 
4. *, /, %, // = kali, nagi, modulo, flooring
5. +, - = jumlah dan selisih
6. >>, << = pergeseran bit kode biner
7. & = operator AND
8. ^, | = operator XOR dan OR
9. <=, <, >, >= = membandingkan dua nilai
10. ==, != = setara dan tidak setara
11. =, %=, /=, //=, -=, +=, *=, **= = shortcut operator
12. is, is not = memeriksa dua variabel, jika sama maka true
13. in, not in = string built
14. not, or, and = operator logika """

# BUILT IN-FUNCTION
# >>> int() = mengubah nilai yang ditentukan, menjadi bilbul
x = int("12")
y = int(7.5)

print(x)
print(y)
# output = line 1 (12), line 2 (7)

# >>> pow() = mendapat niali pangkat dari suatu bilangan
x = pow(3, 3)  # 3 pangkat 3
y = pow(3, -3)  # 3 pangkat -3

print(x)
print(y)
# output = line 1 (27), line 2 (0.015625)

# >>> str() = mengubah sebuah objek menjadi string
x = str(12)
y = str(12.5)

print(type(x))
print(type(y))

# output = line 1 (<class 'str'>), line 2 (<class 'str'>)
