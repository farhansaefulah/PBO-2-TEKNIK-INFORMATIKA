import tkinter as tk
from tkinter import Tk, Canvas
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmAnggota import *
from FrmPetugas import *
from FrmPeminjaman import *
from FrmPengembalian import *
from FrmBuku import *
from BukuAgt import *
from tkinter import *



class Dashboard:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1300x650")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.my_w_child = None
        self.aturKomponen()

        
    def new_window( self, number, _class):
        new = tk.Toplevel()
        new.transient()
        new.grab_set()
        _class(new, number)



    def aturKomponen(self):
        mainFrame = tk.Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        mainFrame.configure(bg="#7986CB")




        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu)
        
        # Menu Awal
        file_menu1.add_command(
            label='Login', command=self.show_login
        )
        file_menu1.add_command(
            label='Exit', command=root.destroy
        )
        
        # Tampilkan menu ke layar
        mainmenu.add_cascade(
            label="File", menu=file_menu1
        )
        
        

    def menuAdmin(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu

        admin_menu = Menu(menubar)
        keluar_menu = Menu(menubar)

        # Menu File
       
        keluar_menu.add_command(
            label='Yakin Logout?', command=self.onLogout
        )

      
        # Menu Admin
        
        admin_menu.add_command(
            label='Data Anggota', command= lambda: self.new_window("Data Peminjaman", FrmAnggota)
        )
        admin_menu.add_command(
            label='Data Petugas', command= lambda: self.new_window("Data Petugas", FrmPetugas)
        )
        admin_menu.add_command(
            label='Data Peminjaman', command= lambda: self.new_window("Data Peminjaman", FrmPeminjaman)
        )
        admin_menu.add_command(
            label='Data Pengembalian', command= lambda: self.new_window("Data Pengembalian", FrmPengembalian)
        )
        admin_menu.add_command(
            label='Data Buku', command= lambda: self.new_window("Data Buku", FrmBuku)
        )



        

        
        # Tampilkan menu ke layar

        
        menubar.add_cascade(
            label="Menu Petugas", menu=admin_menu
        )

        menubar.add_cascade(
            label="Logout", menu=keluar_menu
        )
        
    def menuDosen(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu

        dosen_menu = Menu(menubar)
        keluar_menu = Menu(menubar)

        # Menu File
       
        keluar_menu.add_command(
            label='Yakin Logout?', command=self.onLogout
        )

      
        # Menu Admin

        dosen_menu.add_command(
            label='Data Buku', command= lambda: self.new_window("Data Buku", BukuAgt)
        )
        

        
        # Tampilkan menu ke layar

        
        menubar.add_cascade(
            label="Menu Anggota", menu=dosen_menu
        )
        menubar.add_cascade(
            label="Logout", menu=keluar_menu
        )
        
    def menuMahasiswa(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        file_menu = Menu(menubar)
        mahasiswa_menu = Menu(menubar)

        # Menu File
       
        file_menu.add_command(
            label='Logout', command=self.onLogout
        )
        file_menu.add_command(
            label='Exit', command=root.destroy
        )

      
        # Menu Admin
        mahasiswa_menu.add_command(
            label='Data Mahasiswa 1', command= lambda: self.new_window("Menu mahasiswa 1", FrmAnggota)
        )
        mahasiswa_menu.add_command(
            label='Data Mahasiswa 2', command= lambda: self.new_window("Menu mahasiswa 2", FrmPetugas)
        )
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu mahasiswa", menu=mahasiswa_menu
        )
       
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("300x150") 
        self.my_w_child.configure(bg="#7986CB")
                # pasang Label

        Label(self.my_w_child, text='Please Login',bg="#7986CB",font =('Open Sans',9,'bold'),fg="white").grid(row=1, column=2,
            sticky=W, padx=5, pady=5)


        Label(self.my_w_child, text='Username:',bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=2, column=1,
            sticky=W, padx=5, pady=5)
        
        Label(self.my_w_child, text="Password:",bg="#7986CB",font =('Open Sans',8,'bold'),fg="white").grid(row=3, column=1,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child,width="20") 
        self.txtUsername.grid(row=2, column=2, padx=5, pady=5)
        
        self.txtPassword = Entry(self.my_w_child,width="20") 
        self.txtPassword.grid(row=3, column=2, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login', bg="#0D47A1",width=10,fg="white",
            command=self.onLogin)
        self.btnLogin.grid(row=4, column=2, padx=5, pady=5)
        

    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B =[]
        A.username = u
        A.passwd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        #messagebox.showinfo("showinfo", "status:"+status+"message:"+msg) 
        if(status=="success"):
            self.my_w_child.destroy()
            if(msg=="admin"):
                self.menuAdmin()
            elif(msg=="dosen"):
                self.menuDosen()
            elif(msg=="mahasiswa"):
                self.menuMahasiswa()
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid silahkan cek Username & Password") 
        
    def onLogout(self):
        self.aturKomponen()

                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    my_str = tk.StringVar()
    gambar = PhotoImage(file="C:/xampp/htdocs/ApkPerpusApi/bgperpus.png") #Ubah Sesuai posisi Penyimpanan Anda
    w = Label(root, image=gambar).pack(side="top")
    aplikasi = Dashboard(root, "Dashboard Aplikasi")
    root.mainloop() 