import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Função que gera o gráfico
def gerar_grafico():
    try:
        homens = float(entry_homens.get())
        mulheres = float(entry_mulheres.get())

        if homens < 0 or mulheres < 0:
            messagebox.showerror("Erro", "Os valores não podem ser negativos.")
            return

        # Dados e rótulos do gráfico
        valores = [homens, mulheres]
        labels = ['Homens', 'Mulheres']
        cores = ['skyblue', 'pink']

        # Criando gráfico de pizza
        plt.figure(figsize=(5,5))
        plt.pie(valores, labels=labels, autopct='%1.1f%%', colors=cores, startangle=90)
        plt.title("Vendas de Pizza por Gênero")
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")

# Interface principal
janela = tk.Tk()
janela.title("Gráfico de Pizza - Vendas de Pizza")
janela.geometry("350x250")

tk.Label(janela, text="Pizzas vendidas para homens:").pack(pady=5)
entry_homens = tk.Entry(janela)
entry_homens.pack()

tk.Label(janela, text="Pizzas vendidas para mulheres:").pack(pady=5)
entry_mulheres = tk.Entry(janela)
entry_mulheres.pack()

tk.Button(janela, text="Gerar gráfico", command=gerar_grafico).pack(pady=20)

janela.mainloop()


#tkinter cria a interface (caixas e botões)

# matplotlib.pyplot gera o gráfico de pizza

#entry_homens.get() pega o valor digitado pelo usuário

# plt.pie() cria o gráfico de pizza