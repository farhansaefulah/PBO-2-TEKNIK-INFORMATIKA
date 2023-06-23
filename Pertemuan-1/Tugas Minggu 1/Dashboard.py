import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmAnggota import *
from FrmBuku import *
from FrmPeminjaman import *
from FrmPengembalian import *
from FrmPetugas import *
from tkinter import *

# Untuk login menu petugas > username : admin | password : 123
# Untuk login menu anggota > username : anggota | password : 123
# Link server http://f0832673.xsph.ru

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
            label='Data Anggota', command= lambda: self.new_window("Data Anggota", FrmAnggota)
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
            label='Data Buku', command= lambda: self.new_window("Data Buku", Buku)
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
            label='Data Buku', command= lambda: self.new_window("Menu Buku", FrmBuku)
        )
        
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="File", menu=file_menu
        )
        
        menubar.add_cascade(
            label="Menu Buku", menu=mahasiswa_menu
        )
       
        
    def show_login(self):
        self.my_w_child=tk.Toplevel(root)
        self.my_w_child.geometry("250x200") 
                # pasang Label
        Label(self.my_w_child, text='Username:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        
        Label(self.my_w_child, text="Password:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtUsername = Entry(self.my_w_child) 
        self.txtUsername.grid(row=0, column=1, padx=5, pady=5)
        
        self.txtPassword = Entry(self.my_w_child) 
        self.txtPassword.grid(row=1, column=1, padx=5, pady=5)  
        self.txtPassword.config(show='*')
                
        # Pasang Button
        self.btnLogin = tk.Button(self.my_w_child, text='Login',
            command=self.onLogin)
        self.btnLogin.grid(row=2, column=1, padx=5, pady=5)
        

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
            elif(msg=="mahasiswa" or msg=="anggota"):
                self.menuMahasiswa()
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
            
        else:
            messagebox.showinfo("showinfo", "Login Not Valid") 
        
    def onLogout(self):
        self.aturKomponen()
                    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = tk.Tk()
    my_str = tk.StringVar()
    aplikasi = Dashboard(root, "Dashboard Aplikasi Perpustakaan")
    root.mainloop() 