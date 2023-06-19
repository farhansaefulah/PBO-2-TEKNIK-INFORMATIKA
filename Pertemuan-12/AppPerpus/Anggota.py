import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__niap = None
        self.__nama = None
        self.__jk = None
        self.__prodi = None
        self.__notelp = None
        self.__alamat = None
        self.__url = "http://localhost/ApkPerpusApi/anggota_api.php/"
                    
    @property
    def id(self):
        return self.__id
    @property
    def niap(self):
        return self.__niap
        
    @niap.setter
    def niap(self, value):
        self.__niap = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
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
    def get_by_niap(self, niap):
        url = self.__url+"?niap="+niap
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__niap = item['niap']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__prodi = item['prodi']
            self.__notelp = item['notelp']
            self.__alamat = item['alamat']
        return data
    def simpan(self):
        payload = {
            "niap":self.__niap,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "notelp":self.__notelp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_niap(self, niap):
        url = self.__url+"?niap="+niap
        payload = {
            "niap":self.__niap,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "notelp":self.__notelp,
            "alamat":self.__alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_niap(self,niap):
        url = self.__url+"?niap="+niap
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text