
import tkinter as tk
pencere =tk.Tk()
pencere.geometry("600x300")


başlık=tk.Label(pencere,text="to-do list")
başlık.pack()
""" yapılacakları yazılacak yer"""
kullanıcı=tk.Entry(pencere, width=30 )
kullanıcı.pack()
""" buttonlar """
dugmea=tk.Button(pencere,text="ekle")
dugmea.pack()

dugmeb=tk.Button(pencere,text="görevi tamamala" )
dugmeb.pack()

dugmec=tk.Button(pencere,text="sil")
dugmec.pack()

pencere.mainloop()

