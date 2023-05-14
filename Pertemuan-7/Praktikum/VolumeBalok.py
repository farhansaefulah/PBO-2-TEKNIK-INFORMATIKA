class BalokMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
# Tambahkan method untuk menghitung volume dan Luas Permukaan Persegi
        def Volume(cls, panjang, lebar, tinggi):
            return panjang * lebar * tinggi
        cls.Volume = classmethod(Volume)
        def Lpermukaan(cls, panjang, lebar, tinggi):
            return 2 * (panjang*lebar + panjang*tinggi + lebar*tinggi)
        cls.Lpermukaan = classmethod(Lpermukaan)
class Balok(metaclass=BalokMeta):
    pass
s = Balok()
# Menghitung Volume balok dengan panjang= 4 lebar= 5 dan tinggi = 5
volume_balok = Balok.Volume(4,5,5)
print("Volume Balok :", volume_balok)
# Menghitung Lpermukaan balok dengan panjang= 4 lebar= 6 dan tinggi = 5
Lpermukaan_balok = Balok.Lpermukaan(4,6,5)
print("Lpermukaan Balok:", Lpermukaan_balok)
