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
from subprocess import check_output, run, PIPE, STDOUT, CalledProcessError


def verificar_instalacao_python(elemento: tk.Entry) -> str:
    '''
    ## Verifica a Existência do Python
    ---
    Verifica se o Python está instalado na máquina local
    ### Atribuições
    ---
    1. Verifica se o Python está instalado
    2. Retorna ao usuário se o está instalado na caixa grande de texto\n
    parâmetros:
    elemento : tk.Entry (widget caixa de texto grande)
    return: str
    '''
    cmd_verificar_python = "python --version"
    try:
        texto_de_saida = check_output(args=cmd_verificar_python,
                                      shell=False,
                                      stderr=STDOUT,
                                      text=True)
        # Enviar mensagem final positiva
        elemento.insert(
            tk.END, f"Excelente!\nO Python já está instalado! \n{texto_de_saida}")
        elemento.update_idletasks()
        return texto_de_saida
    except CalledProcessError as er:
        if er == 1:
            caixa_de_mensagem_erro(
                "Erro!", "Oh NO...\nPelo visto, você deverá instalar o Python...")
        else:
            raise


def verificar_instalacao_git(elemento: tk) -> str:
    '''
    ## Verifica a Existencia do Git
    ---
    Faz a verificação do programa Git na máquina local.
    ### Atribuições
    ---
    1. Roda o comando no terminal do powershell para verificar o git
    2. Retorna ao usuário se o está instalado na caixa grande de texto,\n
    caso contrário, executa a instalação pela função: __instalacao_git.
    parâmetros:
    elemento : tkinter (widget caixa de texto grande)
    return: str
    '''
    cmd_verificar_git = "git --version"
    # Envia o status da execução da função para a caixa de texto grande
    elemento.insert(
        tk.END, "\nCalma, não criêmos Pânico!\nEstou verificando se o Git está instalado...")
    elemento.update_idletasks()

    from subprocess import CalledProcessError
    # Execute o comando de verificação do Git
    try:
        texto_de_saida = check_output(args=cmd_verificar_git,
                                      shell=False,
                                      stderr=STDOUT,
                                      text=True)
        # Enviar mensagem final positiva
        elemento.insert(
            tk.END, f"\n\nExcelente!\nO Git já está instalado! \n{texto_de_saida}")
        elemento.update_idletasks()
        return texto_de_saida
    except CalledProcessError as er:
        if er == 1:
            # Executa instalação do programa Git
            __instalacao_git(elemento=elemento)
        else:
            # Envia uma janela com mensagem de erro na tela
            caixa_de_mensagem_erro(
                "Erro", "Ocorreu um erro ao executar a operação de instalação do programa Git.")
            raise


def criar_ambiente_virtual(caminho_pasta: str, elemento: tk):
    '''
    ## Cria o Ambienten Virtual

    ### Atribuições
    1. Criar uma pasta chamada .env que será o novo ambiente virtual do projeto python.\n
    2. Obtendo como parâmetro o elemento e atualizando o status no texto de saída

    parâmetros:
        caminho_arquivo : str
        elemento : scrolledtext.ScrolledText (widget caixa de texto grande)
    return: void
    '''
    cmd = "python -m venv .env"
    try:
        # Adicioanar mensagem ao quadro principal
        elemento.insert(
            tk.END, "\nTenha paciência...\nEstou criando o ambiente virtual...\n")
        elemento.update_idletasks()

        run(cmd, cwd=caminho_pasta, check=True, stdout=PIPE, stderr=PIPE)

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
            "Erro", "Ocorreu um erro ao executar a operação de criar pasta env.")


