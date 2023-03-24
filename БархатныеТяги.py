import tkinter as tk
import webbrowser

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.title("Человек с бархатными тягами")
        self.create_widgets()

    def create_widgets(self):
        self.exit_btn = tk.Button(self, text="Выйти", command=self.quit)
        self.exit_btn.pack(side="left", padx=10, pady=10)

        self.vk_btn = tk.Button(self, text="Вконтакте", command=self.open_vk)
        self.vk_btn.pack(side="left", padx=10, pady=10)

        self.support_btn = tk.Button(self, text="Техподдержка", command=self.open_telegram)
        self.support_btn.pack(side="left", padx=10, pady=10)

    def open_vk(self):
        webbrowser.open_new_tab("https://vk.com/petrovdan2007")

    def open_telegram(self):
        webbrowser.open_new_tab("https://t.me/danpetss")

app = App()
app.mainloop()
