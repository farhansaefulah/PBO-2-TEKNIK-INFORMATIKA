def tambah(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("Argumen harus bertipe integer")
    return a + b

try:
    hasil = tambah("5", 3)
except TypeError as e:
    print(e)