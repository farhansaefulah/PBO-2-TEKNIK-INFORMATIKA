import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("700x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#7986CB")
        Label(mainFrame, text='NIAP:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NOTELP:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Data Anggota',bg="white",font =('Open Sans',15,'bold'),fg="#7986CB").grid(row=3, column=4,
            sticky=W, padx=5, pady=5)
        

        # Textbox
        self.txtNiap = Entry(mainFrame,width = 30) 
        self.txtNiap.grid(row=0, column=1, padx=5, pady=5)
        self.txtNiap.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame,width = 30) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk = StringVar()
        Cbo_jk = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtJk) 
        Cbo_jk.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk combobox drop down list
        Cbo_jk['values'] = ('L','P')
        Cbo_jk.current()
        # Combo Box
        self.txtProdi = StringVar()
        Cbo_prodi = ttk.Combobox(mainFrame, width = 27, textvariable = self.txtProdi) 
        Cbo_prodi.grid(row=0, column=3, padx=5, pady=5)
        # Adding prodi combobox drop down list
        Cbo_prodi['values'] = ('TIF','IND','PET')
        Cbo_prodi.current()
        # Textbox
        self.txtNotelp = Entry(mainFrame,width = 30) 
        self.txtNotelp.grid(row=1, column=3, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame,width = 30) 
        self.txtAlamat.grid(row=2, column=3, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan',bg="#2196F3",font =('Open Sans',9,'bold'), command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=4, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear',bg="#2196F3",font =('Open Sans',9,'bold'), command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=4, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus',bg="#C62828",font =('Open Sans',9,'bold'),fg="white", command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=4, padx=5, pady=5)
        # define columns
        columns = ('id','niap','nama','jk','prodi','notelp','alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('niap', text='NIAP')
        self.tree.column('niap', width="40")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="150")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="40")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="80")
        self.tree.heading('notelp', text='NOTELP')
        self.tree.column('notelp', width="60")
        self.tree.heading('alamat', text='ALAMAT')
        self.tree.column('alamat', width="280")
        # set tree position
        self.tree.place(x=0, y=140)
        
    def onClear(self, event=None):
        self.txtNiap.delete(0,END)
        self.txtNiap.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk.set("")
        self.txtProdi.set("")
        self.txtNotelp.delete(0,END)
        self.txtNotelp.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["niap"],d["nama"],d["jk"],d["prodi"],d["notelp"],d["alamat"]))
    def onCari(self, event=None):
        niap = self.txtNiap.get()
        obj = Anggota()
        a = obj.get_by_niap(niap)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        niap = self.txtNiap.get()
        obj = Anggota()
        res = obj.get_by_niap(niap)
        self.txtNiap.delete(0,END)
        self.txtNiap.insert(END,obj.niap)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk.set(obj.jk)
        self.txtProdi.set(obj.prodi)
        self.txtNotelp.delete(0,END)
        self.txtNotelp.insert(END,obj.notelp)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        niap = self.txtNiap.get()
        nama = self.txtNama.get()
        jk = self.txtJk.get()
        prodi = self.txtProdi.get()
        notelp = self.txtNotelp.get()
        alamat = self.txtAlamat.get()
        # create new Object
        obj = Anggota()
        obj.niap = niap
        obj.nama = nama
        obj.jk = jk
        obj.prodi = prodi
        obj.notelp = notelp
        obj.alamat = alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_niap(niap)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        niap = self.txtNiap.get()
        obj = Anggota()
        obj.niap = niap
        if(self.ditemukan==True):
            res = obj.delete_by_niap(niap)
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()
