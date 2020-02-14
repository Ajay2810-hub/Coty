import os
import shutil
from tkinter import *
from tkinter import messagebox

win=Tk()
win.geometry("500x500")
win.title("COTY")
win["bg"]='#fff'

def copy():
    copy1()

copy_btn=Button(win,text="COPY",fg="#fff",bg='crimson',bd=0,activeforeground="yellow",activebackground="lightblue",command=copy)
copy_btn.config(font="helvetica 20")
copy_btn.place(x=200,y=100)

def move():
    move1()

move_btn=Button(win,text="MOVE",fg="#fff",bg='lightgreen',bd=0,activeforeground="#fff",activebackground="green",command=move)
move_btn.config(font="helvetica 20")
move_btn.place(x=200,y=200)

def delete():
    delete1()
    
delete_btn=Button(win,text="Delete",fg="#fff",bg='#0080ff',bd=0,activeforeground="crimson",activebackground="yellow",command=delete)
delete_btn.config(font="helvetica 20")
delete_btn.place(x=200,y=300)

fname=Label(win,text="Filename",bg="#fff")
fname.config(font="helvetica 20")

fname1=Entry(win,bg="#fff",fg="crimson")
fname1.config(font="helvetica 20")

des=Label(win,text="Destination",bg="#fff")
des.config(font="helvetica 20")

des1=Entry(win,bg="#fff",fg="crimson")
des1.config(font="helvetica 20")

def copy2():
    copy3()
    
copy_btn1=Button(win,text="COPY",fg="#fff",bg='crimson',bd=0,activeforeground="yellow",activebackground="lightblue",command=copy2)
copy_btn1.config(font="helvetica 20")

fname2=Label(win,text="Filename",bg="#fff")
fname2.config(font="helvetica 20")

fname3=Entry(win,bg="#fff",fg="crimson")
fname3.config(font="helvetica 20")

des2=Label(win,text="Destination",bg="#fff")
des2.config(font="helvetica 20")

des3=Entry(win,bg="#fff",fg="crimson")
des3.config(font="helvetica 20")

def move2():
    move3()
    
move_btn1=Button(win,text="MOVE",fg="#fff",bg='lightgreen',bd=0,activeforeground="#fff",activebackground="green",command=move2)
move_btn1.config(font="helvetica 20")

fname4=Label(win,text="Filename",bg="#fff")
fname4.config(font="helvetica 20")

fname5=Entry(win,bg="#fff",fg="crimson")
fname5.config(font="helvetica 20")

def delete2():
    delete3()
    
delete_btn1=Button(win,text="Delete",fg="#fff",bg='#0080ff',bd=0,activeforeground="crimson",activebackground="yellow",command=delete2)
delete_btn1.config(font="helvetica 20")

def back():
    back1()
    
backbtn=Button(win,text="<",bg="crimson",fg="#fff",bd=0,width=2,activebackground="#fff",activeforeground="crimson",command=back)
backbtn.config(font="helvetica 20")

def copy1():
    copy_btn.place(x=-1000,y=100)
    move_btn.place(x=-1000,y=200)
    delete_btn.place(x=-1000,y=300)
    #reg
    fname.place(x=20,y=100)
    des.place(x=20,y=180)
    fname1.place(x=170,y=103)
    des1.place(x=170,y=183)
    copy_btn1.place(x=200,y=270)
    backbtn.place(x=5,y=5)
    backbtn.config(fg="white",bg="crimson",activebackground="#fff",activeforeground="crimson")

def move1():
    copy_btn.place(x=-1000,y=100)
    move_btn.place(x=-1000,y=200)
    delete_btn.place(x=-1000,y=300)
    #reg
    fname2.place(x=20,y=100)
    des2.place(x=20,y=180)
    fname3.place(x=170,y=103)
    des3.place(x=170,y=183)
    move_btn1.place(x=200,y=270)
    backbtn.place(x=5,y=5)
    backbtn.config(fg="white",bg="lightgreen",activebackground="#fff",activeforeground="lightgreen")

def delete1():
    copy_btn.place(x=-1000,y=100)
    move_btn.place(x=-1000,y=200)
    delete_btn.place(x=-1000,y=300)
    #reg
    fname4.place(x=20,y=100)
    fname5.place(x=170,y=103)
    delete_btn1.place(x=200,y=200)
    backbtn.place(x=5,y=5)
    backbtn.config(fg="white",bg="#0080ff",activebackground="#fff",activeforeground="#0080ff")

def copy3():
    file=str(fname1.get())
    dest=str(des1.get())
    if os.path.exists(f"{file}"):
       if os.path.exists(f"{dest}"):
          shutil.copy(file,dest)
       else:
          messagebox.showerror("COTY","Invalid Destination!!")
    else:
       messagebox.showerror("COTY","File Doesn't Exists!!")

def move3():
    file=str(fname3.get())
    dest=str(des3.get())
    if os.path.exists(f"{file}"):
       if os.path.exists(f"{dest}"):
          shutil.move(file,dest)
       else:
          messagebox.showerror("COTY","Invalid Destination!!")
    else:
       messagebox.showerror("COTY","File Doesn't Exists!!")
      
def delete3():
    file=str(fname5.get())
    if os.path.exists(f"{file}"):
       os.remove(file)
    else:
       messagebox.showerror("COTY","File Doesn't Exists!!")

def back1():
    copy_btn.place(x=200,y=100)
    move_btn.place(x=200,y=200)
    delete_btn.place(x=200,y=300)
    #reg
    fname4.place(x=-1000,y=100)
    fname5.place(x=-1000,y=103)
    delete_btn1.place(x=-1000,y=200)
    backbtn.place(x=-1000,y=5)
    fname2.place(x=-1000,y=100)
    des2.place(x=-1000,y=180)
    fname3.place(x=-1000,y=103)
    des3.place(x=-1000,y=183)
    move_btn1.place(x=-1000,y=270)
    fname.place(x=-1000,y=100)
    des.place(x=-1000,y=180)
    fname1.place(x=-1000,y=103)
    des1.place(x=-1000,y=183)
    copy_btn1.place(x=-1000,y=270)
    dele1=len(fname1.get())
    fname1.delete(first=0,last=dele1)
    dele1=len(fname3.get())
    fname3.delete(first=0,last=dele1)
    dele1=len(des1.get())
    des1.delete(first=0,last=dele1)
    dele1=len(des3.get())
    des3.delete(first=0,last=dele1)
    dele1=len(fname5.get())
    fname5.delete(first=0,last=dele1)
