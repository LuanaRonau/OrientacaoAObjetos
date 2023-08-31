from copy import copy

class Produto:

    def __init__(self, nome, valor, tamanho):
        self.nome = nome
        self.valor = valor
        self.tamanho = tamanho
        self.quantidade = 0

    def get_nome(self):
        return self.nome

    def get_valor(self):
        return self.valor

    def get_tamanho(self):
        return self.tamanho

    def get_quant(self):
        return self.quantidade

    def set_nome(self, nome):
        self.nome = nome

    def set_valor(self, valor):
        self.valor = valor

    def set_quant(self, quant):
        self.quantidade = quant

    def calcular_valor(self):
        # 10% de taxação de serviço básico
        return self.valor * 1.1

    def listagem(self):
        return f'Nome: {self.nome}\nValor:{self.valor}\nTamanho:{self.tamanho}\n' \
               f'Quantidade:{self.quantidade}'


class ParteDeCima(Produto):

    def __init__(self, nome, valor, tamanho, manga, gola):
        super().__init__(nome, valor, tamanho)
        self.manga = manga
        self.gola = gola
        self.quantidade = 0

    def get_manga(self):
        return self.manga

    def get_gola(self):
        return self.gola

    def set_manga(self, manga):
        self.manga = manga

    def set_gola(self, gola):
        self.gola = gola

    def listagem(self):
        return f'Nome: {self.nome}\nValor:{self.valor}\nTamanho:{self.tamanho}\n' \
               f'Quantidade:{self.quantidade} \nTipo de manga:{self.manga}\nTipo de gola:{self.gola}'


class ParteDeBaixo(Produto):

    def __init__(self, nome, valor, tamanho, comprimento, modelagem):
        super().__init__(nome, valor, tamanho)
        self.comprimento = comprimento
        self.modelagem = modelagem
        self.quantidade = 0

    def get_comp(self):
        return self.comprimento

    def get_modelagem(self):
        return self.modelagem

    def set_comp(self, comp):
        self.comprimento = comp

    def set_modelagem(self, modelagem):
        self.modelagem = modelagem

    def listagem(self):
        return f'Nome: {self.nome}\nValor:{self.valor}\nTamanho:{self.tamanho}\n' \
               f'Quantidade:{self.quantidade}\nComprimento:{self.comprimento}\nModelagem:{self.modelagem}'


class CorpoTodo(ParteDeCima):

    def __init__(self, nome, preco_custo, tamanho, manga, gola, comprimento, modelagem):
        super().__init__(nome, preco_custo, tamanho, manga, gola)
        self.comprimento = comprimento
        self.modelagem = modelagem
        self.quantidade = 0

    def get_comp(self):
        return self.comprimento

    def get_modelagem(self):
        return self.modelagem

    def set_comp(self, comp):
        self.comprimento = comp

    def set_modelagem(self, modelagem):
        self.modelagem = modelagem

    def listagem(self):
        return f'Nome: {self.nome}\nValor:{self.valor}\nTamanho:{self.tamanho}\n' \
               f'Quantidade:{self.quantidade}\nTipo de manga:{self.manga}\n' \
               f'Tipo de gola:{self.gola}\nComprimento:{self.comprimento}\nModelagem:{self.modelagem}'


class Calcado(Produto):
    def __init__(self, nome, valor, tamanho, salto, marca):
        super().__init__(nome, valor, tamanho)
        self.salto = salto
        self.marca = marca
        self.quantidade = 0

    def get_salto(self):
        return self.salto

    def get_marca(self):
        return self.marca

    def set_salto(self, salto):
        self.salto = salto

    def set_marca(self, marca):
        self.marca = marca

    def calcular_valor(self):
        # Desconto aplicado aos sapatos
        return self.valor * 0.8 * 1.1

    def listagem(self):
        return f'Nome: {self.nome}\nValor:{self.valor}\nTamanho:{self.tamanho}\n' \
               f'Quantidade:{self.quantidade}\nAltura do salto:{self.salto}\nMarca:{self.marca}'


