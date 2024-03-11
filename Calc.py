import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        self.title("SIP Calculator")
        self.geometry('600x600')

        self.SIPamt = ctk.CTkLabel(self,text = 'SIP Amount ::::  ')
        self.SIPamt.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'ew')

        self.Amt = ctk.CTkEntry(self,placeholder_text = '2000')
        self.Amt.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'ew')


if __name__=="__main__":
    app = App()
    app.mainloop()