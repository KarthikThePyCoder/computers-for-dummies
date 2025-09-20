import tkinter as tk   # Define the following modules

# Create the window and functions
root = tk.Tk()

def red_bg():
    root.config(bg='red')

def white_bg():
    root.config(bg='white')

def quit_app():
    root.destroy()

button1 = tk.Button(root, text='Off the lights', command=white_bg)
button1.pack(padx=43, pady=43)

button2 = tk.Button(root, text='On the lights', command=red_bg)
button2.pack(padx=45, pady=45)

quit_button = tk.Button(root, text='Quit', command=quit_app)
quit_button.pack(padx=47, pady=47)

root.title('Zero-Or-All?')
root.geometry('500x400')
root.mainloop()