import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme(
    "blue"
)  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("Eli0ts YT 'Dowmloader'")
        self.geometry(f"{620}x{380}")

        # create main entry and button
        self.url = tkinter.StringVar()
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry",textvariable=self.url)
        self.entry.pack(padx=20, pady=(60,20), fill="x")

        self.download_button = customtkinter.CTkButton(
            master=self,
            fg_color="transparent",
            border_width=2,
            text_color=("gray10", "#DCE4EE"),
            text="Download",
            command=self.download_video,
        )
        self.download_button.pack()
        
        self.statusBar = customtkinter.CTkLabel(self, text="Enter a valid YouTube url and click the download button",font=customtkinter.CTkFont(size=20, weight="bold"),)
        self.statusBar.pack( pady=40)
        
        
        
    def download_video(self):
        try:
            self.statusBar.configure(text="Attempting to download...")
            url = self.url.get()
            youtube_object = YouTube(url)
            self.statusBar.configure(text=f"Downloading {youtube_object.title}")
            video = youtube_object.streams.get_highest_resolution()
            video.download('./downloads/')
            self.statusBar.configure(text="Download complete!")
        except Exception as e:
            self.statusBar.configure(text=e.message, fg_color="red")
            
        
        
        
   


     


   


if __name__ == "__main__":
    app = App()
    app.mainloop()
