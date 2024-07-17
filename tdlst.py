import tkinter as tk
pencere =tk.Tk()
pencere.geometry("900x600")

def göref_yap():
    


    """ kullanıcının yazdığı metni alır """
    kullanıc_al=kullanıcı.get()
    if kullanıc_al.strip()== "":
         return
   
    """ görev silmek """
    var=tk.BooleanVar()

    """ check ekleme """
    

    def görev_tmm():
         if var.get():
              
              checetm.config(font=("Helvetica", 10, "overstrike")) # yazıın üzerinin   çizme
         else:
              
              
              checetm.config(font=("Helvetica", 10, "normal")) # normal yazı tipi
              
              
         

    def sill():
         
         checetm.destroy()
         dugmec.destroy()
    checetm=tk.Checkbutton(pencere,text=kullanıc_al , variable=var, command=görev_tmm)
    checetm.pack()
    dugmec=tk.Button(pencere,text="sil", command=sill )
    dugmec.pack()

    
    
              

    
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

""" metin göstermek için """
mgor=tk.Label(pencere,text="")
mgor.pack(pady=30, padx=30) 


pencere.mainloop()