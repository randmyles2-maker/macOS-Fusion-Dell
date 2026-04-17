import tkinter as tk

def on_enter(e):
    # This creates the "magnify" effect
    e.widget.config(font=("Arial", 14, "bold"), fg="#00ccff")

def on_leave(e):
    e.widget.config(font=("Arial", 10), fg="white")

root = tk.Tk()
root.overrideredirect(True)
# Puts the dock at the bottom center
w = 400
h = 60
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
root.geometry(f"{w}x{h}+{(sw//2)-(w//2)}+{sh-h-10}")
root.attributes("-topmost", True)
root.configure(bg='#1a1a1a')

# Add some fake "Mac" apps
apps = ["Finder", "Messages", "Safari", "Music", "Settings"]
for app in apps:
    btn = tk.Label(root, text=app, fg="white", bg="#1a1a1a", font=("Arial", 10), padx=10)
    btn.pack(side="left", expand=True)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

root.mainloop()