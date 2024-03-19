import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class App(ctk.CTk):
    


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        # amount = 0.0
        # tenure = 0
        # per = 0
        # lumpSum = 0

#


        def Display(self,M,N):
            self.MatDisp.configure(text=str(format(M,',d')))
            self.AmtDisp.configure(text=str(format(N,',d')))


        def getAns(self,amt,te,pe) :
            P = amt
            i = float(pe/12)
            n = te*12

            M = int(P * ((pow((1+i),n)-1)/i) * (1+i))
            N = int(amt*n)
            print(M,N)
            Display(self,M,N)
            

        def pressedCalculate():
            global amount
            if self.Amt.get() != '':
                amount = int(self.Amt.get())
            elif self.ls.get() != '':
                amount = int(self.ls.get())

            global tenure
            tenure = int(self.ten.get())

            global per
            per = float(int(self.roi.get())/100)

            getAns(self,amount,tenure,per)

            
        # print(amount)
        def pressedReset():
            self.Amt.delete(0,'end')
            # self.ten.delete(0,'end')
            self.ls.delete(0,'end')
            self.roi.delete(0,'end')
            


        self.title("SIP Calculator")
        self.geometry('600x600')

        self.SIPamt = ctk.CTkLabel(self,text = 'SIP Amount ::::  ')
        self.SIPamt.grid(row = 0, column = 0, padx = 20, pady = 20, sticky = 'ew')

        self.Amt = ctk.CTkEntry(self,placeholder_text = '2000',border_color="#02b165")
        self.Amt.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = 'ew')
        

        self.Tenure = ctk.CTkLabel(self, text = "Tenure (in years) ::::  ")
        self.Tenure.grid(row = 1, column = 0, padx = 20, pady = 20,sticky = 'ew')

        self.ten = ctk.CTkComboBox(self,values = ['5','10','15','20','25','30','35'],border_color="#02b165",button_color="#02b165",dropdown_hover_color="#02b165")
        self.ten.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = 'ew')

        self.ror = ctk.CTkLabel(self, text = 'Rate of Return (%) ::::  ')
        self.ror.grid(row = 2, column = 0, padx = 20, pady = 20,sticky = 'ew')

        self.roi = ctk.CTkEntry(self, placeholder_text= '12%',border_color="#02b165")
        self.roi.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = 'ew')


        self.lumpSum = ctk.CTkLabel(self,text='Lump-sum Amount ::::  ')
        self.lumpSum.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = 'ew')

        self.ls = ctk.CTkEntry(self, placeholder_text = '1,00,000',border_color="#02b165")
        self.ls.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = 'ew')

        self.Calculate = ctk.CTkButton(self,text="Calculate",bg_color="#02b165",border_color="black", command = pressedCalculate)
        self.Calculate.grid(row = 4, column = 1, padx = 20, pady = 20 ,sticky = 'ew')

        self.Reset = ctk.CTkButton(self,text="Reset",bg_color="#02b165",border_color="black",command = pressedReset)
        self.Reset.grid(row = 4,column = 2, padx =20, pady = 20, sticky = 'ew')

        self.InvAmt = ctk.CTkLabel(self,text ="Invested Amount")
        self.InvAmt.grid(row = 5, column = 0, padx = 20, pady = 20, sticky = 'ew')

        self.AmtDisp = ctk.CTkLabel(self,text='')
        self.AmtDisp.grid(row = 5, column = 1, padx=20, pady = 20, sticky = 'ew')

        self.MatVal = ctk.CTkLabel(self,text='Maturity Value   ')
        self.MatVal.grid(row = 6, column = 0,padx = 10,pady = 20, sticky = 'ew' )

        self.MatDisp = ctk.CTkLabel(self,text='')
        self.MatDisp.grid(row = 6, column = 1, padx = 20,pady =20, sticky = 'ew')

        

if __name__=="__main__":
    app = App()
    app.mainloop()