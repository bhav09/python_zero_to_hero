#GUI template
 
from tkinter import *
root=Tk()
root.title('Test Screen') #title
root.geometry('1280x720') #set geometry
root.configure(background='snow') #screen color ya fore color

name=Label(root,text='Enter Name:',bg='black',fg='red',width=20,height=3)
name.place(x=100,y=150) #co ordintes of the label

surname=Label(root,text='Enter Surname:',bg='black',fg='red',width=20,height=3)
surname.place(x=100,y=300)

entry1=Entry(root,bg='yellow',fg='red',width=20,font=('times',25,'bold'))  #textbox1: we can write content here 
entry1.place(x=400,y=150)

entry2=Entry(root,bg='yellow',fg='red',width=20,font=('times',25,'bold'))
entry2.place(x=400,y=300)

takeImg=Button(root,text='SUBMIT',fg='white',bg='blue',width=20,height=3,activebackground='Red',font=('times',20,'bold'))
takeImg.place(x=450,y=500)         #submit button which turns from blue to red upon clicking

root.mainloop()     #ye btata h ki program is ready for execution
