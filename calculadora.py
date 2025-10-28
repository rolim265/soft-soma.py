import tkinter as tk

def somar():
    resultado["text"] = float(num1.get()) + float(num2.get())

def subtrair():
    resultado["text"] = float(num1.get()) - float(num2.get())

janela = tk.Tk()
janela.title("mini calculator")
janela.geometry("300x200")


tk.Label(janela, text="numero 01").pack()
num1 = tk.Entry(janela)
num1.pack()

tk.Label(janela, text="numeo 02").pack()
num2 = tk.Entry(janela)
num2.pack()

tk.Button(janela, text="Somar", command=somar).pack(pady=5)
tk.Button(janela, text="Subtrair", command=subtrair).pack(pady=5)


resultado = tk.Label(janela, text="Resultado: ")
resultado.pack(pady=10)

janela.mainloop()