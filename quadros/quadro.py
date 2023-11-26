'''Aqui encontramos frames personalizados e centralizados, evita muito código no arquivo principal'''
from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter.ttk import Checkbutton
from tkinter import WORD
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo, showerror


def caixa_de_texto_grande(quadro: Tk) -> ScrolledText:
    '''Uma caixa de texto grande que possibilita escrever e enviar mensagens dew status'''
    texto_de_saida = ScrolledText(
        quadro,
        wrap=WORD,
        width=40,
        height=10)
    texto_de_saida.pack(pady=15)
    return texto_de_saida


def mostrar_texto(titulo: str, quadro: Tk) -> Label:
    '''Uma especie de label personalizado'''
    texto = Label(
        quadro, text=titulo)
    texto.pack()
    return texto


def entrada_de_dados(largura: int, quadro: Tk):
    '''Apenas um input personalizado'''
    dados = Entry(quadro, width=largura)
    dados.pack()
    return dados


def clicar_no_botao(titulo: str, comando, quadro: Tk) -> Button:
    '''Botão de tamanho normal personalizado'''
    botao = Button(
        quadro, text=titulo, command=comando)
    botao.pack()
    return botao


def clicar_no_botao_expassado(titulo: str, comando, quadro: Tk, largura: int = None, altura: int = None):
    '''Botão com espaçamento 100% na horizontal personalizado'''
    botao = Button(
        quadro, text=titulo, command=comando)
    botao.pack(side='right', ipadx=largura,
               ipady=altura, expand=True, fill='none')
    return botao


def caixa_de_mensagem_informativa(titulo: str, corpo_mensagem: str):
    '''Janela informativa personalizada'''
    showinfo(title=titulo, message=corpo_mensagem)


def caixa_de_mensagem_erro(titulo: str, corpo_mensagem: str):
    '''Janela de erro personalizada'''
    showerror(title=titulo, message=corpo_mensagem)


def caixa_de_selecao(titulo, comando, quadro) -> Checkbutton:
    caixa = Checkbutton(quadro,
                       text=titulo,
                       command=comando,
                       onvalue='agree',
                       offvalue='disagree').pack()
    return caixa
