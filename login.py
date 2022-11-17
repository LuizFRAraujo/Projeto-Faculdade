from tkinter import *
from tkinter import messagebox
import sqlite3
from con_e_cad_tec import *                    




#                                       TELA DE LOGIN

login = Tk()
class App:
    def __init__(self) -> None:
        self.login = login
        self.janela_inicio()
        




    def janela_inicio(self):                
        self.login.title('Tela de login')
        self.login.geometry('400x500+100+100')
        self.login.iconbitmap("img-icons\\casa.ico")
        self.login.resizable(width=False, height=False)

        #                               Labels e entrys TELA LOGIN
        self.title = Label(login, text='LOGIN', font=('Times','24','bold'), pady=20)
        self.title.pack()

        self.user = Label(login, text='Nome:', font=('Times', '12'))
        self.user.place(x=10, y=100)
        self.user_entry = Entry(login, width= 40, font=('Times','12'),justify= 'center')
        self.user_entry.place(x=20, y=140)


        self.lab_passowrd = Label(login, text='Senha:', font=('Times','12'))
        self.lab_passowrd.place(x=10, y=200)
        self.login_passowrd = Entry(login, width= 40, font=('Times','12'), justify= 'center',show='*')
        self.login_passowrd.place(x=20, y=240,)

        self.lab_cadastrar = Label(login, text='Não tem cadastro? Clique em cadastrar', font=('Times', '12'))
        self.lab_cadastrar.place(x=10, y= 280)


        #                               Butões

        self.but_entrar = Button(login, width=12, height=2, relief='groove',command=self.entrar ,text='ENTRAR', font=('Times','14','bold'), bg='lightblue', activebackground='lightgreen')
        self.but_entrar.place(x=20, y=380)

        self.but_cadastrar = Button(login, width=12, height=2, relief='groove', command= self.janela_cadastro ,text='CADASTRAR', font=('Times','14','bold'), bg='lightblue', activebackground='lightgreen')
        self.but_cadastrar.place(x=200, y=380)

        self.login.mainloop()

    def janela_cadastro(self):
        self.cadastro = Toplevel()
        self.cadastro.title('Novo cadastro')
        self.cadastro.geometry('400x500+100+100')
        self.cadastro.resizable(False, False)
        self.cadastro.transient(self.login)
        self.cadastro.focus_force()
        self.cadastro.grab_set()
#                                        CRIANDO LABELS E ENTRYS CADASTRO
        self.texto = Label(self.cadastro, text='Novo cadastro', font=('Times','24','bold'), pady=20)
        self.texto.pack()

        self.lab_cadastro = Label(self.cadastro, text='Nome:', font=('Times', '12'))
        self.lab_cadastro.place(x=10, y=100)
        self.nome_cadastro = Entry(self.cadastro, width= 40, font=('Times','12'),justify= 'center')
        self.nome_cadastro.place(x=20, y=140)


        self.lab_passowrd = Label(self.cadastro, text='Senha:', font=('Times','12'))
        self.lab_passowrd.place(x=10, y=200)
        self.senha_cadastro_passowrd = Entry(self.cadastro, width= 40, font=('Times','12'), justify= 'center',show='*')
        self.senha_cadastro_passowrd.place(x=20, y=240,)

        self.but_registrar = Button(self.cadastro, width=12, height=2, relief='groove', command= self.cadastrar ,text='CADASTRAR', font=('Times','14','bold'), bg='lightblue', activebackground='lightgreen')
        self.but_registrar.place(x=125, y= 300)



#                                           CHAMANDO NOVO ARQUIVO  
    def janela2 (self):
        self.login.destroy()
        self.root2 = Application(Funcs, Relatorios, Validadores)
        
    def entrar(self):
        self.conn = sqlite3.connect('Acesso_app.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("SELECT * FROM usuario_senha WHERE nome='{}'".format(self.user_entry.get()))
        consulta = self.cursor.fetchall()
        self.conn.close()
        if consulta == []:
            messagebox.showerror('Erro', "Precisa realizar o cadastro")
        elif self.user_entry.get() == consulta[0][1] and self.login_passowrd.get() == consulta [0][2]:
            print('deu bom')
            self.janela2()


        elif self.user_entry.get() == consulta[0][1] and self.login_passowrd.get() != consulta [0][2]:
            messagebox.showerror('Erro', "Senha incorreta")
        else:
            print('erro inesperado')


    def cadastrar(self):
        self.nome = self.nome_cadastro.get()
        self.senha = self.senha_cadastro_passowrd.get()
        self.conn = sqlite3.connect('Acesso_app.db')
        self.cursor = self.conn.cursor()
        lista = [self.nome, self.senha]
        if self.nome == '':
            messagebox.showerror('Erro', "O campo NOME não pode ser vazio")
        elif self.senha == '':
            messagebox.showerror('Erro', "O campo NOME não pode ser vazio")
        else:
            self.cursor.execute(""" INSERT INTO usuario_senha (nome, senha) VALUES (?,?)""", lista)
            self.conn.commit()
            messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')
            self.conn.close()
            self.cadastro.destroy()

App()
