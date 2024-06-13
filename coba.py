import tkinter as tk
from tkinter import Toplevel

def create_popup():
    popup = Toplevel(root)
    popup.title("Popup Window")
    
    # Setel window agar selalu di atas
    popup.attributes("-topmost", True)
    
    # Membuat window modal
    popup.grab_set()
    
    label = tk.Label(popup, text="This is a popup window")
    label.pack(padx=20, pady=20)

    button = tk.Button(popup, text="Close", command=popup.destroy)
    button.pack(pady=10)

    # Menunggu sampai jendela popup ditutup
    popup.transient(root)
    root.wait_window(popup)

root = tk.Tk()
root.title("Main Window")

main_label = tk.Label(root, text="This is the main window")
main_label.pack(padx=20, pady=20)

popup_button = tk.Button(root, text="Open Popup", command=create_popup)
popup_button.pack(pady=10)

root.mainloop()