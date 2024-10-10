import tkinter as tk
import random

# Rastgele karakterler için kullanılacak karakter seti
char_set = (
    ' .:;+=*%@#'  # Semboller
    'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # Harfler ve sayılar
    '가나다라마바사아자차카타파하'  # Korece karakterler
    '你好世界'  # Çince karakterler
)

class MatrixApp:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)  # Tam ekran
        self.root.configure(bg='black')  # Arka plan rengi
        self.canvas = tk.Canvas(root, bg='black', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.cols, self.rows = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.char_height = 20  # Karakter yüksekliği
        self.create_effect()

        # ESC tuşuna basıldığında çıkışı sağlayan fonksiyon
        self.root.bind('<Escape>', self.quit_app)

    def create_effect(self):
        self.update_effect()

    def update_effect(self):
        self.canvas.delete("all")  # Önceki çizimleri temizle

        # Ekranın tamamını kapsayan rastgele karakterler
        for y in range(0, self.rows, self.char_height):  # Karakter yüksekliği kadar aralıkla yerleştir
            line = ''.join(random.choice(char_set) for _ in range(self.cols // 10))  # Ekranın genişliği kadar karakter
            self.canvas.create_text(
                0, y,
                text=line,
                fill="green",
                font=("Courier", 12),
                anchor="nw"
            )

        self.root.after(30, self.update_effect)  # 30 ms sonra tekrar güncelle

    def quit_app(self, event):
        self.root.destroy()  # Uygulamayı kapat

def main():
    root = tk.Tk()
    app = MatrixApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
