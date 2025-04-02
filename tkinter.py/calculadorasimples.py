from tkinter import *
import time

def soma():
    try:
        n1 = int(Digite.get())
        n2 = int(Digite2.get())

        resultado = (n1 + n2)
        exibir_resultado['text'] = resultado
        erro_tratamento.config(text='')

    except ValueError:
        erro = 'Ocorreu um erro, digite novamente!'
        erro_tratamento['text'] = erro
        exibir_resultado.config(text='')


janela = Tk()
# Título
janela.title('Calculadora')

# Tamanho da janela
janela.geometry('400x400')

# Frame (Centralizar)
ajuste = Frame(janela)
ajuste.pack(padx=10, pady=10, expand=True)


# Boas vindas
Label(ajuste, text='Seja bem vindo!').pack(padx=0, pady=0)
Label(ajuste, text='Digite dois números para somar').pack(padx=10, pady=10)


# Entrada 1

Digite = Entry(ajuste)
Digite.pack(padx=0, pady=0)

# Entrada 2
Digite2 = Entry(ajuste)
Digite2.pack()

# Botão
Button(ajuste, text='Calcular', command=soma, padx=10, pady=10).pack(padx=10, pady=10)

# Exibir Resultado

exibir_resultado = Label(ajuste, text='')
exibir_resultado.pack(padx=5, pady=5)

# Erro
erro_tratamento = Label(ajuste, text='')
erro_tratamento.pack(padx=0, pady=0)

janela.mainloop()