import tkinter as tk

root = tk.Tk()
root.overrideredirect(True)

# Math to center it perfectly above the Windows Taskbar
dock_w = 500
dock_h = 55
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
x = (screen_w // 2) - (dock_w // 2)
y = screen_h - dock_h - 45 # Sits just above the standard Windows taskbar

root.geometry(f"{dock_w}x{dock_h}+{x}+{y}")
root.attributes("-alpha", 0.9) # Slightly see-through
root.configure(bg='#1a1a1a')

# Add icons with a "Mac" feel
icons = ["Finder", "Safari", "Photos", "Settings", "Trash"]
for icon in icons:
    lbl = tk.Label(root, text=icon, fg="white", bg="#1a1a1a", font=("Arial", 9), padx=15)
    lbl.pack(side="left", expand=True)
    # Hover effect
    lbl.bind("<Enter>", lambda e, l=lbl: l.config(fg="#00ccff", font=("Arial", 10, "bold")))
    lbl.bind("<Leave>", lambda e, l=lbl: l.config(fg="white", font=("Arial", 9)))

# Right-click to close safely
root.bind("<Button-3>", lambda e: root.destroy())

root.mainloop()