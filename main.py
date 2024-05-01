import tkinter as tk
from tkinter import messagebox
from viga import Viga

def calcular_volume():
    try:
        base = float(entry_base.get())
        altura = float(entry_altura.get())
        comprimento = float(entry_comprimento.get())

        viga = Viga(base, altura, comprimento)
        volume = viga.calcular_volume()

        messagebox.showinfo("Resultado", f"O volume da viga é: {volume} metros cúbicos.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos.")

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Volume de Concreto")

# Criando os widgets
label_base = tk.Label(root, text="Base:")
label_base.grid(row=0, column=0)
entry_base = tk.Entry(root)
entry_base.grid(row=0, column=1)

label_altura = tk.Label(root, text="Altura:")
label_altura.grid(row=1, column=0)
entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1)

label_comprimento = tk.Label(root, text="Comprimento:")
label_comprimento.grid(row=2, column=0)
entry_comprimento = tk.Entry(root)
entry_comprimento.grid(row=2, column=1)

button_calcular = tk.Button(root, text="Calcular", command=calcular_volume)
button_calcular.grid(row=3, columnspan=2)

# Iniciando o loop principal
root.mainloop()
