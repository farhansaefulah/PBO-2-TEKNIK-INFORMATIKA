#Nama : Farhan Saefulah
#NIM : 210511059
#Kelas : R2


class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def sapa(self):
        print("Halo, nama saya", self.nama)

class Pelajar(Orang):
    def __init__(self, nama, umur, nis):
        super().__init__(nama, umur)
        self.nis = nis

    def belajar(self):
        print("Saya sedang belajar di kelas.")

pelajar1 = Pelajar("Wartiyem", 19, "1920")
pelajar1.sapa()  
pelajar1.belajar()  
