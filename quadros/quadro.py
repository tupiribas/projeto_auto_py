'''Aqui encontramos frames personalizados e centralizados, evita muito código no arquivo principal'''

import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


def caixa_de_texto_grande(quadro: tk.Tk) -> ScrolledText:
    '''Uma caixa de texto grande que possibilita escrever e enviar mensagens dew status'''
    texto_de_saida = ScrolledText(
        quadro,
        wrap=tk.WORD,
        width=40,
        height=10)
    texto_de_saida.pack(pady=15)
    return texto_de_saida


def mostrar_texto(titulo: str, quadro: tk.Tk) -> tk.Label:
    '''Uma especie de label personalizado'''
    texto = tk.Label(
        quadro, text=titulo)
    texto.pack()
    return texto


def entrada_de_dados(largura: int, quadro: tk.Tk):
    '''Apenas um input personalizado'''
    dados = tk.Entry(quadro, width=largura)
    dados.pack()
    return dados


def clicar_no_botao(titulo: str, comando, quadro: tk.Tk) -> tk.Button:
    '''Botão de tamanho normal personalizado'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack()
    return botao


def clicar_no_botao_expassado(titulo: str, comando, quadro: tk.Tk, largura: int = None, altura: int = None):
    '''Botão com espaçamento 100% na horizontal personalizado'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack(side='right', ipadx=largura,
               ipady=altura, expand=True, fill='none')
    return botao


def caixa_de_mensagem_informativa(titulo: str, corpo_mensagem: str):
    '''Janela informativa personalizada'''
    messagebox.showinfo(title=titulo, message=corpo_mensagem)


def caixa_de_mensagem_erro(titulo: str, corpo_mensagem: str):
    '''Janela de erro personalizada'''
    messagebox.showerror(title=titulo, message=corpo_mensagem)
