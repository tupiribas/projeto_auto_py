'''Arquivo principal'''
# Frames
from quadros.quadro import (
    mostrar_texto, clicar_no_botao, entrada_de_dados,
    clicar_no_botao_expassado, caixa_de_mensagem_informativa,
    caixa_de_mensagem_erro, caixa_de_texto_grande, caixa_de_selecao)

# Bibliotecas principais do projeto
import tkinter as tk
from tkinter.filedialog import askdirectory

# Utilitário
import win32comext.shell.shell as shell
from win32event import error
from tkinter import StringVar

# Largura padrão para todos os elementos do quadro pack chamados
LARGURA_VERTICAL_PADRAO = 15


def verificar_instacao_python(elemento: tk.Entry) -> bool:
    '''
    ## Verificar Instalação do Python
    ---
    Verifica se o Python está instalado
    ### Atribuições
    ---
    1. Executa o Power Shell como ADM da máquina;
    2. Verifica se o Python está instalado
    3. Retorna ao usuário se o está instalado na caixa grande de texto\n
    parâmetros:
    elemento : tk.Entry (widget caixa de texto grande)
    return: void
    '''
    cmd = "python --version"
    privilegios = "runas"  # Aumentar o nível de privilégios
    terminal = "powershell.exe"  # Caminho do executável do power shell

    try:
        execute = shell.ShellExecuteEx(
            lpVerb=privilegios, lpFile=terminal, lpParameters=cmd)
        if not execute:
            # Adicioanar mensagem ao quadro principal
            elemento.insert(tk.END, 'O python NÃO está instalado!\n')
            elemento.update_idletasks()
    except error:
        caixa_de_mensagem_erro(
            "Erro!", "Erro ao verificar se o Python está instalado.")
    return True


def criar_ambiente_virtual(caminho_arquivo: str, elemento: tk):
    '''
    ## Criando o Ambienten Virtual

    ### Atribuições
    1. Criar uma pasta chamada .env que será o novo ambiente virtual do projeto python.\n
    2. Obtendo como parâmetro o elemento e atualizando o status no texto de saída

    parâmetros:
        caminho_arquivo : str
        elemento : scrolledtext.ScrolledText (widget caixa de texto grande)
    return: void
    '''
    from subprocess import run, PIPE, CalledProcessError

    cmd = "python -m venv .env"
    try:
        # Adicioanar mensagem ao quadro principal
        elemento.insert(
            tk.END, "Tenha paciência...\nEstou criando o ambiente virtual...\n")
        elemento.update_idletasks()

        run(cmd, cwd=caminho_arquivo, check=True, stdout=PIPE, stderr=PIPE)

        # Adiciona a mensagem de sucesso ao quadro principal
        elemento.insert(
            tk.END, "\nPronto!\nAmbiente virtual criado com sucesso!\n")
        elemento.update_idletasks()

        # Envia mensagem de sucesso na tela
        caixa_de_mensagem_informativa(
            "Sucesso!", "Ambiente virtual criado com sucesso!")
    except CalledProcessError:
        # Envia mensagem de erro na tela
        caixa_de_mensagem_erro(
            "Erro", "Ocorreu um erro ao executar a operação de criar pasta venv.")


def ativar_politicas_execucao(elemento: tk):
    '''## Politicas Execução no Windows
    Comando executado no shell como adm:\n
    >>> "Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy RemoteSigned -Force"

    ### Atribuições
    1. Permite que o usuário possa executar a ativação do ambiente virutal (.env).
    2. Obtendo como parâmetro o elemento e atualizando o status no texto de saída

    parâmetro:
        elemento : scrolledtext.ScrolledText (widget caixa de texto grande)
    return: void
    '''
    # Adicioanar mensagem ao quadro principal
    elemento.insert(
        tk.END, "\nAtivando políticas de execução")
    elemento.update_idletasks()

    cmd = "Set-ExecutionPolicy -Scope LocalMachine -ExecutionPolicy RemoteSigned -Force"
    privilegios = "runas"  # Aumentar o nível de privilégios
    terminal = "powershell.exe"  # Caminho do executável do power shell

    try:
        shell.ShellExecuteEx(lpVerb=privilegios,
                             lpFile=terminal, lpParameters=cmd)
    except error:
        caixa_de_mensagem_erro(
            "Erro!", f"Erro ao ativar políticas de execução.")
    # Adiciona a mensagem de sucesso ao quadro principal
    elemento.insert(
        tk.END, "\n\nPronto!\nPolíticas de execução ativadas!\n")
    elemento.update_idletasks()


