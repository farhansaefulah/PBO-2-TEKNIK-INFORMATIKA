import requests
import json
class Mahasiswa:
    def __init__(self):
        self.__id=None
        self.__nim_mahasiswa = None
        self.__nama_mahasiswa = None
        self.__tempat_tanggallahir_mahasiwa = None
        self.__jenis_kelamin = None
        self.__alamat_mahasiswa = None
        self.__semester = None
        self.__url = "http://f0832638.xsph.ru/apkkrs/mahasiswa_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nim_mahasiswa(self):
        return self.__nim_mahasiswa
        
    @nim_mahasiswa.setter
    def nim_mahasiswa(self, value):
        self.__nim_mahasiswa = value
    @property
    def nama_mahasiswa(self):
        return self.__nama_mahasiswa
        
    @nama_mahasiswa.setter
    def nama_mahasiswa(self, value):
        self.__nama_mahasiswa = value
    @property
    def tempat_tanggallahir_mahasiwa(self):
        return self.__tempat_tanggallahir_mahasiwa
        
    @tempat_tanggallahir_mahasiwa.setter
    def tempat_tanggallahir_mahasiwa(self, value):
        self.__tempat_tanggallahir_mahasiwa = value
    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
        
    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value
    @property
    def alamat_mahasiswa(self):
        return self.__alamat_mahasiswa
        
    @alamat_mahasiswa.setter
    def alamat_mahasiswa(self, value):
        self.__alamat_mahasiswa = value
    @property
    def semester(self):
        return self.__semester
        
    @semester.setter
    def semester(self, value):
        self.__semester = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nim_mahasiswa(self, nim_mahasiswa):
        url = self.__url+"?nim_mahasiswa="+nim_mahasiswa
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_mahasiswa']
            self.__nim_mahasiswa = item['nim_mahasiswa']
            self.__nama_mahasiswa = item['nama_mahasiswa']
            self.__tempat_tanggallahir_mahasiwa = item['tempat_tanggallahir_mahasiwa']
            self.__jenis_kelamin = item['jenis_kelamin']
            self.__alamat_mahasiswa = item['alamat_mahasiswa']
            self.__semester = item['semester']
        return data
    def simpan(self):
        payload = {
            "nim_mahasiswa":self.__nim_mahasiswa,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "tempat_tanggallahir_mahasiwa":self.__tempat_tanggallahir_mahasiwa,
            "jenis_kelamin":self.__jenis_kelamin,
            "alamat_mahasiswa":self.__alamat_mahasiswa,
            "semester":self.__semester
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nim_mahasiswa(self, nim_mahasiswa):
        url = self.__url+"?nim_mahasiswa="+nim_mahasiswa
        payload = {
            "nim_mahasiswa":self.__nim_mahasiswa,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "tempat_tanggallahir_mahasiwa":self.__tempat_tanggallahir_mahasiwa,
            "jenis_kelamin":self.__jenis_kelamin,
            "alamat_mahasiswa":self.__alamat_mahasiswa,
            "semester":self.__semester
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nim_mahasiswa(self,nim_mahasiswa):
        url = self.__url+"?nim_mahasiswa="+nim_mahasiswa
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
