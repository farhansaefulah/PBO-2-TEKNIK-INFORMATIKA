import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Petugas import *
class FrmPetugas:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("700x380")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#7986CB")
        Label(mainFrame, text='NIPP:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JABATAN:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO TELEPON:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Data Petugas',bg="white",font =('Open Sans',15,'bold'),fg="#7986CB").grid(row=2, column=2,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNipp = Entry(mainFrame) 
        self.txtNipp.grid(row=0, column=1, padx=5, pady=5)
        self.txtNipp.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJabatan = StringVar()
        Cbo_jabatan = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJabatan) 
        Cbo_jabatan.grid(row=2, column=1, padx=5, pady=5)
        # Adding jabatan combobox drop down list
        Cbo_jabatan['values'] = ('Kepala Perpus','Super Admin','Admin')
        Cbo_jabatan.current()
        # Textbox
        self.txtNotelp = Entry(mainFrame) 
        self.txtNotelp.grid(row=0, column=3, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=1, column=3, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10,bg="#2196F3",font =('Open Sans',9,'bold'))
        self.btnSimpan.grid(row=0, column=4, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10,bg="#2196F3",font =('Open Sans',9,'bold'))
        self.btnClear.grid(row=1, column=4, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10,bg="#C62828",font =('Open Sans',9,'bold'),fg="white")
        self.btnHapus.grid(row=2, column=4, padx=5, pady=5)
        # define columns
        columns = ('id','nipp','nama','jabatan','notelp','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="50")
        self.tree.heading('nipp', text='NIPP')
        self.tree.column('nipp', width="50")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="200")
        self.tree.heading('jabatan', text='JABATAN')
        self.tree.column('jabatan', width="100")
        self.tree.heading('notelp', text='NOTELP')
        self.tree.column('notelp', width="80")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="200")
        # set tree position
        self.tree.place(x=0, y=120)
        
    def onClear(self, event=None):
        self.txtNipp.delete(0,END)
        self.txtNipp.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJabatan.set("")
        self.txtNotelp.delete(0,END)
        self.txtNotelp.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data petugas
        obj = Petugas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["nipp"],d["nama"],d["jabatan"],d["notelp"],d["alamat"]))
    def onCari(self, event=None):
        nipp = self.txtNipp.get()
        obj = Petugas()
        a = obj.get_by_nipp(nipp)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nipp = self.txtNipp.get()
        obj = Petugas()
        res = obj.get_by_nipp(nipp)
        self.txtNipp.delete(0,END)
        self.txtNipp.insert(END,obj.nipp)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJabatan.set(obj.jabatan)
        self.txtNotelp.delete(0,END)
        self.txtNotelp.insert(END,obj.notelp)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nipp = self.txtNipp.get()
        nama = self.txtNama.get()
        jabatan = self.txtJabatan.get()
        notelp = self.txtNotelp.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Petugas()
        obj.nipp = nipp
        obj.nama = nama
        obj.jabatan = jabatan
        obj.notelp = notelp
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nipp(nipp)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nipp = self.txtNipp.get()
        obj = Petugas()
        obj.nipp = nipp
        if(self.ditemukan==True):
            res = obj.delete_by_nipp(nipp)
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
    aplikasi = FrmPetugas(root2, "Aplikasi Data Petugas")
    root2.mainloop()