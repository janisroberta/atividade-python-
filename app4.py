[import tkinter as tk

def clicar(botao):
    texto_atual = str(visor.get())
    texto_atual += str(botao)
    visor.deimport tkinter as tk

def clicar(botao):
    texto_atual = str(visor.get())
    texto_atual += str(botao)
    visor.delete(0, tk.END)
    visor.insert(0, texto_atual)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

def limpar():
    visor.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criar o visor
visor = tk.Entry(janela, font=("Arial", 20))
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Criar os botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

linha = 1
coluna = 0

for botao in botoes:
    tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 15), command=lambda botao=botao: clicar(botao)).grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Adicionar botões especiais (limpar e calcular)
tk.Button(janela, text='C', padx=20, pady=20, font=("Arial", 15), command=limpar).grid(row=5, column=0, padx=5, pady=5)
tk.Button(janela, text='=', padx=20, pady=20, font=("Arial", 15), command=calcular).grid(row=5, column=1, columnspan=3, padx=5, pady=5)

# Iniciar a aplicação
janela.mainloop()lete(0, tk.END)
    visor.insert(0, texto_atual)

def calcular():
    try:
        resultado = eval(visor.get())
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except:
        visor.delete(0, tk.END)
        visor.insert(0, "Erro")

def limpar():
    visor.delete(0, tk.END)

# Criar a janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Criar o visor
visor = tk.Entry(janela, font=("Arial", 20))
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=10, ipady=10)

# Criar os botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

linha = 1
coluna = 0

for botao in botoes:
    tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 15), command=lambda botao=botao: clicar(botao)).grid(row=linha, column=coluna, padx=5, pady=5)
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Adicionar botões especiais (limpar e calcular)
tk.Button(janela, text='C', padx=20, pady=20, font=("Arial", 15), command=limpar).grid(row=5, column=0, padx=5, pady=5)
tk.Button(janela, text='=', padx=20, pady=20, font=("Arial", 15), command=calcular).grid(row=5, column=1, columnspan=3, padx=5, pady=5)

# Iniciar a aplicação
janela.mainloop()
