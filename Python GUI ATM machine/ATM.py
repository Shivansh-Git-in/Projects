import tkinter as tk
import time

current_balance=100000

class atm(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.shared_data={"Balance":tk.IntVar()}
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage,DepositPage,BalancePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        self.controller.title("ATM")
        self.controller.state("zoomed")

        label1=tk.Label(self,text="WELCOME TO ATM",font=("Orbitron",45,"bold"),fg="white",bg="#3d3d5c")
        label1.pack(pady=25)

        label2=tk.Label(self,text="ENTER YOUT PASSWORD :",font=("orbitron",13),bg="#3d3d5c",fg="white")
        label2.pack(pady=20)
        
        my_password=tk.StringVar()
        password_entry=tk.Entry(self,textvariable=my_password,font=("orbitron",12),width=30)
        password_entry.focus_set()
        password_entry.pack(ipady=8)
        def handle_focus_in(_):
            password_entry.configure(fg="black",show="*")
        password_entry.bind("<FocusIn>",handle_focus_in)
        
        def check_password():
          if my_password.get()=="1234":
             my_password.set("")
             incorrect_password["text"]=""
             controller.show_frame("MenuPage")
          else:
             incorrect_password["text"]="INCORRECT PASSWORD!"

        enter_button=tk.Button(self,text="Log In",command=check_password,relief="solid",borderwidth=2,width=45,height=2)
        enter_button.pack(pady=20)

        incorrect_password=tk.Label(self,text="",font=("orbitron",12),fg="white",bg="#33334d",anchor="n")
        incorrect_password.pack(fill="both",expand=True)

        bottom_frame=tk.Frame(self,relief="raised",borderwidth=5)
        bottom_frame.pack(fill="x",side="bottom")

        visa_photo=tk.PhotoImage(file="visa.png")
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image=visa_photo

        maestro_photo=tk.PhotoImage(file="maestro.png")
        maestro_label=tk.Label(bottom_frame,image=maestro_photo)
        maestro_label.pack(side="left")
        maestro_label.image=maestro_photo

        def tick():
            current_time=time.strftime("%I : %M %p")
            time_label.config(text=current_time)
            time_label.after(100,tick)
            
        time_label=tk.Label(bottom_frame,font=("orbitron",12))
        time_label.pack(side="right")

        tick()
        
class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller
        
        label1=tk.Label(self,text="MAIN MENU",font=("Orbitron",30,"bold"),fg="white",bg="#3d3d5c")
        label1.pack(pady=25)

        selection_label=tk.Label(self,text="Please Select an Option",font=("orbitron",13),fg="white",bg="#3d3d5c",anchor="w")
        selection_label.pack(fill="x")

        button_frame=tk.Frame(self,bg="#33334d")
        button_frame.pack(fill="both",expand=True)

        def withdraw():
            controller.show_frame("WithdrawPage")
        withdraw_button=tk.Button(button_frame,text="Withdraw",command=withdraw,relief="raised",borderwidth=3,width=50,height=5)
        withdraw_button.grid(row=0,column=0,pady=5)

        def deposit():
            controller.show_frame("DepositPage")
        deposit_button=tk.Button(button_frame,text="deposit",command=deposit,relief="raised",borderwidth=3,width=50,height=5)
        deposit_button.grid(row=1,column=0,pady=5)

        def balance():
            controller.show_frame("BalancePage")
        balance_button=tk.Button(button_frame,text="balance",command=balance,relief="raised",borderwidth=3,width=50,height=5)
        balance_button.grid(row=2,column=0,pady=5)

        def exit():
            controller.show_frame("StartPage")
        exit_button=tk.Button(button_frame,text="Exit",command=exit,relief="raised",borderwidth=3,width=50,height=5)
        exit_button.grid(row=3,column=0,pady=5)

        bottom_frame=tk.Frame(self,relief="raised",borderwidth=5)
        bottom_frame.pack(fill="x",side="bottom")

        visa_photo=tk.PhotoImage(file="visa.png")
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image=visa_photo

        maestro_photo=tk.PhotoImage(file="maestro.png")
        maestro_label=tk.Label(bottom_frame,image=maestro_photo)
        maestro_label.pack(side="left")
        maestro_label.image=maestro_photo

        def tick():
            current_time=time.strftime("%I : %M %p")
            time_label.config(text=current_time)
            time_label.after(100,tick)
            
        time_label=tk.Label(bottom_frame,font=("orbitron",12))
        time_label.pack(side="right")

        tick()

class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller

        label1=tk.Label(self,text="WITHDRAW",font=("Orbitron",30,"bold"),fg="white",bg="#3d3d5c")
        label1.pack(pady=25)

        choose_amount_label=tk.Label(self,text="Please Choose the Amount",font=("orbitron",13),fg="white",bg="#3d3d5c",anchor="w")
        choose_amount_label.pack()

        button_frame=tk.Frame(self,bg="#33334d")
        button_frame.pack(fill="both",expand=True)

        def withdraw(amount):
          global current_balance
          current_balance-=amount
          controller.shared_data["Balance"].set(current_balance)
          controller.show_frame("MenuPage")
        hundred_button=tk.Button(button_frame,text="100",command=lambda:withdraw(100),relief="raised",borderwidth=3,width=50,height=5)
        hundred_button.grid(row=0,column=0,pady=5)
        
        fivehundred_button=tk.Button(button_frame,text="500",command=lambda:withdraw(500),relief="raised",borderwidth=3,width=50,height=5)
        fivehundred_button.grid(row=1,column=0,pady=5)

        thousand_button=tk.Button(button_frame,text="1000",command=lambda:withdraw(1000),relief="raised",borderwidth=3,width=50,height=5)
        thousand_button.grid(row=2,column=0,pady=5)

        fivethousand_button=tk.Button(button_frame,text="5000",command=lambda:withdraw(5000),relief="raised",borderwidth=3,width=50,height=5)
        fivethousand_button.grid(row=0,column=1,pady=5,padx=640)
        
        cash=tk.StringVar()
        other_amount_entry=tk.Entry(button_frame,textvariable=cash,width=60,justify="right")
        other_amount_entry.grid(row=1,column=1,pady=5,ipady=30)
        def other_amount(_):
          global current_balance
          current_balance-=int(cash.get())
          controller.shared_data["Balance"].set(current_balance)
          cash.set("")
          controller.show_frame("MenuPage")
        other_amount_entry.bind("<Return>",other_amount)

        def back():
            controller.show_frame("MenuPage")
        back_button=tk.Button(button_frame,text="Back",command=back,relief="raised",borderwidth=3,width=50,height=5)
        back_button.grid(row=2,column=1,pady=5)

        bottom_frame=tk.Frame(self,relief="raised",borderwidth=5)
        bottom_frame.pack(fill="x",side="bottom")

        visa_photo=tk.PhotoImage(file="visa.png")
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image=visa_photo

        maestro_photo=tk.PhotoImage(file="maestro.png")
        maestro_label=tk.Label(bottom_frame,image=maestro_photo)
        maestro_label.pack(side="left")
        maestro_label.image=maestro_photo

        def tick():
            current_time=time.strftime("%I : %M %p")
            time_label.config(text=current_time)
            time_label.after(100,tick)
            
        time_label=tk.Label(bottom_frame,font=("orbitron",12))
        time_label.pack(side="right")

        tick()

class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller

        label1=tk.Label(self,text="DEPOSIT",font=("Orbitron",30,"bold"),fg="white",bg="#3d3d5c")
        label1.pack(pady=25)

        enter_amount_label=tk.Label(self,text="ENTER AMOUNT :",font=("orbitron",13),bg="#3d3d5c",fg="white")
        enter_amount_label.pack(pady=20)

        cash=tk.StringVar()
        deposit_entry=tk.Entry(self,textvariable=cash,font=("orbitron",12),width=30)
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance+=int(cash.get())
            controller.shared_data["Balance"].set(current_balance)
            controller.show_frame("MenuPage")
            cash.set("")
        enter_button=tk.Button(self,text="Enter",command=deposit_cash,relief="raised",borderwidth=3,width=40,height=3)
        enter_button.pack(pady=10)

        
        def back():
            controller.show_frame("MenuPage")
        back_button=tk.Button(self,text="Back",command=back,relief="raised",borderwidth=3,width=40,height=3)
        back_button.pack(pady=3)

        two_tone_label=tk.Label(self,bg="#33334d")
        two_tone_label.pack(fill="both",expand=True)
        
        bottom_frame=tk.Frame(self,relief="raised",borderwidth=5)
        bottom_frame.pack(fill="x",side="bottom")

        visa_photo=tk.PhotoImage(file="visa.png")
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image=visa_photo

        maestro_photo=tk.PhotoImage(file="maestro.png")
        maestro_label=tk.Label(bottom_frame,image=maestro_photo)
        maestro_label.pack(side="left")
        maestro_label.image=maestro_photo

        def tick():
            current_time=time.strftime("%I : %M %p")
            time_label.config(text=current_time)
            time_label.after(100,tick)
            
        time_label=tk.Label(bottom_frame,font=("orbitron",12))
        time_label.pack(side="right")

        tick()
        
class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="#3d3d5c")
        self.controller = controller

        label1=tk.Label(self,text="BALANCE",font=("Orbitron",30,"bold"),fg="white",bg="#3d3d5c")
        label1.pack(pady=25)

        global current_balance
        controller.shared_data["Balance"].set(current_balance)
        balance_label=tk.Label(self,textvariable=controller.shared_data["Balance"],font=("orbitron",13),fg="white",bg="#3d3d5c",anchor="w")
        balance_label.pack(fill="x")

        button_frame=tk.Frame(self,bg="#33334d")
        button_frame.pack(fill="both",expand=True)

        def back():
            controller.show_frame("MenuPage")
        back_button=tk.Button(button_frame,text="Back",command=back,relief="raised",borderwidth=3,width=50,height=5)
        back_button.grid(row=0,column=2,pady=5)
        
        bottom_frame=tk.Frame(self,relief="raised",borderwidth=5)
        bottom_frame.pack(fill="x",side="bottom")

        visa_photo=tk.PhotoImage(file="visa.png")
        visa_label=tk.Label(bottom_frame,image=visa_photo)
        visa_label.pack(side="left")
        visa_label.image=visa_photo

        maestro_photo=tk.PhotoImage(file="maestro.png")
        maestro_label=tk.Label(bottom_frame,image=maestro_photo)
        maestro_label.pack(side="left")
        maestro_label.image=maestro_photo

        def tick():
            current_time=time.strftime("%I : %M %p")
            time_label.config(text=current_time)
            time_label.after(100,tick)
            
        time_label=tk.Label(bottom_frame,font=("orbitron",12))
        time_label.pack(side="right")

        tick()

if __name__ == "__main__":
    app = atm()
    app.mainloop()
