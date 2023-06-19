import requests
import json
class Petugas:
    def __init__(self):
        self.__id=None
        self.__nipp = None
        self.__nama = None
        self.__jabatan = None
        self.__notelp = None
        self.__alamat = None
        self.__url = "http://f0832375.xsph.ru/app/petugas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nipp(self):
        return self.__nipp
        
    @nipp.setter
    def nipp(self, value):
        self.__nipp = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jabatan(self):
        return self.__jabatan
        
    @jabatan.setter
    def jabatan(self, value):
        self.__jabatan = value
    @property
    def notelp(self):
        return self.__notelp
        
    @notelp.setter
    def notelp(self, value):
        self.__notelp = value
    @property
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nipp(self, nipp):
        url = self.__url+"?nipp="+nipp
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__nipp = item['nipp']
            self.__nama = item['nama']
            self.__jabatan = item['jabatan']
            self.__notelp = item['notelp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "nipp":self.__nipp,
            "nama":self.__nama,
            "jabatan":self.__jabatan,
            "notelp":self.__notelp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nipp(self, nipp):
        url = self.__url+"?nipp="+nipp
        payload = {
            "nipp":self.__nipp,
            "nama":self.__nama,
            "jabatan":self.__jabatan,
            "notelp":self.__notelp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nipp(self,nipp):
        url = self.__url+"?nipp="+nipp
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text