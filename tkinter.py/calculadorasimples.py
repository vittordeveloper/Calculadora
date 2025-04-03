from tkinter import *

# Função de cálculo
def calculando():
    try:
        expressao = Digite.get()
        total = eval(expressao)
        resultado.config(text=total)
        resultado.place(x=170, y=64, anchor='center')  # Exibe o resultado
        Digite.delete(0, END)  # Limpa o campo de entrada
        if total > 100000000:
            raise ValueError
    except:
        resultado.config(text='Erro!')
        resultado.place(x=170, y=64, anchor='center')
        Digite.delete(0, END)

# Adiciona um número no display e esconde o resultado
def pegar_numero(n):
    resultado.place_forget()  # Esconde o resultado ao digitar novamente
    Digite.insert(END, n)

# Adiciona o símbolo de soma, evitando duplicação de operadores
def pegar_soma():
    expressao = Digite.get()
    Digite.insert(END, '+')

def limpando():
    Digite.delete(0, END)
    resultado.place_forget()


# Criando a janela
janela = Tk()
janela.geometry("340x400")
janela.title("Calculadora")

# Campo de entrada
Digite = Entry(janela, font=("Arial", 40), width=10, justify='center', bg='white')
Digite.pack(padx=10, pady=20, ipady=10)

# Resultado (começa escondido)
resultado = Label(janela, text='', font=('Arial', 40), background='white')
resultado.place_forget()  # Esconde o resultado no início

# Criando os botões numéricos
numeros = [
    (1, 50, 200), (2, 120, 200), (3, 190, 200),
    (4, 50, 250), (5, 120, 250), (6, 190, 250),
    (7, 50, 300), (8, 120, 300), (9, 190, 300),
    (0, 120, 350)
]

for num, x, y in numeros:
    Button(janela, text=num, width=8, height=2, command=lambda n=num: pegar_numero(n)).place(x=x, y=y, anchor='center')

# Botão de soma
Button(janela, text='+', width=8, height=2, command=pegar_soma).place(x=190, y=350, anchor='center')

# Botão calcular
Button(janela, text='Calcular', padx=10, pady=10, command=calculando).place(x=250, y=340)

# Botão Limpar

limpar = Button(janela, text='Limpar', width=8, height=2, command=limpando)
limpar.place(x=50, y=350, anchor='center')

janela.mainloop()
