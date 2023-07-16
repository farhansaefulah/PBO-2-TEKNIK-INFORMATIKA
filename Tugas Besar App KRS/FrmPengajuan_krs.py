import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengajuan_krs import *
class FrmPengajuan_krs:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1200x670")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#001C30")
        Label(mainFrame, text='💾PENGISIAN PENGAJUAN KRS',font="Poppins 16 bold",fg="White",bg="#001C30").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| KODE PENGAJUAN                                             :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| NIM MAHASISWA                                               :',fg="White",bg="#001C30",font="Poppins 11").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| NAMA MAHASISWA                                           :',fg="White",bg="#001C30",font="Poppins 11 ").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| SEMESTER                                                            :',fg="White",bg="#001C30",font="Poppins 11").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| MATA KULIAH (NAMA DOSEN MATAKULIAH)',fg="White",bg="#001C30",font="Poppins 11").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='  (SKS) SMT                                                           :',fg="White",bg="#001C30",font="Poppins 11").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| DOSEN WALI                                                       :',fg="White",bg="#001C30",font="Poppins 11").grid(row=7, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='| STATUS KRS                                                        :',fg="White",bg="#001C30",font="Poppins 11").grid(row=8, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Aplikasi KRS Berbasis Tkinter | ©2023 Farhan Saefulah',font="Poppins 10",fg="White",bg="#001C30").grid(row=9, column=1,
            sticky=W, padx=5, pady=5)
        # Textbox
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Kode Pengajuan KRS':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Kode Pengajuan KRS')

        self.txtKode_pengajuan = Entry(mainFrame,width = 45,font="Poppins 9 ") 
        self.txtKode_pengajuan.grid(row=1, column=1, padx=5, pady=5)
        self.txtKode_pengajuan.bind("<Return>",self.onCari) # menambahkan event Enter key
        self.txtKode_pengajuan.insert(0, 'Isi Dengan Kode Pengajuan KRS')
        self.txtKode_pengajuan.bind('<FocusIn>', on_enter)
        self.txtKode_pengajuan.bind('<FocusOut>', on_leave)
        # Textbox
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Nomer Induk Mahasiswa':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Nomer Induk Mahasiswa')
        self.txtNim_mahasiswa = Entry(mainFrame,width = 45,font="Poppins 9 ") 
        self.txtNim_mahasiswa.grid(row=2, column=1, padx=5, pady=5)
        self.txtNim_mahasiswa.insert(0, 'Isi Dengan Nomer Induk Mahasiswa')
        self.txtNim_mahasiswa.bind('<FocusIn>', on_enter)
        self.txtNim_mahasiswa.bind('<FocusOut>', on_leave)
        # Textbox
        label_style = ('Helvetica', 11, 'normal')
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Isi Dengan Nama Lengkap':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Isi Dengan Nama Lengkap')
        self.txtNama_mahasiswa = Entry(mainFrame,width = 45,font="Poppins 9") 
        self.txtNama_mahasiswa.grid(row=3, column=1, padx=5, pady=5)
        self.txtNama_mahasiswa.insert(0, 'Isi Dengan Nama Lengkap')
        self.txtNama_mahasiswa.bind('<FocusIn>', on_enter)
        self.txtNama_mahasiswa.bind('<FocusOut>', on_leave)
        # Combo Box
        self.txtSemester = StringVar()
        Cbo_semester = ttk.Combobox(mainFrame, width = 42, textvariable = self.txtSemester,font="Poppins 10 ") 
        Cbo_semester.grid(row=4, column=1, padx=5, pady=5)
        # Adding semester combobox drop down list
        Cbo_semester['values'] = ('1','2','3','4','5','6','7','8','9')
        Cbo_semester.current()
        # Combo Box
        self.txtMata_kuliah_namadosen_matakuliah = StringVar()
        Cbo_mata_kuliah_namadosen_matakuliah = ttk.Combobox(mainFrame, width = 42, textvariable = self.txtMata_kuliah_namadosen_matakuliah,font="Poppins 10") 
        Cbo_mata_kuliah_namadosen_matakuliah.grid(row=6, column=1, padx=5, pady=5)
        # Adding mata_kuliah_namadosen_matakuliah combobox drop down list
        Cbo_mata_kuliah_namadosen_matakuliah['values'] = ('Agama (Khozin) (2) 1','Bahasa Inggris (Ayu) (2) 1','Logika Matematika (Rachmat) (2) 1','Al-Islam Kemuhammadiyahan (2) 2','Sistem Digital (Agust Martinus) (3) 2','Kalkulus 1 (Deni) (3) 2','Pemograman Berbasis Objek 1 (Freddy Wicaksono) (3) 3','Al-Islam Quran (Khozin) (2) 3','Pemograman Berbasis Objek 2 (Freddy Wicaksono) (3) 4','Pengembangan Web (Farhan Saefulah) (3) 4','Analisis Data (Khaerul Anwar) (2) 4','Jaringan Komputer (Imam) (2) 4','Basis Data (Supri) (3) 4', 'Matematika Distrik (Pahla) (2) 4')
        Cbo_mata_kuliah_namadosen_matakuliah.current()
        # Combo Box
        self.txtDosen_wali = StringVar()
        Cbo_dosen_wali = ttk.Combobox(mainFrame, width = 42, textvariable = self.txtDosen_wali,font="Poppins 10 ") 
        Cbo_dosen_wali.grid(row=7, column=1, padx=5, pady=5)
        # Adding dosen_wali combobox drop down list
        Cbo_dosen_wali['values'] = ('Freddy Wicaksono','Farhan Saefulah','Agust Martinus','Imam','Sokid')
        Cbo_dosen_wali.current()
        # Combo Box
        self.txtStatus_krs = StringVar()
        Cbo_status_krs = ttk.Combobox(mainFrame, width = 42, textvariable = self.txtStatus_krs,font="Poppins 10 ") 
        Cbo_status_krs.grid(row=8, column=1, padx=5, pady=5)
        # Adding status_krs combobox drop down list
        Cbo_status_krs['values'] = ('BelumValidasi')
        Cbo_status_krs.current()
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10,border="6")
        self.btnSimpan.grid(row=1, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10,border="6")
        self.btnClear.grid(row=2, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10,border="6")
        self.btnHapus.grid(row=3, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_pengajuan','kode_pengajuan','nim_mahasiswa','nama_mahasiswa','semester','mata_kuliah_namadosen_matakuliah','dosen_wali','status_krs')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pengajuan', text='ID PENGAJUAN')
        self.tree.column('id_pengajuan', width="110")
        self.tree.heading('kode_pengajuan', text='KODE PENGAJUAN')
        self.tree.column('kode_pengajuan', width="110")
        self.tree.heading('nim_mahasiswa', text='NIM MAHASISWA')
        self.tree.column('nim_mahasiswa', width="130")
        self.tree.heading('nama_mahasiswa', text='NAMA MAHASISWA')
        self.tree.column('nama_mahasiswa', width="150")
        self.tree.heading('semester', text='SEMESTER')
        self.tree.column('semester', width="100")
        self.tree.heading('mata_kuliah_namadosen_matakuliah', text='MATA KULIAH (NAMA DOSEN_MATA KULIAH) (SKS) SMT')
        self.tree.column('mata_kuliah_namadosen_matakuliah', width="350")
        self.tree.heading('dosen_wali', text='DOSEN WALI')
        self.tree.column('dosen_wali', width="130")
        self.tree.heading('status_krs', text='STATUS KRS')
        self.tree.column('status_krs', width="100")
        # set tree position
        self.tree.place(x=0, y=430)
        
    def onClear(self, event=None):
        self.txtKode_pengajuan.delete(0,END)
        self.txtKode_pengajuan.insert(END,"")
        self.txtNim_mahasiswa.delete(0,END)
        self.txtNim_mahasiswa.insert(END,"")
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,"")
        self.txtSemester.set("")
        self.txtMata_kuliah_namadosen_matakuliah.set("")
        self.txtDosen_wali.set("")
        self.txtStatus_krs.set("")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengajuan_krs
        obj = Pengajuan_krs()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_pengajuan"],d["kode_pengajuan"],d["nim_mahasiswa"],d["nama_mahasiswa"],d["semester"],d["mata_kuliah_namadosen_matakuliah"],d["dosen_wali"],d["status_krs"]))
    def onCari(self, event=None):
        kode_pengajuan = self.txtKode_pengajuan.get()
        obj = Pengajuan_krs()
        a = obj.get_by_kode_pengajuan(kode_pengajuan)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_pengajuan = self.txtKode_pengajuan.get()
        obj = Pengajuan_krs()
        res = obj.get_by_kode_pengajuan(kode_pengajuan)
        self.txtKode_pengajuan.delete(0,END)
        self.txtKode_pengajuan.insert(END,obj.kode_pengajuan)
        self.txtNim_mahasiswa.delete(0,END)
        self.txtNim_mahasiswa.insert(END,obj.nim_mahasiswa)
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,obj.nama_mahasiswa)
        self.txtSemester.set(obj.semester)
        self.txtMata_kuliah_namadosen_matakuliah.set(obj.mata_kuliah_namadosen_matakuliah)
        self.txtDosen_wali.set(obj.dosen_wali)
        self.txtStatus_krs.set(obj.status_krs)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_pengajuan = self.txtKode_pengajuan.get()
        nim_mahasiswa = self.txtNim_mahasiswa.get()
        nama_mahasiswa = self.txtNama_mahasiswa.get()
        semester = self.txtSemester.get()
        mata_kuliah_namadosen_matakuliah = self.txtMata_kuliah_namadosen_matakuliah.get()
        dosen_wali = self.txtDosen_wali.get()
        status_krs = self.txtStatus_krs.get()
        # create new Object
        obj = Pengajuan_krs()
        obj.kode_pengajuan = kode_pengajuan
        obj.nim_mahasiswa = nim_mahasiswa
        obj.nama_mahasiswa = nama_mahasiswa
        obj.semester = semester
        obj.mata_kuliah_namadosen_matakuliah = mata_kuliah_namadosen_matakuliah
        obj.dosen_wali = dosen_wali
        obj.status_krs = status_krs
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_pengajuan(kode_pengajuan)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_pengajuan = self.txtKode_pengajuan.get()
        obj = Pengajuan_krs()
        obj.kode_pengajuan = kode_pengajuan
        if(self.ditemukan==True):
            res = obj.delete_by_kode_pengajuan(kode_pengajuan)
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
    aplikasi = FrmPengajuan_krs(root2, "Aplikasi Data Pengajuan_krs")
    root2.mainloop()