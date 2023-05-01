data = [1, 2, 0, 4, 5]
for nilai in data:
    try:
        hasil = 10 / nilai
    except ZeroDivisionError:
        print("Terjadi kesalahan pembagian dengan nol!")



