import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *




class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("670x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()


        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#7986CB")
        Label(mainFrame, text='KODEPINJAM:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGLPINJAM:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TGL HRS KEMBALI:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODE BUKU:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=0, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NIAP:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=1, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NIPP:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Data Peminjaman',bg="white",font =('Open Sans',15,'bold'),fg="#7986CB").grid(row=5, column=4,
            sticky=W, padx=5, pady=5)

        # Textbox
        self.txtKodepinjam = Entry(mainFrame) 
        self.txtKodepinjam.grid(row=0, column=1, padx=5, pady=5)
        self.txtKodepinjam.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtTglpinjam = Entry(mainFrame) 
        self.txtTglpinjam.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTglhrskembali = Entry(mainFrame) 
        self.txtTglhrskembali.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=0, column=3, padx=5, pady=5)
        # Textbox
        self.txtNiap = Entry(mainFrame) 
        self.txtNiap.grid(row=1, column=3, padx=5, pady=5)
        # Textbox
        self.txtNipp = Entry(mainFrame) 
        self.txtNipp.grid(row=2, column=3, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10,bg="#2196F3",font =('Open Sans',9,'bold'))
        self.btnSimpan.grid(row=0, column=4, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10,bg="#2196F3",font =('Open Sans',9,'bold'))
        self.btnClear.grid(row=1, column=4, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10,bg="#C62828",font =('Open Sans',9,'bold'),fg="white")
        self.btnHapus.grid(row=2, column=4, padx=5, pady=5)
        # define columns
        columns = ('id_pinjam','kodepinjam','tglpinjam','tglhrskembali','kodebuku','niap','nipp')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_pinjam', text='ID_PINJAM')
        self.tree.column('id_pinjam', width="80")
        self.tree.heading('kodepinjam', text='KODEPINJAM')
        self.tree.column('kodepinjam', width="80")
        self.tree.heading('tglpinjam', text='TGLPINJAM')
        self.tree.column('tglpinjam', width="150")
        self.tree.heading('tglhrskembali', text='TGLHRSKEMBALI')
        self.tree.column('tglhrskembali', width="150")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="80")
        self.tree.heading('niap', text='NIAP')
        self.tree.column('niap', width="50")
        self.tree.heading('nipp', text='NIPP')
        self.tree.column('nipp', width="50")
        # set tree position
        self.tree.place(x=0, y=140)
        
    def onClear(self, event=None):
        self.txtKodepinjam.delete(0,END)
        self.txtKodepinjam.insert(END,"")
        self.txtTglpinjam.delete(0,END)
        self.txtTglpinjam.insert(END,"")
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,"")
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtNiap.delete(0,END)
        self.txtNiap.insert(END,"")
        self.txtNipp.delete(0,END)
        self.txtNipp.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_pinjam"],d["kodepinjam"],d["tglpinjam"],d["tglhrskembali"],d["kodebuku"],d["niap"],d["nipp"]))
    def onCari(self, event=None):
        kodepinjam = self.txtKodepinjam.get()
        obj = Peminjaman()
        a = obj.get_by_kodepinjam(kodepinjam)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodepinjam = self.txtKodepinjam.get()
        obj = Peminjaman()
        res = obj.get_by_kodepinjam(kodepinjam)
        self.txtKodepinjam.delete(0,END)
        self.txtKodepinjam.insert(END,obj.kodepinjam)
        self.txtTglpinjam.delete(0,END)
        self.txtTglpinjam.insert(END,obj.tglpinjam)
        self.txtTglhrskembali.delete(0,END)
        self.txtTglhrskembali.insert(END,obj.tglhrskembali)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtNiap.delete(0,END)
        self.txtNiap.insert(END,obj.niap)
        self.txtNipp.delete(0,END)
        self.txtNipp.insert(END,obj.nipp)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodepinjam = self.txtKodepinjam.get()
        tglpinjam = self.txtTglpinjam.get()
        tglhrskembali = self.txtTglhrskembali.get()
        kodebuku = self.txtKodebuku.get()
        niap = self.txtNiap.get()
        nipp = self.txtNipp.get()
        # create new Object
        obj = Peminjaman()
        obj.kodepinjam = kodepinjam
        obj.tglpinjam = tglpinjam
        obj.tglhrskembali = tglhrskembali
        obj.kodebuku = kodebuku
        obj.niap = niap
        obj.nipp = nipp
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodepinjam(kodepinjam)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodepinjam = self.txtKodepinjam.get()
        obj = Peminjaman()
        obj.kodepinjam = kodepinjam
        if(self.ditemukan==True):
            res = obj.delete_by_kodepinjam(kodepinjam)
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
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()