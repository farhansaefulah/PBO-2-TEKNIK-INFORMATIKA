import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__kode = None
        self.__tglkembali = None
        self.__denda = None
        self.__kodebuku = None
        self.__niap = None
        self.__nipp = None
        self.__url = "http://f0832375.xsph.ru/app/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode(self):
        return self.__kode
        
    @kode.setter
    def kode(self, value):
        self.__kode = value
    @property
    def tglkembali(self):
        return self.__tglkembali
        
    @tglkembali.setter
    def tglkembali(self, value):
        self.__tglkembali = value
    @property
    def denda(self):
        return self.__denda
        
    @denda.setter
    def denda(self, value):
        self.__denda = value
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
    def get_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__kode = item['kode']
            self.__tglkembali = item['tglkembali']
            self.__denda = item['denda']
            self.__kodebuku = item['kodebuku']
            self.__niap = item['niap']
            self.__nipp = item['nipp']
        return data
    def simpan(self):
        payload = {
            "kode":self.__kode,
            "tglkembali":self.__tglkembali,
            "denda":self.__denda,
            "kodebuku":self.__kodebuku,
            "niap":self.__niap,
            "nipp":self.__nipp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode(self, kode):
        url = self.__url+"?kode="+kode
        payload = {
            "kode":self.__kode,
            "tglkembali":self.__tglkembali,
            "denda":self.__denda,
            "kodebuku":self.__kodebuku,
            "niap":self.__niap,
            "nipp":self.__nipp
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode(self,kode):
        url = self.__url+"?kode="+kode
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text