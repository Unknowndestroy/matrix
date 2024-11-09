import tkinter as tk
import random


char_set = (
    ' .:;+=*%@#'  
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  
    '가나다라마바사아자차카타파하'  
    '你好世界' 
)

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  
        self.root.configure(bg='black')  
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.cols, self.rows = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.char_height = 20  
        self.create_effect()

    
        self.root.bind('<Escape>', self.quit_app)

    def create_effect(self):
        self.update_effect()

    def update_effect(self):
        self.canvas.delete("all")  


        for y in range(0, self.rows, self.char_height):  
            line = ''.join(random.choice(char_set) for _ in range(self.cols // 10))  
            self.canvas.create_text(
                0, y,
                text=line,
                fill="green",
                font=("Courier", 12),
                anchor="nw"
            )

        self.root.after(30, self.update_effect)  

    def quit_app(self, event):
        self.root.destroy()  # Uygulamayı kapat

def main():
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
