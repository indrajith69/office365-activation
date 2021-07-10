from tkinter import *
from tkinter import messagebox
import subprocess

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

class app:
	def __init__(self):
		self.bg = '#081828'
		self.fg = '#FFFFFF'
		self.window()

	def window(self):
		self.root = Tk()
		self.root.title('microsoft office 365')
		self.root.geometry('350x150')
		self.root.config(bg=self.bg)

		self.btn_install  = Button(self.root,text='install' ,fg=self.fg,bg=self.bg,font=14,command=self.install)
		self.btn_activate = Button(self.root,text='activate',fg=self.fg,bg=self.bg,font=14,command=self.activate)

		self.btn_install.pack(side=LEFT,expand=True,fill=BOTH,padx=10,pady=50)
		self.btn_activate.pack(side=LEFT,expand=True,fill=BOTH,padx=10,pady=50)

		#CreateToolTip(self.btn_install,'hello')
		self.root.mainloop()

	def install(self):
		print('installing....')
		print('installed!')

	def activate(self):
		print('activated')



app()