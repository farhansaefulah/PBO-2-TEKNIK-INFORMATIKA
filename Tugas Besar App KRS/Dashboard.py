import tkinter as tk
from tkinter import Tk, Canvas
from tkinter import colorchooser
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox, Menu
from Users import *
from FrmMahasiswa import *
from FrmPengajuan_krs import *
from FrmValidasi_krs import *
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
        mainFrame.configure(bg="#001C30")
        
        Label(mainFrame, text='.',font="Poppins 7",fg="#001C30",bg="#001C30").grid(row=0, column=1,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='.',font="Poppins 7",fg="#001C30",bg="#001C30").grid(row=1, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='.',font="Poppins 7",fg="#001C30",bg="#001C30").grid(row=2, column=3,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='.',font="Poppins 100",fg="#001C30",bg="#001C30").grid(row=3, column=3,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='🌫',font="Calibri 200",fg="White",bg="#001C30").grid(row=3, column=5,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='💻',font="Poppins 200",fg="White",bg="#001C30").grid(row=3, column=6,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='🌫',font="Calibri 200",fg="White",bg="#001C30").grid(row=3, column=7,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Aplikasi KRS Berbasis Tkinter | ©2023 Farhan Saefulah',font="Poppins 10",fg="White",bg="#001C30").grid(row=5, column=6,
            sticky=W, padx=10, pady=5)




        mainmenu = Menu(self.parent)
        self.parent.config(menu=mainmenu)
        file_menu1 = Menu(mainmenu)
        
        # Menu Awal
        file_menu1.add_command(
            label='Login Mahasiswa', command=self.show_login
        )
        file_menu1.add_command(
            label='Login Dosen', command=self.show_login_dosen
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
            label='Menu Pengajuan KRS', command= lambda: self.new_window("Menu Pengajuan KRS",)
        )



        

        
        # Tampilkan menu ke layar

        
        menubar.add_cascade(
            label="Menu Aplikasi KRS", menu=admin_menu
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
            label='Exit Aplikasi', command=root.destroy
        )
        keluar_menu.add_command(
            label='Yakin Logout?', command=self.onLogout
        )


      
        # Menu Admin

        dosen_menu.add_command(
            label='Menu Validasi KRS', command= lambda: self.new_window("Menu Validasi KRS", FrmValidasi_krs)
        )
        

        
        # Tampilkan menu ke layar

        
        menubar.add_cascade(
            label="Menu Aplikasi KRS", menu=dosen_menu
        )
        menubar.add_cascade(
            label="Logout", menu=keluar_menu
        )
        
    def menuMahasiswa(self):
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)
       
        # create a menu
        mahasiswa_menu = Menu(menubar)
        keluar_menu = Menu(menubar)



        # Menu File

        keluar_menu.add_command(
            label='Exit Aplikasi', command=root.destroy
        )
        keluar_menu.add_command(
            label='Yakin Logout?', command=self.onLogout
        )


      
        # Menu Admin
        mahasiswa_menu.add_command(
            label='Menu Biodata Mahasiswa', command= lambda: self.new_window("Menu Biodata Mahasiswa", FrmMahasiswa)
        )
        mahasiswa_menu.add_command(
            label='Menu Pengajuan KRS', command= lambda: self.new_window("Menu Pengajuan KRS", FrmPengajuan_krs)
        )
        
        # Tampilkan menu ke layar
        menubar.add_cascade(
            label="Menu Aplikasi KRS", menu=mahasiswa_menu
        )
        menubar.add_cascade(
            label="Logout", menu=keluar_menu
        )
       
        
    def show_login(self):
        self.my_w_child = tk.Toplevel(root)
        self.my_w_child.title("Login Mahasiswa Aplikasi KRS")
        self.my_w_child.geometry("400x320")
        self.my_w_child.configure(bg="#1E2630")

        # Set styles
        title_style = ('Helvetica', 14, 'bold')
        label_style = ('Helvetica', 11, 'normal')
        button_style = ('Helvetica', 11, 'bold')

        # Add labels
        tk.Label(self.my_w_child, text='                 🎓 Login Mahasiswa', bg="#1E2630", font=title_style, fg="#FFFFFF").grid(row=0, column=1, sticky='w', padx=20, pady=5)
        tk.Label(self.my_w_child, text="Username", bg="#1E2630", font=label_style, fg="#FFFFFF").grid(row=1, column=1, sticky='w', padx=20, pady=10)
        tk.Label(self.my_w_child, text="Password:", bg="#1E2630", font=label_style, fg="#FFFFFF").grid(row=3, column=1, sticky='w', padx=20, pady=10)

        # Add textboxes
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Masukan Username':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Masukan Username')

        self.txtUsername = tk.Entry(self.my_w_child, width="25", font=label_style)
        self.txtUsername.grid(row=2, column=1, padx=20, pady=10, sticky='w')
        self.txtUsername.insert(0, 'Masukan Username')
        self.txtUsername.bind('<FocusIn>', on_enter)
        self.txtUsername.bind('<FocusOut>', on_leave)


        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Masukan Password':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Masukan Password')

        self.txtPassword = tk.Entry(self.my_w_child, width="25", font=label_style)
        self.txtPassword.grid(row=4, column=1, padx=20, pady=10, sticky='w')
        self.txtPassword.insert(0, 'Masukan Password')
        self.txtPassword.bind('<FocusIn>', on_enter)
        self.txtPassword.bind('<FocusOut>', on_leave)


        # Add remember checkbox
        self.remember_var = tk.BooleanVar()
        tk.Checkbutton(self.my_w_child, text="Remember", bg="#1E2630", font=label_style, fg="#FFFFFF", variable=self.remember_var).grid(row=5, column=1, sticky='w', padx=20, pady=10)

        # Add show/hide password button
        self.btnShowPassword = tk.Button(self.my_w_child, text='Show/Hide', width=10, font=button_style, bg="#405F7B", fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.toggle_password_visibility)
        self.btnShowPassword.place(x=130, y=200)

        # Add login button
        self.btnLogin = tk.Button(self.my_w_child, text='Login', width=10, bg="#405F7B", font=button_style, fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.onLogin)
        self.btnLogin.grid(row=6, column=1, columnspan=2, padx=20, pady=20, sticky='w')
        self.btnCancel = tk.Button(self.my_w_child, text='Cancel', width=10, bg="red", font=button_style, fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.my_w_child.quit)
        self.btnCancel.place(x=260, y=275)




    def toggle_password_visibility(self):
        if self.txtPassword['show'] == '':
            self.txtPassword.config(show='*')
        else:
            self.txtPassword.config(show='')

    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B = []
        A.username = u
        A.passwd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        if status == "success":
            self.my_w_child.destroy()
            if msg == "admin":
                self.menuAdmin()
            elif msg == "dosen":
                self.menuDosen()
            elif msg == "mahasiswa":
                self.menuMahasiswa()
            else:
                messagebox.showinfo("showinfo", "User Tidak Dikenal")
        else:
            messagebox.showinfo("showinfo", "Login Not Valid silahkan cek Username & Password")
    def show_login_dosen(self):
        self.my_w_child = tk.Toplevel(root)
        self.my_w_child.title("Login Dosen Aplikasi KRS")
        self.my_w_child.geometry("400x320")
        self.my_w_child.configure(bg="#1E2630")

        # Set styles
        title_style = ('Helvetica', 14, 'bold')
        label_style = ('Helvetica', 11, 'normal')
        button_style = ('Helvetica', 11, 'bold')

        # Add labels
        tk.Label(self.my_w_child, text='                      👨‍🎓 Login Dosen', bg="#1E2630", font=title_style, fg="#FFFFFF").grid(row=0, column=1, sticky='w', padx=20, pady=5)
        tk.Label(self.my_w_child, text="Username", bg="#1E2630", font=label_style, fg="#FFFFFF").grid(row=1, column=1, sticky='w', padx=20, pady=10)
        tk.Label(self.my_w_child, text="Password:", bg="#1E2630", font=label_style, fg="#FFFFFF").grid(row=3, column=1, sticky='w', padx=20, pady=10)

        # Add textboxes
        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Masukan Username':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Masukan Username')

        self.txtUsername = tk.Entry(self.my_w_child, width="25", font=label_style)
        self.txtUsername.grid(row=2, column=1, padx=20, pady=10, sticky='w')
        self.txtUsername.insert(0, 'Masukan Username')
        self.txtUsername.bind('<FocusIn>', on_enter)
        self.txtUsername.bind('<FocusOut>', on_leave)


        def on_enter(event):
            entry = event.widget
            if entry.get() == 'Masukan Password':
                entry.delete(0, 'end')

        def on_leave(event):
            entry = event.widget
            if entry.get() == '':
                entry.insert(0, 'Masukan Password')

        self.txtPassword = tk.Entry(self.my_w_child, width="25", font=label_style)
        self.txtPassword.grid(row=4, column=1, padx=20, pady=10, sticky='w')
        self.txtPassword.insert(0, 'Masukan Password')
        self.txtPassword.bind('<FocusIn>', on_enter)
        self.txtPassword.bind('<FocusOut>', on_leave)


        # Add remember checkbox
        self.remember_var = tk.BooleanVar()
        tk.Checkbutton(self.my_w_child, text="Remember", bg="#1E2630", font=label_style, fg="#FFFFFF", variable=self.remember_var).grid(row=5, column=1, sticky='w', padx=20, pady=10)

        # Add show/hide password button
        self.btnShowPassword = tk.Button(self.my_w_child, text='Show/Hide', width=10, font=button_style, bg="#405F7B", fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.toggle_password_visibility)
        self.btnShowPassword.place(x=130, y=200)

        # Add login button
        self.btnLogin = tk.Button(self.my_w_child, text='Login', width=10, bg="#405F7B", font=button_style, fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.onLogin)
        self.btnLogin.grid(row=6, column=1, columnspan=2, padx=20, pady=20, sticky='w')
        self.btnCancel = tk.Button(self.my_w_child, text='Cancel', width=10, bg="red", font=button_style, fg="#FFFFFF", bd=0, highlightthickness=0, activebackground="#405F7B", activeforeground="#FFFFFF", command=self.my_w_child.quit)
        self.btnCancel.place(x=260, y=275)



    def toggle_password_visibility(self):
        if self.txtPassword['show'] == '':
            self.txtPassword.config(show='*')
        else:
            self.txtPassword.config(show='')

    def onLogin(self, event=None):
        u = self.txtUsername.get()
        p = self.txtPassword.get()
        A = Users()
        B = []
        A.username = u
        A.passwd = p
        res = A.Login()
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        if status == "success":
            self.my_w_child.destroy()
            if msg == "admin":
                self.menuAdmin()
            elif msg == "dosen":
                self.menuDosen()
            elif msg == "mahasiswa":
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
    aplikasi = Dashboard(root, "Dashboard Aplikasi KRS")
    root.mainloop() 