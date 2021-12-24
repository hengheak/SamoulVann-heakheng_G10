#  IMPORTS------------------------------------------------------
import tkinter as tk
#  MAIN Code-----------------------------------------------------
root = tk.Tk()

#Size of Window--------------------------------------------------
root.geometry("600x655")
root.resizable(0,0)
canvas = tk.Canvas(root)

#Title----------------------------------------------------------
root.title('Samoul_G-10')



canvas.pack(expand=True, fill="both")
root.mainloop()