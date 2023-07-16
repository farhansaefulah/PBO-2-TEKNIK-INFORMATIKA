import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Mahasiswa import *
class FrmMahasiswa:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1200x630")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#001C30")
        Label(mainFrame, text= '🎓DATA MAHASISWA',font="Poppins 16 bold",fg="White",bg="#001C30").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| NIM MAHASISWA                                   :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| NAMA MAHASISWA                               :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| TEMPAT,TANGGAL LAHIR                      :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| JENIS KELAMIN                                      :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| ALAMAT                                                 :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| SEMESTER                                             :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Aplikasi KRS Berbasis Tkinter | ©2023 Farhan Saefulah',font="Poppins 10",fg="White",bg="#001C30").grid(row=7, column=1,
            sticky=W, padx=5, pady=5)
        # Textbox
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Nomor Induk Mahasiswa':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Nomor Induk Mahasiswa')
        self.txtNim_mahasiswa = Entry(mainFrame,width = 45,font="Poppins 9 bold") 
        self.txtNim_mahasiswa.grid(row=1, column=1, padx=5, pady=5)
        self.txtNim_mahasiswa.bind("<Return>",self.onCari) # menambahkan event Enter key
        self.txtNim_mahasiswa.insert(0, 'Isi Dengan Nomor Induk Mahasiswa')
        self.txtNim_mahasiswa.bind('<FocusIn>', on_enter)
        self.txtNim_mahasiswa.bind('<FocusOut>', on_leave)
        # Textbox
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Nama':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Nama')
        self.txtNama_mahasiswa = Entry(mainFrame,width = 45,font="Poppins 9 bold") 
        self.txtNama_mahasiswa.grid(row=2, column=1, padx=5, pady=5)
        self.txtNama_mahasiswa.insert(0, 'Isi Dengan Nama')
        self.txtNama_mahasiswa.bind('<FocusIn>', on_enter)
        self.txtNama_mahasiswa.bind('<FocusOut>', on_leave)
        # Textbox
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Tanggal Lahir':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Tanggal Lahir')

        self.txtTempat_tanggallahir_mahasiwa = Entry(mainFrame, width=45, font="Poppins 9 bold")
        self.txtTempat_tanggallahir_mahasiwa.grid(row=3, column=1, padx=5, pady=5)
        self.txtTempat_tanggallahir_mahasiwa.insert(0, 'Isi Dengan Tanggal Lahir')
        self.txtTempat_tanggallahir_mahasiwa.bind('<FocusIn>', on_enter)
        self.txtTempat_tanggallahir_mahasiwa.bind('<FocusOut>', on_leave)

        # Combo Box
        self.txtJenis_kelamin = StringVar()
        Cbo_jenis_kelamin = ttk.Combobox(mainFrame, width = 43, textvariable = self.txtJenis_kelamin,font="Poppins 9 bold") 
        Cbo_jenis_kelamin.grid(row=4, column=1, padx=5, pady=5)
        # Adding jenis_kelamin combobox drop down list
        Cbo_jenis_kelamin['values'] = ('L','P')
        Cbo_jenis_kelamin.current()
        # Textbox
        # self.txtAlamat_mahasiswa = Entry(mainFrame,width = 45,font="Poppins 9 bold") 
        # self.txtAlamat_mahasiswa.grid(row=5, column=1, padx=5, pady=5)
       # Combo Box
        self.txtAlamat_mahasiswa = StringVar()
        Cbo_alamat_mahasiswa = ttk.Combobox(mainFrame, width = 43, textvariable = self.txtAlamat_mahasiswa,font="Poppins 9 bold") 
        Cbo_alamat_mahasiswa.grid(row=5, column=1, padx=5, pady=5)
        # Adding alamat_mahasiswa combobox drop down list
        Cbo_alamat_mahasiswa['values'] = ('Aceh','Sumatera Utara','Sumatera Barat','Riau','Kepulauan Riau','Jambi','Sumatera Selatan','Bangka Belitung','Bengkulu','Lampung','DKI Jakarta','Banten','Jawa Barat','Jawa Tengah','DI Yogyakarta','Jawa Timur','Bali','Nusa Tenggara Barat','Nusa Tenggara Timur','Kalimantan Barat','Kalimantan Tengah','Kalimantan Selatan','Kalimantan Timur','Kalimantan Utara','Sulawesi Utara','Sulawesi Tengah','Sulawesi Selatan','Sulawesi Tenggara','Gorontalo','Sulawesi Barat','Maluku','Maluku Utara','Papua Barat','Papua')
        Cbo_alamat_mahasiswa.current()
        # Combo Box
        self.txtSemester = StringVar()
        Cbo_semester = ttk.Combobox(mainFrame, width = 43, textvariable = self.txtSemester,font="Poppins 9 bold") 
        Cbo_semester.grid(row=6, column=1, padx=5, pady=5)
        # Adding semester combobox drop down list
        Cbo_semester['values'] = ('1','2','3','4','5','6','7','8','9')
        Cbo_semester.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10,border="6")
        self.btnSimpan.grid(row=1, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10,border="6")
        self.btnClear.grid(row=2, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10,border="6")
        self.btnHapus.grid(row=3, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_mahasiswa','nim_mahasiswa','nama_mahasiswa','tempat_tanggallahir_mahasiwa','jenis_kelamin','alamat_mahasiswa','semester')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_mahasiswa', text='ID MAHASISWA')
        self.tree.column('id_mahasiswa', width="120")
        self.tree.heading('nim_mahasiswa', text='NIM MAHASISWA')
        self.tree.column('nim_mahasiswa', width="120")
        self.tree.heading('nama_mahasiswa', text='NAMA MAHASISWA')
        self.tree.column('nama_mahasiswa', width="150")
        self.tree.heading('tempat_tanggallahir_mahasiwa', text='TEMPAT,TANGGAL LAHIR MAHASISWA')
        self.tree.column('tempat_tanggallahir_mahasiwa', width="240")
        self.tree.heading('jenis_kelamin', text='JENIS KELAMIN')
        self.tree.column('jenis_kelamin', width="100")
        self.tree.heading('alamat_mahasiswa', text='ALAMAT')
        self.tree.column('alamat_mahasiswa', width="100")
        self.tree.heading('semester', text='SEMESTER')
        self.tree.column('semester', width="100")
        # set tree position
        self.tree.place(x=0, y=350)

        
    def onClear(self, event=None):
        self.txtNim_mahasiswa.delete(0,END)
        self.txtNim_mahasiswa.insert(END,"")
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,"")
        self.txtTempat_tanggallahir_mahasiwa.delete(0,END)
        self.txtTempat_tanggallahir_mahasiwa.insert(END,"")
        self.txtJenis_kelamin.set("")
        self.txtAlamat_mahasiswa.set("")
        self.txtSemester.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data mahasiswa
        obj = Mahasiswa()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_mahasiswa"],d["nim_mahasiswa"],d["nama_mahasiswa"],d["tempat_tanggallahir_mahasiwa"],d["jenis_kelamin"],d["alamat_mahasiswa"],d["semester"]))
    def onCari(self, event=None):
        nim_mahasiswa = self.txtNim_mahasiswa.get()
        obj = Mahasiswa()
        a = obj.get_by_nim_mahasiswa(nim_mahasiswa)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nim_mahasiswa = self.txtNim_mahasiswa.get()
        obj = Mahasiswa()
        res = obj.get_by_nim_mahasiswa(nim_mahasiswa)
        self.txtNim_mahasiswa.delete(0,END)
        self.txtNim_mahasiswa.insert(END,obj.nim_mahasiswa)
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,obj.nama_mahasiswa)
        self.txtTempat_tanggallahir_mahasiwa.delete(0,END)
        self.txtTempat_tanggallahir_mahasiwa.insert(END,obj.tempat_tanggallahir_mahasiwa)
        self.txtJenis_kelamin.set(obj.jenis_kelamin)
        self.txtAlamat_mahasiswa.set(obj.alamat_mahasiswa)
        self.txtSemester.set(obj.semester)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nim_mahasiswa = self.txtNim_mahasiswa.get()
        nama_mahasiswa = self.txtNama_mahasiswa.get()
        tempat_tanggallahir_mahasiwa = self.txtTempat_tanggallahir_mahasiwa.get()
        jenis_kelamin = self.txtJenis_kelamin.get()
        alamat_mahasiswa = self.txtAlamat_mahasiswa.get()
        semester = self.txtSemester.get()
        # create new Object
        obj = Mahasiswa()
        obj.nim_mahasiswa = nim_mahasiswa
        obj.nama_mahasiswa = nama_mahasiswa
        obj.tempat_tanggallahir_mahasiwa = tempat_tanggallahir_mahasiwa
        obj.jenis_kelamin = jenis_kelamin
        obj.alamat_mahasiswa = alamat_mahasiswa
        obj.semester = semester
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nim_mahasiswa(nim_mahasiswa)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nim_mahasiswa = self.txtNim_mahasiswa.get()
        obj = Mahasiswa()
        obj.nim_mahasiswa = nim_mahasiswa
        if(self.ditemukan==True):
            res = obj.delete_by_nim_mahasiswa(nim_mahasiswa)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmMahasiswa(root2, "Aplikasi Data Mahasiswa")
    root2.mainloop()