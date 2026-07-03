from tkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("WT Studio Client - 登录")
        self.geometry("350x350")
        self.resizable(False,False)
        
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, padx=20, pady=20)
        
        self.window_title = ctk.CTkLabel(self.main_frame, text="LOGIN", font=("Ubuntu Mono", 70))
        self.window_title_line = ctk.CTkLabel(self.main_frame, text="|", font=("Ubuntu Mono", 70))
        self.window_subtitle = ctk.CTkLabel(self.main_frame, text="登录", font=("Ubuntu Mono", 25))
        
        self.window_title.grid(row=0, column=0, sticky="s")
        self.window_title_line.grid(row=0, column=1, padx=(5, 5))
        self.window_subtitle.grid(row=0, column=2, sticky="s", padx=(10, 0), pady=(0, 10))
        
        self.form_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.form_frame.grid(row=1, column=0, pady=20)
        
        self.username_tip = ctk.CTkLabel(self.form_frame, text="用户名 ", font=("Ubuntu Mono", 23))
        self.username = ctk.CTkEntry(self.form_frame, font=("Ubuntu Mono", 15), width=200)
        self.username_tip.grid(row=0, column=0, sticky="e")
        self.username.grid(row=0, column=1, sticky="w")
        
        self.password_tip = ctk.CTkLabel(self.form_frame, text="密  码 ", font=("Ubuntu Mono", 23))
        self.password = ctk.CTkEntry(self.form_frame, font=("Ubuntu Mono", 15), width=200)
        self.password_tip.grid(row=1, column=0, sticky="e",pady=10)
        self.password.grid(row=1, column=1, sticky="w",pady=10)

        self.enter = ctk.CTkButton(self,text="登录",height=35,font=("Ubuntu Mono", 23))
        self.enter.grid(row=2, column=0, sticky="e", padx=100)

    def jump_to_main(self):
        self.destroy()
        main_window = MainWindow()
        MainWindow.mainloop()
    
    def verif_login(self):
        if True:
            self.jump_to_main()

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WT Studio Client - 主界面")
        

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()