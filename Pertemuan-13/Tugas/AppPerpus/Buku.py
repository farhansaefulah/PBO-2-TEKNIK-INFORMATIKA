import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__kodebuku = None
        self.__judul = None
        self.__penulis = None
        self.__penerbit = None
        self.__tahunpenerbit = None
        self.__stok = None
        self.__url = "http://f0832375.xsph.ru/app/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def judul(self):
        return self.__judul
        
    @judul.setter
    def judul(self, value):
        self.__judul = value
    @property
    def penulis(self):
        return self.__penulis
        
    @penulis.setter
    def penulis(self, value):
        self.__penulis = value
    @property
    def penerbit(self):
        return self.__penerbit
        
    @penerbit.setter
    def penerbit(self, value):
        self.__penerbit = value
    @property
    def tahunpenerbit(self):
        return self.__tahunpenerbit
        
    @tahunpenerbit.setter
    def tahunpenerbit(self, value):
        self.__tahunpenerbit = value
    @property
    def stok(self):
        return self.__stok
        
    @stok.setter
    def stok(self, value):
        self.__stok = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__kodebuku = item['kodebuku']
            self.__judul = item['judul']
            self.__penulis = item['penulis']
            self.__penerbit = item['penerbit']
            self.__tahunpenerbit = item['tahunpenerbit']
            self.__stok = item['stok']
        return data
    def simpan(self):
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahunpenerbit":self.__tahunpenerbit,
            "stok":self.__stok
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kodebuku(self, kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        payload = {
            "kodebuku":self.__kodebuku,
            "judul":self.__judul,
            "penulis":self.__penulis,
            "penerbit":self.__penerbit,
            "tahunpenerbit":self.__tahunpenerbit,
            "stok":self.__stok
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kodebuku(self,kodebuku):
        url = self.__url+"?kodebuku="+kodebuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text