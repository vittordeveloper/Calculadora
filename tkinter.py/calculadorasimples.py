from tkinter import *


# Função de cálculo
def calculando():
    erro_tratamento.place_forget()
    expressao = Digite.get()
        
    try:
        total = eval(expressao)
        Digite.delete(0, END)
        Digite.insert(END, total)
        if total > 10000000:
            raise ValueError
        if not expressao or expressao.isdigit():
            raise ArithmeticError
    except:
        erro_tratamento.place(x=170, y=60, anchor='center')
        Digite.delete(0, END)

# Adiciona um número no display
def pegar_numero(n):
    erro_tratamento.place_forget()
    expressao = Digite.get()
    Digite.insert(END, n)

# Adiciona o operador (+)
def pegar_soma():
    erro_tratamento.place_forget()
    expressao = Digite.get()
    Digite.insert(END, '+')

# Adiciona o operador (-)
def pegar_menos():
    erro_tratamento.place_forget()
    expressao = Digite.get()
    Digite.insert(END, '-')

def limpando():
    erro_tratamento.place_forget()
    Digite.delete(0, END)

# Criando a janela
janela = Tk()

# Config
janela.geometry("340x400")
janela.title("Calculadora")
janela.resizable(False, False)

# Campo de entrada
Digite = Entry(janela, font=("Arial", 40), width=10, justify='center', bg='white')
Digite.pack(padx=10, pady=20, ipady=10)

# Criando os botões numéricos
numeros = [
    (1, 50, 200), (2, 120, 200), (3, 190, 200),
    (4, 50, 250), (5, 120, 250), (6, 190, 250),
    (7, 50, 300), (8, 120, 300), (9, 190, 300),
    (0, 120, 350)
]

# Loop (pegando os números e as posições dadas à partir do **numeros**(variavel))
for num, x, y in numeros:
    Button(janela, text=num, width=8, height=2, command=lambda n=num: pegar_numero(n)).place(x=x, y=y, anchor='center')

# Botão de soma
Button(janela, text='+', width=8, height=2, command=pegar_soma).place(x=190, y=350, anchor='center')

# Botão menos
Button(janela, text='-', width=8, height=2, command=pegar_menos).place(x=280, y=300, anchor='center')

# Botão calcular
Button(janela, text='Calcular', width=8, height=2, command=calculando).place(x=280, y=350, anchor='center')

# Botão Limpar
limpar = Button(janela, text='Limpar', width=8, height=2, command=limpando)
limpar.place(x=50, y=350, anchor='center')

# Mensagem de erro
erro_tratamento = Label(janela, text='Erro', font=('Arial', 40), background='white')
erro_tratamento.forget()

janela.mainloop()