class Carrinho:
    def __init__(self):
        self.lista_compras = list()
        # Sub-estoque feito para retirar quantidade do estoque ao final
        self.sub_estoque = list()

    def adicionar_carrinho(self, lugar):

        while True:


            nome = input('Digite o nome do produto desejado: ').lower()
            lista_op = list()
            confirma = False

            # Checando a existência do produto, e adicionando à lista de produtos disponíveis.
            for i in lugar:
                if i.get_nome().lower() == nome:
                    lista_op.append(i)
                    confirma = True

            if confirma is True:

                for i in lista_op:
                    print(f'\nProduto {lista_op.index(i) + 1}:')
                    print(i.listagem())

                # Escolha do produto
                op = int(input('\nIndique o número do produto a ser adicionado: '))
                self.sub_estoque.append(lista_op[op-1])
                op = copy(lista_op[op-1])

                # Indicação de quantidade
                quant = int(input('\nIndique a quantidade: '))
                while quant > op.get_quant():
                    quant = int(input('Indique um valor válido: '))

                if quant < op.get_quant():
                    # Corrigindo a quantidade no carrinho
                    op.set_quant(quant)
                    self.lista_compras.append(op)

                # Concluindo
                op = input('Produto adicionado! Continuar adicionando? [S/N] ').upper()
                if op == 'S':
                    pass
                else:
                    break

            # Caso não houver resultados com a pesquisa:
            else:
                op = input('Produto não encontrado. Tentar novamente? [S/N] ').upper()
                if op == 'S':
                    pass
                else:
                    break

    def listar(self):

        print('\nCARRINHO: ')
        if len(self.lista_compras) > 0:
            for i in self.lista_compras:
                print(f'\n{i.listagem()}')
        else:
            print('Carrinho vazio.')

    def excluir(self):
        # Excluindo itens do carrinho
        while True:
            self.listar()
            op = input('\nDigite o produto que deseja excluir: ')
            lista_op = list()

            for i in self.lista_compras:
                if i.get_nome() == op:
                    lista_op.append(i)

            for i in lista_op:
                print(f'\nProduto {lista_op.index(i) + 1}:')
                print(i.listagem())

            # Escolha do produto
            op = int(input('\nIndique o número do produto a ser excluido: '))
            self.lista_compras.pop(self.lista_compras.index(lista_op[op-1]))

            op = input('Produto excluido! Continuar excluindo? [S/N] ').upper()
            if op == 'N':
                break

    def calcular_valor_total(self):
        # Calculo do valor total para finalizar a compra
        total = 0
        for i in self.lista_compras:
            total += i.calcular_valor() * i.get_quant()
        print(f'Valor da compra: R${round(total, 2)}. Obrigado por comprar conosco! ')
        print(f'(Valores de taxação e descontos (sapatos) incluídos no valor final.)')

    def retirar_estoque(self, lugar):
        # Corrigindo a quantidade no estoque
        for i in lugar:
            for y in self.sub_estoque:
                if y == i:
                    index = self.sub_estoque.index(y)
                    i.set_quant(i.get_quant() - self.lista_compras[index].get_quant())

        self.lista_compras.clear()


# Configurações iniciais
carrinho = Carrinho()
estoque = list()
estoque.append(CorpoTodo('vestido', 10.0, 'M', 'curta', 'alta', 'midi', 'justo'))
estoque[-1].set_quant(5)
estoque.append(Calcado('sapatilha', 20.0, '35', '0', 'moleca'))
estoque[-1].set_quant(5)
estoque.append(Calcado('sapatilha', 30.0, '35', '0', 'melissa'))
estoque[-1].set_quant(5)
estoque.append(ParteDeBaixo('calça', 30.0, 'G', 'canela', 'legging'))
estoque[-1].set_quant(5)


# Funções relacionadas ao gerenciamento de estoque

