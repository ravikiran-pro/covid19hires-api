from tkinter import*
from tkinter import messagebox
import sqlite3
currpage=0
datas=[]
new=[]

def changebottomtab():
	try:
		new[0].pack_forget()
	except:
		print('ss')

def changenextframe(datas,frames):
	global currpage
	if(currpage<frames):
		datas[currpage].pack_forget()
		currpage+=1
		datas[currpage].pack()
	else:
		messagebox.showinfo("End", "No more jobs available")
def changepreviousframe(datas,frames):
	global currpage
	if(currpage>0):
		datas[currpage].pack_forget()
		currpage-=1
		datas[currpage].pack()
	else:
		messagebox.showinfo("start", "can't go before")
def removepreviousframes():
	for i in range(len(datas)):
		datas[i].pack_forget()

def Assembler(data):
	removepreviousframes()
	changebottomtab()
	global currpage,datas
	currpage=0
	datas.append(Frame())
	jobcount=0
	page=0
	for jobs in data.fetchall():
		Label(datas[page],text=jobs[0],width=8,anchor='w',justify="left").grid(row=jobs[0],column=0)
		Label(datas[page],text=jobs[1],width=30,anchor='w',justify="left").grid(row=jobs[0],column=1)
		Label(datas[page],text=jobs[2],width=24,anchor='w',justify="left").grid(row=jobs[0],column=2)
		jobcount+=1
		if(jobcount%15==0):
			datas.append(Frame())
			page+=1
	datas[0].pack(anchor='w')
	new.append(Frame())
	Button(new[0],text="front",command=lambda:changenextframe(datas,page)).pack()
	Button(new[0],text="back",command=lambda:changepreviousframe(datas,page)).pack()
	new[0].pack()
def onpress(location):
	cur=sqlite3.connect("data").cursor()	
	data=cur.execute('select * from {}'.format(location))
	Assembler(data)
	cur.close()

win=Tk()
win.geometry('450x600')
windowwidth=450
tabwidth=windowwidth//30
Tab=Frame()
Button(Tab,text="chennai",width=tabwidth,command=lambda:onpress('chennai')).pack(side="left",anchor="n")
Button(Tab,text="bangalore",width=tabwidth,command=lambda:onpress('bangalore')).pack(side="left",anchor="n")
Button(Tab,text="hyderabad",width=tabwidth,command=lambda:onpress('hyderabad')).pack(side="left",anchor="n")
Tab.pack()
win.mainloop()