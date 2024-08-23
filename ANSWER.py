import customtkinter
from tkinter import messagebox
import winsound
from PIL import Image, ImageTk
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class ReminderApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Break Reminder")
        self.geometry("800x400")
        self.configure(background="#f0f0f0")

        # Create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="Login Page",
                                                  font=customtkinter.CTkFont(size=50, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=400, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=400, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))


        # Load and place image
        current_path = os.path.dirname(os.path.realpath(__file__))
        image_path = os.path.join(current_path, "background.jpg")
        self.image = Image.open(image_path)
        self.image = self.image.resize((400, 300), Image.ANTIALIAS)  # Resize image to fit
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = customtkinter.CTkLabel(self.login_frame, image=self.photo,text="")
        self.image_label.grid(row=0, column=1, rowspan=4, padx=30, pady=(150, 15))





        # Create main frame for timer display
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure((2, 3), weight=0)
        self.main_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.main_frame.grid_remove()  

        # Create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self.main_frame, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Break Reminder", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 200))
        image_path = os.path.join(current_path, "alarm.jpg")
        self.image = Image.open(image_path)
        self.image = self.image.resize((150, 150), Image.ANTIALIAS) 
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = customtkinter.CTkLabel(self.sidebar_frame, image=self.photo,text="")
        self.image_label.grid(row=0, column=0, columnspan=5, padx=(100, 100), pady=(100, 100), sticky="n")
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Restart Timer", command=self.restart)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Settings", command=self.open_settings)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.timer_label = customtkinter.CTkLabel(self.main_frame, text="Time Remaining: 20:00", font=("Segoe UI", 24, "bold"), text_color="#0000FF")

        self.timer_label.grid(row=0, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # Create settings frame
        self.settings_frame = customtkinter.CTkFrame(self.main_frame, fg_color="transparent")
        self.settings_frame.grid(row=1, column=1, columnspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(0, weight=1)
        self.settings_frame.grid_remove()  

        self.appearance_mode_label = customtkinter.CTkLabel(self.settings_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.settings_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.settings_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=3, column=0, padx=20, pady=(10, 20))

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())
        self.login_frame.grid_forget()  
        self.main_frame.grid(row=0, column=0, sticky="nsew")  

    def countdown(self, count):
        minutes, seconds = divmod(count, 60)
        self.timer_label.configure(text=f"Time Remaining: {minutes:02}:{seconds:02}")
        if count > 0:
            self.after(1000, self.countdown, count - 1)  # Call this function every 1 second
        else:
            self.remind()

    def remind(self):
        print("Time to take a break!")
        winsound.Beep(2500, 1000)  # Play a beep sound
        self.deiconify()
        messagebox.showinfo("Break Time!", "Take a 20-second break!")
        self.iconify()  

    def restart(self):
        print("Countdown restarted.")
        self.countdown(1200)  # Restart the countdown

    def open_settings(self):
        self.settings_frame.grid()   
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = ReminderApp()
    app.mainloop()