def adicionar(lugar):

    while True:

        nome, valor, quantidade = input('\nIndique o nome, valor, quantidade do produto a ser adicionado: ').split()
        valor, quantidade = float(valor), int(quantidade)

        op = int(input('''
        Indique qual tipo de produto será adicionado:
        1) Peça de cima
        2) Peça de baixo
        3) Peça de corpo todo
        4) Calçado
        '''))

        while 4 < op < 1:
            op = int(input('Digite uma opção válida.'))
        if op == 1:
            tamanho, manga, gola = input('Indique o tamanho, e o tipo de manga e gola, respectivamente: ').split()
            lugar.append(ParteDeCima(nome, valor, tamanho, manga, gola))
            lugar[-1].set_quant(quantidade)
        if op == 2:
            tamanho, comprimento, modelagem = input('Indique o tamanho, o comprimento e a '
                                                    'modelagem, respectivamente: ').split()
            lugar.append(ParteDeBaixo(nome, valor, tamanho, comprimento, modelagem))
            lugar[-1].set_quant(quantidade)
        if op == 3:
            tamanho, manga, gola, comprimento, modelagem = input('Indique o tamanho, o tipo de manga e gola, '
                                                                 'comprimento e modelagem, respectivamente: ').split()
            lugar.append(CorpoTodo(nome, valor, tamanho, manga, gola, comprimento, modelagem))
            lugar[-1].set_quant(quantidade)
        if op == 4:
            tamanho, salto, marca = input('Indique o tamanho, o tamanho do salto, e a marca, respectivamente: ').split()
            lugar.append(Calcado(nome, valor, tamanho, salto, marca))
            lugar[-1].set_quant(quantidade)

        print('Produto adicionado!')
        op = input('Continuar adicionando? [S/N] ').upper()
        if op == 'S':
            pass
        else:
            break


def excluir(lugar):

    excluir = busca(lugar)
    if excluir == '':
        pass
    else:
        op = input('\nDeseja excluir todos os produtos correspondentes?[S/N] ').upper()
        if op == 'S':
            for i in excluir:
                estoque.pop(estoque.index(i))
            print('Excluído com sucesso!')
        elif op == 'N':
            op = int(input('\nInforme o número do produto a ser excluido da lista: ').upper())
            for i in excluir:
                if excluir.index(i) + 1 == op:
                    estoque.pop(estoque.index(i))
            print('Excluído com sucesso!')
        else:
            pass


def busca(lugar):
    while True:
        pesquisa = input('\nDigite o nome do produto: ')
        print('...buscando produto...')
        lista_op = list()
        confirma = False

        for i in lugar:
            if i.get_nome().lower() == pesquisa.lower():
                lista_op.append(i)
                confirma = True

        if confirma is True:
            for i in lista_op:
                print(f'\nProduto {lista_op.index(i) + 1}:')
                print(i.listagem())
            return lista_op

        else:
            op = input('Produto não encontrado. Procurar novamente? [S/N] ').upper()
            if op == 'S':
                pass
            elif op == 'N':
                return ''


def listar(lugar):

    for i in lugar:
        if i.get_quant() == 0:
            lugar.pop(lugar.index(i))
        else:
            print(f'\n{i.listagem()}')


def menu_avancado():

    while True:
        op = int(input('''
            ====== MENU ESTOQUE ======
            1) Adicionar produtos
            2) Excluir produtos
            3) Buscar produtos
            4) Listar estoque
            5) Sair
            '''))

        while 5 < op < 1:
            op = int(input('Digite uma opção válida.'))

        if op == 1:
            print('\nAdicionando novos produtos!')
            adicionar(estoque)
        elif op == 2:
            excluir(estoque)
        elif op == 3:
            busca(estoque)
        elif op == 4:
            print('\nESTOQUE: ')
            listar(estoque)
        elif op == 5:
            break


# Menu principal

while True:

    menu_op = int(input('''
    ==========  MENU  ==========
    1) Adicionar produto ao carrinho
    2) Excluir produto ao carrinho
    3) Listar produtos no carrinho
    4) Finalizar compra
    5) Menu avançado (gerenciamento de estoque)
    6) Sair
        '''))

    while 6 < menu_op < 1:
        menu_op = int(input('Digite uma opção válida.'))

    if menu_op == 1:
        carrinho.adicionar_carrinho(estoque)
    elif menu_op == 2:
        carrinho.excluir()
    elif menu_op == 3:
        carrinho.listar()
    elif menu_op == 4:
        carrinho.calcular_valor_total()
        carrinho.retirar_estoque(estoque)
    elif menu_op == 5:
        menu_avancado()
    elif menu_op == 6:
        print('\nVOLTE SEMPRE!')
        break
