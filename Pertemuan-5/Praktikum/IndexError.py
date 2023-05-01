list_buah = ["apel", "jeruk", "mangga"]
try:
    buah_keempat = list_buah[3]
except IndexError:
    print("Index yang diminta melebihi jumlah elemen dalam list!")