def criar_arquivo_gitignore(caminho_projeto: str, elemento: tk):
    '''
    ## Cria Arquivo ´.gitignore´

    ### Atribuições
    1. Criar um arquivo chamado .gitignore que impede que certas pastas sejam enviadas para o repoiótrio no GigHub.\n
    2. Obtendo como parâmetro o elemento e atualizando o status no texto de saída

    parâmetros:
        caminho_arquivo : str
        elemento : scrolledtext.ScrolledText (widget caixa de texto grande)
    return: void'''
    conteudo_gitignore = '''
    # Arquivo .gitignore gerado automaticamente

    # Ignorar arquivos de configuração
    config.json

    # Ignorar a pasta de dependências
    /node_modules

    # Ignorar arquivos de compilação
    /build
    /dist
    /venv
    venv
    '''
    from os.path import join, exists

    caminho_pasta = join(caminho_projeto, '.gitignore')
    if not exists(caminho_pasta):
        with open(caminho_pasta, 'w') as arquivo_git:
            arquivo_git.write(conteudo_gitignore)
            elemento.insert(
                tk.END, f"O arquivo .gitignore foi criado com sucesso!")
            elemento.update_idletasks()
    else:
        elemento.insert(tk.END, f"O arquivo .gitignore JÁ EXISTE!")
        elemento.update_idletasks()


def __instalacao_git(elemento: tk):
    '''
    ## Executa a Instalação do Git
    ---
    Faz a instalação do programa Git na máquina local.
    ### Atribuições
    ---
    1. Roda o comando no terminal do powershell para instalar o git
    2. Retorna ao usuário se o está instalado na caixa grande de texto\n
    parâmetros:
    elemento : tkinter (widget caixa de texto grande)
    return: void
    '''
    # Enviar mensagem negativa para a caixa grande
    elemento.insert(
        tk.END, "\n\nOpa!\nO GIT NÃO ESTÁ INSTALADO!\nPode deixar que eu instalo...\n\n")
    elemento.update_idletasks()

    # Instalação do GIT
    CMD_INSTALAR_GIT = "Set-ExecutionPolicy Bypass -Scope Process -Force;Install-Module -Name Posh-Git;"
    TERMINAL = "powershell.exe"  # Caminho do executável do power shell
    try:
        # O -Comand informa que o comando seguinte não é um comando nativo do powershell
        run([TERMINAL, "-Command", CMD_INSTALAR_GIT],
            check=True,
            stdout=PIPE,
            stderr=PIPE)

        # Envi
        elemento.insert(tk.END, 'O Git foi instalado com sucesso!\n')
        elemento.update_idletasks()
    except CalledProcessError as e:
        caixa_de_mensagem_erro(titulo="Erro!",
                               corpo_mensagem=f"Erro ao instalar o Git {e}")


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
        # Comando para mudar as politicas, permitindo execução de scripts via editor de código
        comando = shell.ShellExecuteEx(lpVerb=privilegios,
                                       lpFile=terminal,
                                       lpParameters=cmd)

        if comando == 1:
            # Adiciona a mensagem de sucesso ao quadro principal
            elemento.insert(
                tk.END, "\n\nPronto!\nPolíticas de execução ativadas!\n")
            elemento.update_idletasks()
    except PermissionError:
        caixa_de_mensagem_erro(
            "Erro!", f"Sinto muito, mas você não tem permissão pra fazer isso...")
    except OSError:
        caixa_de_mensagem_erro(
            "Erro!", f"Ai, é o seu sistema operacional...")


def instancias_do_projeto(caminho_do_projeto: str, *elementos: tk):
    '''
    ## Instancias das Funções
    ---
    Instância uma sequencia de tarefas para criar o projeto 
    com base no caminho do arquivo e na seqência de elementos.
    ---
    parâmetros:
        caminho_do_projeto : str -> caminho da pasta do projeto
        elementos : list[tkinter] -> elemento qualquer que vai receber ou que vai enviar 
    return void
    '''
    if caminho_do_projeto == "" or caminho_do_projeto is None:
        caixa_de_mensagem_erro(
            'Claro que deu erro!', 'Informe o caminho da pasta do projeto, pelo amor...!')
    elif not verificar_instalacao_python(elemento=elementos[0]):
        caixa_de_mensagem_erro(
            'Erro!', 'O python não está instalado! \nSiga as recomendações no repositório do projeto.')
    else:
        criar_ambiente_virtual(caminho_pasta=caminho_do_projeto,
                               elemento=elementos[0])
        # Implementação:
        # Preciso verificar se existe uma pasta chamada .env antes de criar
        ativar_politicas_execucao(elemento=elementos[0])

        # Instalação do programa Git
        if elementos[1] == 1:
            verificar_instalacao_git(elemento=elementos[0])
        criar_arquivo_gitignore(
            caminho_projeto=caminho_do_projeto, elemento=elementos[0])


