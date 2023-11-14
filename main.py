import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter.filedialog import askdirectory

from quadros.quadro import (
    mostrar_texto, clicar_no_botao, entrada_de_dados, clicar_no_botao_expassado)

# Condições:
#   1. Já tenha instalado o python na máquina dele


# def verificar_venv_instalado():
#     try:
#         import venv
#         msg = 'O módulo venv está instalado na sua máquina.'
#     except ImportError:
#         msg = "O módulo venv NÃO está instalado na sua máquina."
#     messagebox.showinfo('Verificação do venv', msg)

def criar_arquivo_venv(caminho_arquivo, entidade: scrolledtext.ScrolledText):
    import subprocess
    comando = "python -m venv venv"
    try:
        # Adicioanar mensagem ao quadro principal
        entidade.insert(tk.END, "Iniciando a criação do ambiente virtual...\n")
        entidade.update_idletasks()

        subprocess.run(comando, cwd=caminho_arquivo, check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Adiciona a mensagem de sucesso ao quadro principal
        entidade.insert(tk.END, "Ambiente virtual criado com sucesso!\n")
        entidade.update_idletasks()
        messagebox.showinfo(
            "Sucesso!", "Ambiente virtual criado com sucesso!")
    except subprocess.CalledProcessError:
        messagebox.showerror(
            "Erro", "Ocorreu um erro ao executar a operação de executar o venv.")


def instanciar_projeto(caminho_do_projeto, entidades: list[tk.Tk]):
    criar_arquivo_venv(caminho_arquivo=caminho_do_projeto,
                       entidade=entidades[0])


def buscar_caminho_pasta(elemento: tk.Entry) -> str:
    '''Encontrar caminho da pasta do novo projeto'''
    try:
        pasta_selecionada = askdirectory()
        elemento.delete(0, tk.END)  # Limpa o conteúdo atual do Entry
        elemento.insert(0, pasta_selecionada)  # Insere o novo caminho no Entry
    except FileExistsError as e:
        print(f"Ocorreu um erro ao ecnotrar erro: {e}")
    return pasta_selecionada


def main():
    '''Programa Principal'''
    # Criar Janela principal
    janela = tk.Tk()
    janela.title("Criar Projeto")

    quadro = tk.Frame(janela)
    quadro.pack(padx=20, pady=20)

    # Obter o caminho da pasta do novo projeto
    mostrar_texto(
        "1. Informe o local do arquivo onde localiza a pasta do novo projeto:", quadro)
    entidade_caminho_pasta = entrada_de_dados(50, quadro)
    clicar_no_botao(
        "Procurar Pasta...", lambda: buscar_caminho_pasta(entidade_caminho_pasta), quadro)

    # Preparar pasta para projeto base python
    texto_de_saida = scrolledtext.ScrolledText(
        janela, wrap=tk.WORD, width=40, height=10)
    texto_de_saida.pack()

    # Enviar dados do projeto ou sair
    clicar_no_botao_expassado(
        titulo="Cancelar", largura=5, altura=5, comando=janela.destroy, quadro=janela)
    clicar_no_botao_expassado(
        titulo="Enviar", largura=5, altura=5,
        comando=lambda: instanciar_projeto(entidade_caminho_pasta.get(), [texto_de_saida]), quadro=janela)

    janela.mainloop()


if __name__ == "__main__":
    main()
    # verificar_venv_instalado()
