import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    app_title = "Results Analyser"
    nav_buttons = ["Home", "Analysis", "Data"]

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Eli0ts YT 'Dowmloader'")
        self.geometry(f"{720}x{580}")

        # create main entry and button
        self.url = tkinter.StringVar()
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry",textvariable=self.url)
        self.entry.pack(padx=20, pady=20, fill="x")

        self.download_button = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="Download"
        )
        self.download_button.pack()
        
        
   

        # set default values

     


   


if __name__ == "__main__":
    app = App()
    app.mainloop()
