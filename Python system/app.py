import tkinter as tk
import mysql.connector
from tkinter import messagebox

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema de cadastro",
        port=3306
    )

janela = tk.Tk()
janela.title("Sistema de Cadastro")
janela.geometry("600x400")

tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Senha").pack()
entrada_senha = tk.Entry(janela, show="*")
entrada_senha.pack()

tk.Label(janela, text="Email").pack()
entrada_email = tk.Entry(janela)
entrada_email.pack()

tk.Label(janela, text="CPF").pack()
entrada_cpf = tk.Entry(janela)
entrada_cpf.pack()

resultado = tk.Label(janela, text="")
resultado.pack(pady=10)

def cadastro():
    nome = entrada_nome.get()
    email = entrada_email.get()
    cpf = entrada_cpf.get()
    senha = entrada_senha.get()

    if not nome or not email or not cpf or not senha:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()

        sql = """
            INSERT INTO cadastro (Nome, Email, CPF, Senha)
            VALUES (%s, %s, %s, %s)
        """
        valores = (nome, email, cpf, senha)

        cursor.execute(sql, valores)
        conexao.commit()

        cursor.close()
        conexao.close()

        resultado.config(
            text=f"✅ CADASTRADO!\n\nNome: {nome}\nEmail: {email}\nCPF: {cpf}"
        )

        entrada_nome.delete(0, tk.END)
        entrada_email.delete(0, tk.END)
        entrada_cpf.delete(0, tk.END)
        entrada_senha.delete(0, tk.END)

    except mysql.connector.Error as erro:
        messagebox.showerror("Erro no banco", str(erro))

tk.Button(janela, text="Cadastrar", command=cadastro).pack(pady=10)

janela.mainloop()

