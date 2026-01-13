# VARIABEL = tempat menyimpan nilai tertentu dalam program
# Dalam pyhton, kita tidak perlu mendeklarasikan tipe data.

berat_orang = 55.5  # variabel dg nama berat
manusia = ('naila', 55.5)  # variabel jenis tuple

# DEKLARASI VARIABEL
# penggunaan identifier
lebar = 10
tinggi = 4
luas_kotak = lebar * tinggi
print("luas area kotak adalah = ", luas_kotak)

"""notes : dalam penulisan identifier tidak boleh menulis menggunkan salah satu keyword python
seperti : False, class, return, is, finally, none, 
if, for, lambda, continue, True, def, from, while, nonlocal, and, del, global,
not, with, as, elif, try, or,
yield, asser, else, import, pass, break, 
accept, in, raise.
>>> apabila kita mngguenakan salah satu keyword di atas maka akan muncul syntax error"""

# VARIABLE ASSIGNMENT
"""Python Simultaneous Assignment"""
x, y = 100, 200
result = x + y
print('x + y = ', result)  # output = x + y = 300

"""Python Multiple Assignment"""
num1 = num2 = num3 = 200
print(num1, num2, num3)  # output = 200 200 200

# COMPOUND ASSIGNMENT OPERATORS (pake shorcut kayak +=, dll)
num = 200
num += 100
print(num)
num -= 100
print(num)
num *= 20
print(num)
num /= 2
print(num)
# output = line 1 (300), line 2 (200), line 3 (4000), line 4 (2000.0)

# PENGAPLIKASIAN OPERATOR ARITMATIKA
""" format >>> variabel = typedata(input("isi") """
berat = float(input("Masukkan berat anda dalam kg: "))
tinggi = float(input("Masukkan tinggi anda dalam m: "))

bmi = (berat/(tinggi ** 2))
print("BMI Anda =", bmi)

# INPUT FUNCTION
"""fungsi untuk mendapatkan input data dari user"""
Name = input("Enter Name: ")
print("Hello", Name)
# output = Hello, Name

# INPUT TO INTEGER
x = int(input("Masukkan angka pertama: "))
y = int(input("Masukkan angka kedua: "))
s = x + y
print("total dari", x, "+", y, "adalah", s)
# output = total dari  x + y adalah s

# INPUT ERRORS
"""Jika kita menginputkan karakter atau string spt "hundred" alih-alih sting "300",
maka fungsi int() tidak dapat mengubah "hundred" menjadi bilbul dan akan menghasilkan value error"""
