import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

tenure = 0
amt = 0


class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title("SIP Calculator")
        self.geometry('600x600')

        self.SIPamt = ctk.CTkLabel(self,text = 'SIP Amount ::::  ')
        self.SIPamt.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'ew')

        self.Amt = ctk.CTkEntry(self,placeholder_text = '2000')
        self.Amt.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'ew')
        

        self.Tenure = ctk.CTkLabel(self, text = "Tenure (in years) ::::  ")
        self.Tenure.grid(row = 1, column = 0, padx = 20, pady = 20,sticky = 'ew')

        self.ten = ctk.CTkComboBox(self,values = ['5','10','15','20','25','30','35'])
        self.ten.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = 'ew')

if __name__=="__main__":
    app = App()
    app.mainloop()