import requests
import json
class Pengajuan_krs:
    def __init__(self):
        self.__id=None
        self.__kode_pengajuan = None
        self.__nim_mahasiswa = None
        self.__nama_mahasiswa = None
        self.__semester = None
        self.__mata_kuliah_namadosen_matakuliah = None
        self.__dosen_wali = None
        self.__status_krs = None
        self.__url = "http://f0832638.xsph.ru/apkkrs/pengajuan_krs_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_pengajuan(self):
        return self.__kode_pengajuan
        
    @kode_pengajuan.setter
    def kode_pengajuan(self, value):
        self.__kode_pengajuan = value
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
    def semester(self):
        return self.__semester
        
    @semester.setter
    def semester(self, value):
        self.__semester = value
    @property
    def mata_kuliah_namadosen_matakuliah(self):
        return self.__mata_kuliah_namadosen_matakuliah
        
    @mata_kuliah_namadosen_matakuliah.setter
    def mata_kuliah_namadosen_matakuliah(self, value):
        self.__mata_kuliah_namadosen_matakuliah = value
    @property
    def dosen_wali(self):
        return self.__dosen_wali
        
    @dosen_wali.setter
    def dosen_wali(self, value):
        self.__dosen_wali = value
    @property
    def status_krs(self):
        return self.__status_krs
        
    @status_krs.setter
    def status_krs(self, value):
        self.__status_krs = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_pengajuan(self, kode_pengajuan):
        url = self.__url+"?kode_pengajuan="+kode_pengajuan
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_pengajuan']
            self.__kode_pengajuan = item['kode_pengajuan']
            self.__nim_mahasiswa = item['nim_mahasiswa']
            self.__nama_mahasiswa = item['nama_mahasiswa']
            self.__semester = item['semester']
            self.__mata_kuliah_namadosen_matakuliah = item['mata_kuliah_namadosen_matakuliah']
            self.__dosen_wali = item['dosen_wali']
            self.__status_krs = item['status_krs']
        return data
    def simpan(self):
        payload = {
            "kode_pengajuan":self.__kode_pengajuan,
            "nim_mahasiswa":self.__nim_mahasiswa,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "semester":self.__semester,
            "mata_kuliah_namadosen_matakuliah":self.__mata_kuliah_namadosen_matakuliah,
            "dosen_wali":self.__dosen_wali,
            "status_krs":self.__status_krs
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_pengajuan(self, kode_pengajuan):
        url = self.__url+"?kode_pengajuan="+kode_pengajuan
        payload = {
            "kode_pengajuan":self.__kode_pengajuan,
            "nim_mahasiswa":self.__nim_mahasiswa,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "semester":self.__semester,
            "mata_kuliah_namadosen_matakuliah":self.__mata_kuliah_namadosen_matakuliah,
            "dosen_wali":self.__dosen_wali,
            "status_krs":self.__status_krs
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_pengajuan(self,kode_pengajuan):
        url = self.__url+"?kode_pengajuan="+kode_pengajuan
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text