def instancias_do_projeto(caminho_do_projeto: str, *elementos: tk):
    '''
    ## Instancias
    ---
    Instância uma sequencia de tarefas para criar o projeto 
    com base no caminho do arquivo.
    ---
    parâmetros:
        caminho_do_projeto : str -> caminho da pasta do projeto
        elementos : list[tkinter] -> elemento qualquer que vai receber ou que vai enviar 
    return void
    '''
    if not verificar_instacao_python(elemento=elementos[0]):
        # Manda mensagem de erro
        caixa_de_mensagem_erro(
            'Erro!', 'O python não está instalado! \nSiga as recomendações no repositório do projeto.')
    # criar_ambiente_virtual(caminho_arquivo=caminho_do_projeto,
    #                        elemento=elementos[0])
    # ativar_politicas_execucao(elemento=elementos[0])
    caixa_de_mensagem_informativa('teste', elementos[1])


# def verificar_instalacao_git():
#     # aqui você precisa acessar o estado da caixa de seleção do Git
#     git_selecionado = estado
#     if git_selecionado:
#         # Coloque aqui o código para instalar o Git via terminal
#         # Por exemplo, se estiver usando o Windows:
#         cmd_instalacao_git = "seu_comando_de_instalacao_do_git"
#         # Execute o comando para instalar o Git
#         try:
#             # Use subprocess ou outras bibliotecas para executar comandos no terminal
#             # subprocess.run(cmd_instalacao_git, shell=True) - exemplo de como usar subprocess
#             pass  # Substitua este pass pelo código de instalação real
#         except Exception as e:
#             print(f"Erro ao instalar o Git: {e}")


def selecionar_caminho_pasta(elemento: tk.Entry) -> str:
    '''
    ## Selecionar Caminho Pasta
    ---
    Seleciona caminho da pasta para criar um novo novo projeto
    ### Atribuições
    ---
    parâmetros:
        elemento : tkinter.Entry

    return pasta_selecionada : str
    '''
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
    janela.title("Criar Projeto Python")

    # Cria um quadro (frame) dentro da janela princial
    quadro = tk.Frame(janela)
    quadro.pack(padx=20, pady=20)

    # Obter o caminho da pasta do novo projeto
    mostrar_texto(titulo="Informe a pasta do novo projeto:",
                  quadro=quadro)
    elemento_caminho_pasta = entrada_de_dados(largura=50, quadro=quadro)
    clicar_no_botao(titulo="Procurar Pasta...",
                    comando=lambda: selecionar_caminho_pasta(
                        elemento=elemento_caminho_pasta),
                    quadro=quadro)

    # Selecionar instaladores - falta incluir função na caixa de seleção
    caixa_selecao_git = caixa_de_selecao(titulo='Git',
                                         comando=None,
                                         quadro=quadro)

    # Visualização do processo de instrâcia do novo projeto
    texto_de_saida = caixa_de_texto_grande(quadro=quadro)

    # Enviar dados do projeto ou sair
    clicar_no_botao_expassado(
        titulo="Cancelar", largura=5, altura=5, comando=janela.destroy, quadro=janela)
    clicar_no_botao_expassado(
        titulo="Enviar", largura=5, altura=5,
        comando=lambda: instancias_do_projeto(
            elemento_caminho_pasta.get(),
            texto_de_saida,
            caixa_selecao_git), quadro=janela)

    janela.mainloop()


if __name__ == "__main__":
    main()
