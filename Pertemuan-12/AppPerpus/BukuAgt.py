import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class BukuAgt:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("800x300")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES,)
        mainFrame.configure(bg="#7986CB")

        Label(mainFrame, text='Data Buku Stok Buku',bg="white",font =('Open Sans',15,'bold'),fg="#7986CB").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)

        # define columns
        columns = ('id','kodebuku','judul','penulis','penerbit','tahunpenerbit','stok')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('kodebuku', text='KODEBUKU')
        self.tree.column('kodebuku', width="80")
        self.tree.heading('judul', text='JUDUL')
        self.tree.column('judul', width="200")
        self.tree.heading('penulis', text='PENULIS')
        self.tree.column('penulis', width="170")
        self.tree.heading('penerbit', text='PENERBIT')
        self.tree.column('penerbit', width="150")
        self.tree.heading('tahunpenerbit', text='TAHUNPENERBIT')
        self.tree.column('tahunpenerbit', width="100")
        self.tree.heading('stok', text='STOK')
        self.tree.column('stok', width="40")
        # set tree position
        self.tree.place(x=0, y=40)
        
    def onClear(self, event=None):
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahunpenerbit.delete(0,END)
        self.txtTahunpenerbit.insert(END,"")
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["kodebuku"],d["judul"],d["penulis"],d["penerbit"],d["tahunpenerbit"],d["stok"]))
    def onCari(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        a = obj.get_by_kodebuku(kodebuku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        res = obj.get_by_kodebuku(kodebuku)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.kodebuku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.judul)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.penulis)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.penerbit)
        self.txtTahunpenerbit.delete(0,END)
        self.txtTahunpenerbit.insert(END,obj.tahunpenerbit)
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,obj.stok)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kodebuku = self.txtKodebuku.get()
        judul = self.txtJudul.get()
        penulis = self.txtPenulis.get()
        penerbit = self.txtPenerbit.get()
        tahunpenerbit = self.txtTahunpenerbit.get()
        stok = self.txtStok.get()
        # create new Object
        obj = Buku()
        obj.kodebuku = kodebuku
        obj.judul = judul
        obj.penulis = penulis
        obj.penerbit = penerbit
        obj.tahunpenerbit = tahunpenerbit
        obj.stok = stok
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kodebuku(kodebuku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kodebuku = self.txtKodebuku.get()
        obj = Buku()
        obj.kodebuku = kodebuku
        if(self.ditemukan==True):
            res = obj.delete_by_kodebuku(kodebuku)
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
    aplikasi = BukuAgt(root2, "Aplikasi Data Buku")
    root2.mainloop()