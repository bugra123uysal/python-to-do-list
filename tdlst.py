
import tkinter as tk
pencere =tk.Tk()
pencere.geometry("900x600")

def göref_yap():

    """ kullanıcının yazdığı metni alır """
    kullanıc_al=kullanıcı.get()
    """girilen yeni kelimeyi  alt alta yazdirmak 
    mgor['text']+= '\n'+kullanıc_al
    """
    """ görev silmek """
    var=tk.BooleanVar()
    """ check ekleme """
    checetm=tk.Checkbutton(pencere,text=kullanıc_al , variable=var)
    checetm.pack()

    


başlık=tk.Label(pencere,text="to-do list")
başlık.pack()
""" yapılacakları yazılacak yer"""
kullanıcı=tk.Entry(pencere, width=30 )
kullanıcı.pack()
""" kullanıcının yazdığı metni alır """

""" buttonlar """
""" buttona bastığında göref_yap çalışır """
dugmea=tk.Button(pencere,text="ekle", command=göref_yap )
dugmea.pack(pady=5)

dugmeb=tk.Button(pencere,text="görevi tamamala" )
dugmeb.pack(pady=5)

dugmec=tk.Button(pencere,text="sil")
dugmec.pack(pady=5)

""" metin göstermek için """
mgor=tk.Label(pencere,text="")
mgor.pack(pady=30, padx=30) 


pencere.mainloop()


