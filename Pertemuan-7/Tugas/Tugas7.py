
class BodyMassIndexMeta(type):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        cls.nilai_bmi = ""
        
    @classmethod
    def hitung_bmi(cls, tinggi, berat):
        bmi = berat / (tinggi ** 2)
        if bmi <= 18.5:
            cls.nilai_bmi = "Kurus"
        elif 18.5 < bmi <= 25.0:
            cls.nilai_bmi = "Normal"
        elif 25.0 < bmi <= 30.0:
            cls.nilai_bmi = "Gemuk"
        else:
            cls.nilai_bmi = "Obesitas"
        return bmi

class BodyMassIndex(metaclass=BodyMassIndexMeta):
    def __init__(self, tinggi, berat):
        self.tinggi = tinggi
        self.berat = berat
        
    def hitung(self):
        self.bmi = self.__class__.hitung_bmi(self.tinggi, self.berat)
        
    def __repr__(self):
        return f"BMI Anda adalah {self.bmi:.2f}, Anda termasuk {self.__class__.nilai_bmi}"
    
# Membuat objek bmi dengan tinggi 1.7 dan berat 70
bmi = BodyMassIndex(2.0, 80)
# Menghitung bmi
bmi.hitung()
print(bmi)
