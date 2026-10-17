import tkinter as tk
from tkinter import ttk


def main():
    window = tk.Tk()
    window.title("Hello World")
    window.geometry("360x180")
    window.minsize(280, 150)

    frame = ttk.Frame(window, padding=24)
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text="Hello, World!", font=("TkDefaultFont", 20)).pack(
        expand=True
    )
    ttk.Button(frame, text="Close", command=window.destroy).pack(pady=(16, 0))
    window.bind("<Escape>", lambda event: window.destroy())
    window.mainloop()


if __name__ == "__main__":
    main()
