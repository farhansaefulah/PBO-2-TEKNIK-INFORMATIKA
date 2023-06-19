import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__kodepinjam = None
        self.__tglpinjam = None
        self.__tglhrskembali = None
        self.__kodebuku = None
        self.__niap = None
        self.__nipp = None
        self.__url = "http://f0832375.xsph.ru/app/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodepinjam(self):
        return self.__kodepinjam
        
    @kodepinjam.setter
    def kodepinjam(self, value):
        self.__kodepinjam = value
    @property
    def tglpinjam(self):
        return self.__tglpinjam
        
    @tglpinjam.setter
    def tglpinjam(self, value):
        self.__tglpinjam = value
    @property
    def tglhrskembali(self):
        return self.__tglhrskembali
        
    @tglhrskembali.setter
    def tglhrskembali(self, value):
        self.__tglhrskembali = value
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def niap(self):
        return self.__niap
        
    @niap.setter
    def niap(self, value):
        self.__niap = value
    @property
    def nipp(self):
        return self.__nipp
        
    @nipp.setter
    def nipp(self, value):
        self.__nipp = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodepinjam(self, kodepinjam):
        url = self.__url+"?kodepinjam="+kodepinjam
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pinjam']
            self.__kodepinjam = item['kodepinjam']
            self.__tglpinjam = item['tglpinjam']
            self.__tglhrskembali = item['tglhrskembali']
            self.__kodebuku = item['kodebuku']
            self.__niap = item['niap']
            self.__nipp = item['nipp']
        return data
    def simpan(self):
        payload = {
            "kodepinjam":self.__kodepinjam,
            "tglpinjam":self.__tglpinjam,
            "tglhrskembali":self.__tglhrskembali,
            "kodebuku":self.__kodebuku,
            "niap":self.__niap,
            "nipp":self.__nipp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodepinjam(self, kodepinjam):
        url = self.__url+"?kodepinjam="+kodepinjam
        payload = {
            "kodepinjam":self.__kodepinjam,
            "tglpinjam":self.__tglpinjam,
            "tglhrskembali":self.__tglhrskembali,
            "kodebuku":self.__kodebuku,
            "niap":self.__niap,
            "nipp":self.__nipp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodepinjam(self,kodepinjam):
        url = self.__url+"?kodepinjam="+kodepinjam
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text