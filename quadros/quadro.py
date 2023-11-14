import tkinter as tk


def mostrar_texto(titulo: str, quadro: tk.Tk):
    texto = tk.Label(
        quadro, text=titulo)
    texto.pack()


def entrada_de_dados(largura: int, quadro: tk.Tk):
    dados = tk.Entry(quadro, width=largura)
    dados.pack(side='top')
    return dados


def clicar_no_botao(titulo: str, comando, quadro: tk.Tk):
    '''assdd'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack()


def clicar_no_botao_expassado(titulo: str, comando, quadro: tk.Tk, largura: int = None, altura: int = None):
    '''assdd'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack(side='right', ipadx=largura,
               ipady=altura, expand=True, fill='none')
