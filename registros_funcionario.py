class funcionario:
    cpf = ""
    nome = ""
    idade = -1
    cargo = ""


def menu_opcoes():
    print('Menu de opções')
    print('1. Cadastrar funcionário: ')
    print('2. Consultar um funcionário: ')
    print('3. Consultar todos os funcionários')
    print('4. Excluir um funcionário')
    print('5. Alterar dados de um funcionário')
    print('0. sair')
    op = int(input('Escolha umas das opções do menu (0-2): '))
    return op

def verificar_funcionario(lista_func, cpf): 
    for i in range(len(lista_func)):
        if lista_func[i].cpf == cpf: # verifica se o cpf informado é igual ao cpf da posição i
            return i #se o cpf existe, então retorna a sua posição na lista
    return -1 # retorna -1 para indicar que o cpf não foi encontrado    

def cadastrar_funcionario(lista_func):
    func = funcionario() #criando um registro de funcionario
    func.cpf = input('Informe o cpf do funcionario: ')
    achou = verificar_funcionario(lista_func, func.cpf)
    if achou == -1: # -1 indica que o cpf não não está cadastrado ainda
        func.nome = input('Informe o nome do funcionario: ')   
        func.idade = int(input('Informe a idade do funcionario: '))
        func.cargo = input('Informe o cargo do funcionario: ')
        lista_func.append(func)
        print("Funcionário cadastrado com sucesso!")
    else:
        print("O CPF informado já existe no cadastro!")

def  excluir_funcionario(lista_func):
    cpf = input("Digite o CPF do funcionário que deseja remover:")
    #chama a função para verificar se existe um funcionário com o cpf informado
    pos = verificar_funcionario(lista_func, cpf)
    if  pos != -1: 
        #se chegou neste ponto, é pq o CPF existe na lista na posição pos
        del lista_func[pos] # remove o funcionario da posição pos
        print("Funcionário removido com sucesso!")
    else:
        print("Funcionário não encontrado!")

def alterar_funcionario(lista_func):
    cpf = input("Digite o CPF do funcionário que deseja alterar:")
    pos = verificar_funcionario(lista_func,cpf)
    if pos != -1:
        lista_func[pos].nome = input("Digite um novo nome:")
        lista_func[pos].cargo = input("Digite o novo cargo:")
        lista_func[pos].idade = int(input("Digite a nova idade:"))
        print('Dados alterados com sucesso!')
    else:
        print("Funcionário não encontrado!")


def consultar_funcionario(lista_func,cpf_func):
    i = 0
    while i<len(lista_func):
        if lista_func[i].cpf == cpf_func:
            print(lista_func[i].nome + ' | ' + str(lista_func[i].idade)+ ' | ' + str(lista_func[i].cargo))        
        i+=1

def imprimir_funcionarios(lista_func):
    for i in range(len(lista_func)):
        print(lista_func[i].nome + ' | '+ lista_func[i].cpf + ' | ' + str(lista_func[i].cargo) + ' | ' + str(lista_func[i].idade))

def gravar_dados_arquivo(nome_arquivo, lista_func):
    arq = open(nome_arquivo, 'w')
    for i in range(len(lista_func)):
        arq.write(lista_func[i].cpf + ';' + lista_func[i].nome +';'+ str(lista_func[i].idade) +';'+  lista_func[i].cargo + "\n")
    arq.close()

def existe_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def carregar_dados_arquivos(nome_arquivo):
    arq = open(nome_arquivo, 'r')
    lista_funcionarios = []
    if existe_arquivo(nome_arquivo):
        for linha in arq:
            infos = linha.split(';')
            func = funcionario()
            func.cpf = infos[0]
            func.nome = infos[1]
            func.idade = infos[2]
            func.cargo = int(infos[3])
            lista_funcionarios.append(func)
        arq.close()
        return lista_funcionarios

def main():
    arquivo_func = './dados_funcionarios.txt'
    funcionarios = [] #guarda registros de funcionarios
    opcao = 1
    while opcao !=0:
        opcao = menu_opcoes() #apresenta o menu de opções e retorna
        if opcao ==1:
            print('Cadastrando um novo funcioanrio...')
            cadastrar_funcionario(funcionarios)
        elif opcao == 2:
            print('Consultando un novo funcionario...')
            cpf = input('Qual o cpf do funcionario que deseja: ')
            funcionarioss = carregar_dados_arquivos(arquivo_func)
            print(funcionarioss[0].cpf)
            consultar_funcionario(funcionarioss,cpf)
        elif opcao == 3:
            print("Imprimindo dados de todos os funcionários...")
            funcionarios = carregar_dados_arquivos(arquivo_func)
            imprimir_funcionarios(funcionarios)
        elif opcao == 4:
            print("Excluindo um funcionário...")
            excluir_funcionario(funcionarios)
        elif opcao == 5:
            print("Alterando os dados de um funcionario...")
            alterar_funcionario(funcionarios)
        elif opcao == 0:
            print('Obrigado por usar o nosso sistema!')
            if len(funcionarios) > 0:
                gravar_dados_arquivo(arquivo_func, funcionarios)
        else:
            print('opcao invalida')    

main()