def selecionar_caminho_pasta(elemento: tk.Entry) -> str:
    '''
    ## Selecionar Caminho Pasta
    ---
    Seleciona caminho da pasta para criar um novo novo projeto
    ### Atribuições
    1. Permite que o usuário selecione a pasta específica que ele deseja criar o projeto.
    2. Retorna o caminho da pasta para o usuário.
    ---
    parâmetros:
        elemento : tkinter.Entry

    return pasta_selecionada : str
    '''
    try:
        pasta_selecionada = askdirectory()
        if pasta_selecionada is not None or pasta_selecionada == "":
            elemento.delete(0, tk.END)  # Limpa o conteúdo atual do Entry
            # Insere o novo caminho no Entry
            elemento.insert(0, pasta_selecionada)
    except FileNotFoundError:
        caixa_de_mensagem_erro(
            'Claro que deu erro!', 'Informe o caminho da pasta do projeto válido, pelo amor...!')
    except PermissionError:
        caixa_de_mensagem_erro(
            "Erro!", f"Sinto muito, mas você não tem permissão pra fazer isso...")
    except OSError:
        caixa_de_mensagem_erro(
            "Erro!", f"Ai, é o seu sistema operacional...")


def main():
    '''# Programa Principal'''
    # Criar Janela principal
    janela = tk.Tk()
    janela.title("Criar Projeto Python")
    janela.resizable(False, False)

    # Frames
    quadro_mostrar_pasta = tk.Frame(janela)
    quadro_mostrar_pasta.pack(side=tk.TOP, padx=10)
    quadros = tk.Frame(janela)
    quadros.pack(padx=20, pady=10)

    # Obter o caminho da pasta do novo projeto
    mostrar_texto(titulo="Informe a pasta do novo projeto:",
                  quadro=quadro_mostrar_pasta)
    elemento_caminho_pasta = entrada_de_dados(largura=50,
                                              quadro=quadro_mostrar_pasta)
    elemento_caminho_pasta.pack(side=tk.LEFT, padx=10)
    botao_procurar_pasta = clicar_no_botao(titulo="Procurar Pasta...",
                                           comando=lambda: selecionar_caminho_pasta(
                                               elemento=elemento_caminho_pasta),
                                           quadro=quadro_mostrar_pasta)
    botao_procurar_pasta.pack(side=tk.LEFT)

    # Variável de estado - caixa de selecao
    mostrar_texto(titulo="Quais programas você deseja instalar?",
                  quadro=quadros)
    estado_caixa_selecao_git = tk.IntVar()
    # Selecionar instaladores - falta incluir função na caixa de seleção
    caixa_de_selecao(titulo='Git',
                     comando=None,
                     variavel=estado_caixa_selecao_git,
                     quadro=quadros)

    # Visualização do processo de instrâcia do novo projeto
    texto_de_saida = caixa_de_texto_grande(quadro=quadros)

    # Enviar dados do projeto ou sair
    clicar_no_botao_expassado(titulo="Cancelar",
                              largura=5,
                              altura=5,
                              comando=janela.destroy,
                              quadro=janela)
    clicar_no_botao_expassado(titulo="Enviar",
                              largura=5,
                              altura=5,
                              comando=lambda: instancias_do_projeto(elemento_caminho_pasta.get(),
                                                                    texto_de_saida,
                                                                    estado_caixa_selecao_git.get()),
                              quadro=janela)

    janela.mainloop()


if __name__ == "__main__":
    main()
