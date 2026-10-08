import tkinter as tk
def click():
    pass
root= tk.Tk()
root.title('Password gen')
root.geometry("300x150")
button= tk.Button(root, text = "Generate", command=click)
button.pack()

root.mainloop()