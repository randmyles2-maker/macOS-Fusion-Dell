import tkinter as tk
import pygetwindow as gw

def update_top_bar():
    try:
        # Detect the current window title
        active_window = gw.getActiveWindow()
        name = active_window.title.split(" - ")[-1] if active_window else "Finder"
        label.config(text=f"   {name}")
    except:
        label.config(text="   Finder")
    root.after(1000, update_top_bar)

root = tk.Tk()
root.overrideredirect(True) # Removes Windows borders
root.geometry(f"{root.winfo_screenwidth()}x28+0+0") # Fixed at top
root.attributes("-alpha", 0.9)
root.configure(bg='#000000')

label = tk.Label(root, text="   Finder", fg="white", bg="#000000", font=("Arial", 9, "bold"))
label.pack(side="left", padx=10)

update_top_bar()
root.mainloop()