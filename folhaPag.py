funcionarios = {}
dadosFunc = []
maiorSal = 0
matriculaMaiorSalLiq = 0
maiorFaltas = 0
matriculaMaiorFaltas = 0

#Função para definir o funcionario com mais faltas e com maior salario (5 e 6 do menu) e suas respectivas matriculas

def maior(maior,maiorMatricula,x,y):
    if maior == 0:
        maior = x
        maiorMatricula = y
    else:
        if x > maior:
            maior = x
            maiorMatricula = y
    return maior, maiorMatricula

#Função para mostrar o menu inicial

def menuInicial():
        print('-'*65)
        print('1. INSERIR FUNCIONARIOS')
        print('2. REMOVER FUNCIONARIOS')
        print('3. FOLHA DE PAGAMENTO DE UM FUNCIONARIO')
        print('4. RELATÓRIO DE SALARIO BRUTO E LIQUIDO DE TODOS OS FUNCIONARIOS')
        print('5. INFORMAÇÕES DO FUNCIONARIO COM MAIOR SALARIO LIQUIDO')
        print('6. INFROMAÇÕES DO FUNCIONARIO COM MAIS FALTAS')
        print('QUALQUER OUTRO NUMERO PRA FECHAR O PROGRAMA')
        print('-'*65)
        menu = int(input('DIGITE O NUMERO DA OPÇÃO: '))
        return menu

#Função para definir o salario liquido com o salario bruto e seu respectivo imposto

def imposto(salBruto):
    if salBruto <= 2259.20:
        salLiq = salBruto
    elif salBruto <= 2828.65:
        salLiq = salBruto - 7.5*(salBruto/100)
    elif salBruto <= 3751.05:
        salLiq = salBruto - 15*(salBruto/100)
    elif salBruto <= 4664.68:
        salLiq = salBruto - 22.5*(salBruto/100)
    else:
        salLiq = salBruto - 27.5*(salBruto/100)
    return salLiq

#Função para definir o percentual de imposto

def percentualImposto(salBruto):
    if salBruto <= 2259.20:
        percImposto = 0
    elif salBruto <= 2828.65:
        percImposto = 7.5
    elif salBruto <= 3751.05:
        percImposto = 15
    elif salBruto <= 4664.68:
        percImposto = 22.5
    else:
        percImposto = 27.5
    return percImposto

#Função para definir o salario bruto com base na função do funcionario

def salariobruto(codFunc):
    salBruto=0
    salFixo=0
    if codFunc == 101:
        salFixo = 1500
        numVendas = int(input('Digite o valor total de vendas realizado pelo vendedor: '))
        salBruto = salFixo + 0.09*numVendas
    else:
        salFixo = float(input('Digite o salario fixo do funcionario: '))
        if salFixo < 2150 or salFixo > 6950:
            print('Este salário não é permitido para a função')
            while salFixo < 2150 or salFixo > 6950:
                salFixo = float(input('Digite o salario fixo do funcionario: '))
        salBruto = salFixo
    return salBruto, salFixo

