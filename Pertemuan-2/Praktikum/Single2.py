#Nama : Farhan Saefulah
#NIM : 210511059
#Kelas : R2

class Orangtua:
    def __init__(self, rambut, umur):
        self.rambut = rambut
        self.umur = umur
    def jenisRambut(self):

        print(self.rambut, "Keriting")

class Anak(Orangtua):
    def __init__(self, rambut, umur, warnaMata):
        super().__init__(rambut, umur)
        self.warnaMata = warnaMata
        
    def JenisKelamin(self):
        print("Laki Laki")
      
kucingA = Anak("Wartiyem", 15, "Ungu")
kucingA.jenisRambut() 
kucingA.JenisKelamin()