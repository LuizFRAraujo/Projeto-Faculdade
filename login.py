from tkinter import *

#                               TELA DE LOGIN
login = Tk()
login.title('Tela de login')
login.geometry('400x500')
login.iconbitmap("img-icons\\casa.ico")
login.resizable(width=False, height=False)

#                               Labels e entrys
title = Label(login, text='LOGIN', font=('Times','24','bold'), pady=20)
title.pack()

user = Label(login, text='Nome:', font=('Times', '12'))
user.place(x=10, y=100)
user_entry = Entry(login, width= 40, font=('Times','12'),justify= 'center')
user_entry.place(x=20, y=140)


passowrd = Label(login, text='Senha:', font=('Times','12'))
passowrd.place(x=10, y=200)
passowrd = Entry(login, width= 40, font=('Times','12'), justify= 'center')
passowrd.place(x=20, y=240,)

lab_cadastrar = Label(login, text='Não tem cadastro? Clique em cadastrar', font=('Times', '12'))
lab_cadastrar.place(x=10, y= 280)


#                               Butões

but_entrar = Button(login, width=12, height=2, relief='groove', text='ENTRAR', font=('Times','14','bold'), bg='lightblue', activebackground='lightgreen')
but_entrar.place(x=20, y=380)

but_cadastrar = Button(login, width=12, height=2, relief='groove', text='CADASTRAR', font=('Times','14','bold'), bg='lightblue', activebackground='lightgreen')
but_cadastrar.place(x=200, y=380)


login.mainloop()