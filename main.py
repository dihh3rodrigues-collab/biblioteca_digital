import os

PASTA = "documentos"

if not os.path.exists(PASTA):
    os.makedirs(PASTA)


def listar_documentos():
    arquivos = os.listdir(PASTA)

    print("\n=== DOCUMENTOS ===")

    if len(arquivos) == 0:
        print("Nenhum documento encontrado.")
    else:
        for arquivo in arquivos:
            print("-", arquivo)


def adicionar_documento():
    nome = input("Nome do documento: ")

    caminho = os.path.join(PASTA, nome)

    with open(caminho, "w") as arquivo:
        arquivo.write("Novo documento")

    print("Documento criado com sucesso!")


def renomear_documento():
    antigo = input("Nome atual: ")
    novo = input("Novo nome: ")

    caminho_antigo = os.path.join(PASTA, antigo)
    caminho_novo = os.path.join(PASTA, novo)

    if os.path.exists(caminho_antigo):
        os.rename(caminho_antigo, caminho_novo)
        print("Documento renomeado!")
    else:
        print("Documento não encontrado!")


def remover_documento():
    nome = input("Nome do documento: ")

    caminho = os.path.join(PASTA, nome)

    if os.path.exists(caminho):
        os.remove(caminho)
        print("Documento removido!")
    else:
        print("Documento não encontrado!")


while True:

    print("\n===== BIBLIOTECA DIGITAL =====")
    print("1 - Listar documentos")
    print("2 - Adicionar documento")
    print("3 - Renomear documento")
    print("4 - Remover documento")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_documentos()

    elif opcao == "2":
        adicionar_documento()

    elif opcao == "3":
        renomear_documento()

    elif opcao == "4":
        remover_documento()

    elif opcao == "5":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")