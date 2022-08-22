from tkinter import *
import base64
from tkinter import messagebox
import tkinter.font as font

#Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) +
                     ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


#Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

        dec.append(list_dec)
    return "".join(dec)

#Function that executes on clicking Show Message function
def Result():
    msg = Message.get()
    k= key.get()
    i = mode.get()
    if (i==1):
        Output.set(encode(k, msg))
    elif(i==2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('Encrypt & Decrypt', 'Please Choose one of Encryption or Decrption and Try again.')

#Function that executes on clicking Reset function
def Reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")
    

wn = Tk()
wn.geometry("630x600")
#wn.eval('tk::PlaceWindow . center')
wn.configure(bg='blanchedalmond')
wn.title("Encryptor Decryptor")
wn.resizable(False,False)
# Gets the requested values of the height and width.
windowWidth = wn.winfo_reqwidth()
windowHeight = wn.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(wn.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(wn.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
wn.geometry("+{}+{}".format(positionRight, positionDown))

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

#headingFrame1 = Frame(wn,bg="blue",bd=5)
#headingFrame1.place(x=20, y=100)

headingLabel = Label(wn, text=" Welcome to \n Encryptor Decryptor", fg='grey19', font=('Courier',20,'bold'), borderwidth=1.5, relief="solid", width=25, height=4)
headingLabel.place(x=125, y=40)


label1 = Label(wn, text='Enter the Message', font=('Courier',14, 'bold'))
label1.place(x=10,y=200)

msg = Entry(wn,textvariable=Message, width=35, font=('calibre',12,'normal'))
msg.place(x=250,y=200)

label2 = Label(wn, text='Enter the key', font=('Courier',14, 'bold'))
label2.place(x=10,y=275)

InpKey = Entry(wn, textvariable=key,  width=35,font=('calibre',12,'normal'))
InpKey.place(x=250,y=275)

label3 = Label(wn, text='Click one', font=('Courier',14, 'bold'))
label3.place(x=10,y=350)

Radiobutton(wn, text='Encrypt',  variable=mode, value=1, font=('Courier',12, 'bold')).place(x=250,y=350) 
Radiobutton(wn, text='Decrypt', variable=mode, value=2, font=('Courier',12, 'bold')).place(x=350,y=350) 

label3 = Label(wn, text='Result', font=('Courier',14, 'bold'))
label3.place(x=10,y=425)

res = Entry(wn,textvariable=Output, width=35, font=('calibre',12,'normal'))
res.place(x=250,y=425)


ResetBtn = Button(wn, text='Reset', bg='honeydew2', fg='black', width=15,height=1,command=Reset)
ResetBtn['font'] = font.Font( size=14)
ResetBtn.place(x=40,y=500)

ShowBtn = Button(wn,text="Show Message",bg='lavender blush2', fg='black',width=15,height=1,command=Result)
ShowBtn['font'] = font.Font( size=14)
ShowBtn.place(x=230,y=500)

QuitBtn = Button(wn, text='Exit', fg='black',width=15,height=1, command=wn.destroy)
QuitBtn['font'] = font.Font( size=14)
QuitBtn.place(x=420,y=500)


wn.mainloop()