menu = menuInicial()
while menu > 0 and menu < 7:
    if menu == 1:
        matricula = int(input('Digite o numero da matricula: '))
        if matricula < 0:
            print('A matricula não pode ser negativo')
            while matricula < 0:
                matricula = int(input('Digite o numero da matricula: '))
        nome = input('Digite o nome do funcionario: ')
        codFunc = int(input('Digite o codigo da função: '))
        if codFunc != 101 and codFunc != 102:
            print('Este código de função não é valido! Digite novamente')
            while codFunc != 101 and codFunc != 102:
                codFunc = int(input('Digite o codigo da função: '))
        salBruto, salFixo = salariobruto(codFunc)
        faltas = int(input('Digite o numero de faltas do funcionario: '))
        if faltas < 0 or faltas > 30:
            print('Numero de faltas invalido')
            while faltas < 0 or faltas > 30:
                faltas = int(input('Digite o numero de faltas do funcionario: '))

        # Definir o funcionario com mais faltas e sua matricula: 
        maiorFaltas, matriculaMaiorFaltas = maior(maiorFaltas, matriculaMaiorFaltas, faltas, matricula)
        salDesc = faltas*(salFixo/30)
        salBruto = salBruto - salDesc
        salLiq = imposto(salBruto)

        #Definir o funcionario com maior salario e sua matricula
        maiorSal, matriculaMaiorSalLiq = maior(maiorSal, matriculaMaiorSalLiq, salLiq, matricula)
        percImposto = percentualImposto(salBruto)

        #Salvando os dados em uma lista e depois em um dicionario

        dadosFunc.append(nome)
        dadosFunc.append(codFunc)
        dadosFunc.append(faltas)
        dadosFunc.append(salDesc)
        dadosFunc.append(salBruto)
        dadosFunc.append(percImposto)
        dadosFunc.append(salLiq)
        funcionarios[matricula] = dadosFunc
        print('-'*65)

        #Esse for é usado para printar os dados do funcionario cadastrado de maneira mais organizada, com o 'c' percorrendo os elementos da lista

        for c in range(len(dadosFunc)):
            if c == 0:
                print(f'Nome do Funcionario: {dadosFunc[c]}')
            elif c == 1:
                print(f'Codigo da Função do Funcionario: {dadosFunc[c]}')
            elif c == 2:
                print(f'Faltas do Funcionario: {dadosFunc[c]}')
            elif c == 3:
                print(f'Salario Descontado(Faltas): R${dadosFunc[c]:.2f}')
            elif c == 4:
                print(f'Salario Bruto do Funcionario: R${dadosFunc[c]:.2f}')
            elif c == 5:
                print(f'Percentual de Imposto do Funcionario: {dadosFunc[c]}%')
            elif c == 6:
                print(f'Salario Liquido do Funcionario: {dadosFunc[c]:.2f}')
        print('-'*65)
        dadosFunc = []

        #A variavel 'cont' é usada para o usuario poder se manter no menu selecionado caso deseje, abrindo o menu novamente apenas se o usuario quiser ir para outro menu

        cont = int(input('Digite 1 para cadastrar outro funcionario ou outro numero para voltar para o menu: '))
        if cont == 1:
            menu = 1
        else:
            menu = menuInicial()
    elif menu == 2:

        #Teste para saber se o dicionario que armazena os funcionario esta vazio, caso não esteja exclui o funcionario selecionado

        if funcionarios != {}:
            func = int(input('Digite o numero da matricula do funcionario que deseja remover: '))
            if func not in funcionarios.keys():
                print('Digite uma matricula valida: ')
                while func not in funcionarios.keys():
                    func = int(input('Digite o numero da matricula do funcionario que deseja remover: '))
            funcionarios.pop(func)
            print('O funcionario foi removido!')
            listaFunc = int(input('Digite 1 para ver a lista atualizda ou outro numero para fechar: '))
            if listaFunc == 1:

                #Esse for mostra todos os funcionario da lista de funcionarios atualizada

                for k in funcionarios.keys():
                    print('-'*65)
                    print(f'Matricula {k}')
                    for c in range(len(funcionarios[k])):
                        if c == 0:
                            print(f'Nome do Funcionario: {funcionarios[k][c]}')
                        elif c == 1:
                            print(f'Codigo da Função do Funcionario: {funcionarios[k][c]}')
                        elif c == 2:
                            print(f'Faltas do Funcionario: {funcionarios[k][c]}')
                        elif c == 3:
                            print(f'Salario Descontado(Faltas): R${funcionarios[k][c]:.2f}')
                        elif c == 4:
                            print(f'Salario Bruto do Funcionario: R${funcionarios[k][c]:.2f}')
                        elif c == 5:
                            print(f'Percentual de Imposto do Funcionario: {funcionarios[k][c]}%')
                        elif c == 6:
                            print(f'Salario Liquido do Funcionario: {funcionarios[k][c]:.2f}')
                    print('-'*65)
                cont = int(input('Digite 1 para remover outro funcionario ou outro numero para voltar para o menu: '))
                if cont == 1:
                    menu = 2
                else:
                    menu = menuInicial()

        #Caso a lista esteja vazia, o programa ja avisa o usuario e abre o menu

        else:
            print('A lista esta vazia! Adicione um funcionario.')
            menu = menuInicial()
    elif menu == 3:
        if funcionarios != {}:
            func = int(input('Digite o numero da matricula do funcionario que deseja mostrar: '))
            if func not in funcionarios.keys():
                print('Digite uma matricula valida!')
                while func not in funcionarios.keys():
                    func = int(input('Digite o numero da matricula do funcionario que deseja mostrar: '))
            for c in range(len(funcionarios[func])):
                print('-'*65)
                if c == 0:
                    print(f'Nome do Funcionario: {funcionarios[func][c]}')
                elif c == 1:
                    print(f'Codigo da Função do Funcionario: {funcionarios[func][c]}')
                elif c == 2:
                    print(f'Faltas do Funcionario: {funcionarios[func][c]}')
                elif c == 3:
                    print(f'Salario Descontado(Faltas): R${funcionarios[func][c]:.2f}')
                elif c == 4:
                    print(f'Salario Bruto do Funcionario: R${funcionarios[func][c]:.2f}')
                elif c == 5:
                    print(f'Percentual de Imposto do Funcionario: {funcionarios[func][c]}%')
                elif c == 6:
                    print(f'Salario Liquido do Funcionario: {funcionarios[func][c]:.2f}')
            print('-'*65)
            cont = int(input('Digite 1 para determinar outra folha de pagamento ou outro numero para voltar para o menu: '))
            if cont == 1:
                menu = 3
            else:
                menu = menuInicial()
        else:
            print('A lista esta vazia! Adicione um funcionario.')
            menu = menuInicial()
    elif menu == 4:
        if funcionarios != {}:
            for k in funcionarios.keys():
                print('-'*65)
                print(f'Matricula: {k}')
                for c in range(len(funcionarios[k])):
                    if c == 0:
                        print(f'Nome do Funcionario: {funcionarios[k][c]}')
                    elif c == 1:
                        print(f'Codigo da Função do Funcionario: {funcionarios[k][c]}')
                    elif c == 4:
                        print(f'Salario Bruto do Funcionario: R${funcionarios[k][c]:.2f}')
                    elif c == 6:
                        print(f'Salario Liquido do Funcionario: {funcionarios[k][c]:.2f}')
            print('-' * 65)
            cont = int(input('Digite 1 para ir ao menu: '))
            while cont != 1:
                print('Numero invalido!')
                cont = int(input('Digite 1 para ir ao menu: '))
            menu = menuInicial()
        else:
            print('A lista esta vazia! Adicione um funcionario.')
            menu = menuInicial()
    elif menu == 5:
        if funcionarios != {}:
            for salario in funcionarios.values():
                if maiorSal in salario:
                    print(f'Matricula: {matriculaMaiorSalLiq}')
                    for c in range(len(salario)):
                        if c == 0:
                            print(f'Nome do Funcionario: {salario[c]}')
                        elif c == 1:
                            print(f'Codigo da Função do Funcionario: {salario[c]}')
                        elif c == 4:
                            print(f'Salario Bruto do Funcionario: R${salario[c]:.2f}')
                        elif c == 5:
                            print(f'Percentual de Imposto do Funcionario: {salario[c]}%')
                        elif c == 6:
                            print(f'Salario Liquido do Funcionario: {salario[c]:.2f}')
                    print('-'*65)
            cont = int(input('Digite 1 para ir ao menu: '))
            while cont != 1:
                print('Numero invalido!')
                cont = int(input('Digite 1 para ir ao menu: '))
            menu = menuInicial()
        else:
            print('A lista esta vazia! Adicione um funcionario.')
            menu = menuInicial()
    elif menu == 6:
        if funcionarios != {}:
            for matricula, dados in funcionarios.items():
                if dados[2] == maiorFaltas:  # Verifica se o número de faltas é igual ao maior registrado
                    print(f'Matricula: {matricula}')
                    for c in range(len(dados)):
                        if c == 0:
                            print(f'Nome do Funcionario: {dados[c]}')
                        elif c == 1:
                            print(f'Codigo da Função do Funcionario: {dados[c]}')
                        elif c == 2:
                            print(f'Faltas do Funcionario: {dados[c]}')
                        elif c == 3:
                            print(f'Salario Descontado(Faltas): R${dados[c]:.2f}')
                    print('-' * 65)
            cont = int(input('Digite 1 para ir ao menu: '))
            while cont != 1:
                print('Numero invalido!')
                cont = int(input('Digite 1 para ir ao menu: '))
            menu = menuInicial()
        else:
            print('A lista esta vazia! Adicione um funcionario.')
            menu = menuInicial()
print('Programa encerrado!')