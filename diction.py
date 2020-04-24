import time
import keyboard
from tkinter import *
import sqlite3

defi = []

con= sqlite3.connect("dict.db")
cursor=con.cursor()

def tablo_ol():
    cursor.execute("""CREATE TABLE IF NOT EXISTS word (text INT,name TEXT,
                   langId INT,transcription CHAR)""")
    con.commit()
    
def tablo_ol_translation():
    cursor.execute("""CREATE TABLE IF NOT EXISTS translation (text INT,
                   idWord INT, idTranslation INT,idCategory INT)""")
    con.commit()

def veri_cekme(name): 
    cursor.execute("select *from word where name=? ",(name,))
    liste=cursor.fetchmany(0)
    for a in liste:
        idWord=a[0]
        cursor.execute("select *from translation where idWord=? ",(idWord,))
        liste=cursor.fetchmany(0)  
        for b in liste:
            text=b[2]
            
            cursor.execute("select *from word where text=? ",(text,))
            liste=cursor.fetchmany(0)
          
            for c in liste:
                result = c[1]+("")
                defi.append(result)
                

##Gui
app = Tk()
app.title("diction")
app.minsize(width=220, height =255)


###Set scr to defi

def clicker(event):
    tablo_ol()
    tablo_ol_translation()
    clip_text_zero = app.clipboard_get()
    clip_text_low = clip_text_zero.lower()
    clip_text = clip_text_low.strip()

    veri_cekme(clip_text)
    popo = ",".join(defi)
    mean = popo.replace(',', '\n')
    text.insert(END, mean)
    
    
def eraser():
    text.delete(1.0, END)
    defi.clear()
    
scr = Scrollbar(app)
scr.pack(side = RIGHT, fill = Y)

text = Text(app, width = 26,height = 14)
text.pack()

scr.config(command = text.yview)
text.config(yscrollcommand = scr.set)

button = Button(app, text = 'yuppi', width = 9,command = eraser)
button.pack(side = LEFT, padx = 20)
app.bind("<Button-3>", clicker)

app.mainloop()
