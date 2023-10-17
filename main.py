from tkinter import *

janela = Tk()
janela.geometry('320x145+500+150')
janela.title("Tkinter Calculator")

def calcular():
    entradaNumeros = entrada.get()
    result = str(round(eval(entradaNumeros), 10))
    entrada.delete(0, 'end')  # Remove o valor anterior
    entrada.insert(0, result)  # Insere o resultado

def on_click(text):
   entrada.insert('end',text)

def limpar():
    entrada.delete(0,'end')

entrada = Entry(
    master = janela,
    width = 20,
    font = ('Arial', 20)
)

entrada.grid(row=0, columnspan=4)

botao0 = Button(
    master = janela,
    text = '0',
    width=10,
    command=lambda:on_click('0')
)
botao0.grid(row=4, column=1)
botao1 = Button(
    master = janela,
    text = '1',
    width=10,
    command=lambda:on_click("1")
)
botao1.grid(row=3, column=0)
botao2 = Button(
    master = janela,
    text = '2',
    width=10,
    command=lambda:on_click("2")
)
botao2.grid(row=3, column=1)
botao3 = Button(
    master = janela,
    text = '3',
    width=10,
    command=lambda:on_click("3")
)
botao3.grid(row=3, column=2)
botao4 = Button(
    master = janela,
    text = '4',
    width=10,
    command=lambda:on_click("4")
)
botao4.grid(row=2, column=0)
botao5 = Button(
    master = janela,
    text = '5',
    width=10,
    command=lambda:on_click("5")
)
botao5.grid(row=2, column=1)
botao6 = Button(
    master = janela,
    text = '6',
    width=10,
    command=lambda:on_click("6")
)
botao6.grid(row=2, column=2)
botao7 = Button(
    master = janela,
    text = '7',
    width=10,
    command=lambda:on_click("7")
)
botao7.grid(row=1, column=0)
botao8 = Button(
    master = janela,
    text = '8',
    width=10,
    command=lambda:on_click("8")
)
botao8.grid(row=1, column=1)
botao9 = Button(
    master = janela,
    text = '9',
    width=10,
    command=lambda:on_click("9")
)
botao9.grid(row=1, column=2)
botaoC = Button(
    master = janela,
    text = 'c',
    width=10,
    command=lambda:limpar()
)
botaoC.grid(row=4, column=0)
botaoIgual = Button(
    master = janela,
    text = '=',
    width=10,
    command=calcular
)
botaoIgual.grid(row=4, column=2)
botaoMenos = Button(
    master = janela,
    text = '-',
    width=10,
    command=lambda:on_click("-")
)
botaoMenos.grid(row=1, column=3)
botaoMais = Button(
    master = janela,
    text = '+',
    width=10,
    command=lambda:on_click("+")
)
botaoMais.grid(row=2, column=3)
botaoDividir = Button(
    master = janela,
    text = '/',
    width=10,
    command=lambda:on_click("/")
)
botaoDividir.grid(row=3, column=3)
botaoMultiplicar = Button(
    master = janela,
    text = '*',
    width=10,
    command=lambda:on_click("*")
)
botaoMultiplicar.grid(row=4, column=3)


janela.mainloop()