'''Aqui encontramos frames personalizados e centralizados, evita muito código no arquivo principal'''

import tkinter as tk
from tkinter import messagebox, scrolledtext


def caixa_de_texto_grande(janela: tk.Tk) -> scrolledtext.ScrolledText:
    '''Uma caixa de texto grande'''
    texto_de_saida = scrolledtext.ScrolledText(
        janela, wrap=tk.WORD, width=40, height=10)
    texto_de_saida.pack()
    return texto_de_saida


def mostrar_texto(titulo: str, quadro: tk.Tk):
    '''Uma especie de label personalizado'''
    texto = tk.Label(
        quadro, text=titulo)
    texto.pack()


def entrada_de_dados(largura: int, quadro: tk.Tk):
    '''Apenas um input personalizado'''
    dados = tk.Entry(quadro, width=largura)
    dados.pack(side='top')
    return dados


def clicar_no_botao(titulo: str, comando, quadro: tk.Tk):
    '''Botão de tamanho normal personalizado'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack()


def clicar_no_botao_expassado(titulo: str, comando, quadro: tk.Tk, largura: int = None, altura: int = None):
    '''Botão com espaçamento 100% na horizontal personalizado'''
    botao = tk.Button(
        quadro, text=titulo, command=comando)
    botao.pack(side='right', ipadx=largura,
               ipady=altura, expand=True, fill='none')


def caixa_de_mensagem_informativa(titulo: str, corpo_mensagem: str):
    '''Janela informativa personalizada'''
    messagebox.showinfo(title=titulo, message=corpo_mensagem)


def caixa_de_mensagem_erro(titulo: str, corpo_mensagem: str):
    '''Janela de erro personalizada'''
    messagebox.showerror(title=titulo, message=corpo_mensagem)
