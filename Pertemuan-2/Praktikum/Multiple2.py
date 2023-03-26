#Nama : Farhan Saefulah
#NIM : 210511059
#Kelas : R2


class Manusia:
    def __init__(self, nama ,umur):
        self.nama = nama
        self.umur = umur
        
class Penari:
    def __init__(self, style):
        self.style = style
        
class Murid (Manusia, Penari):
    def __init__(self, nama, umur, style):
        Manusia.__init__(self, nama, umur)
        Penari.__init__(self,style)
        
Farhan = Murid( 'Farhan',19, 'Hiphop')
print (Farhan.nama)
print (Farhan.umur)
print (Farhan.style)       