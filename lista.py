class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.status = "disponível"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.membros = {}

    def adicionar_livro(self, livro):
        self.livros[livro.titulo] = livro

    def registrar_membro(self, membro):
        self.membros[membro.nome] = membro

    def emprestar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "disponível":
                livro.status = "emprestado"
                self.membros[nome_membro].livros_emprestados.append(livro)
                return f"{titulo_livro} emprestado para {nome_membro}."
            else:
                return f"{titulo_livro} não está disponível no momento."
        else:
            return "Livro ou membro não encontrado."

    def retornar_livro(self, titulo_livro, nome_membro):
        if titulo_livro in self.livros and nome_membro in self.membros:
            livro = self.livros[titulo_livro]
            if livro.status == "emprestado" and livro in self.membros[nome_membro].livros_emprestados:
                livro.status = "disponível"
                self.membros[nome_membro].livros_emprestados.remove(livro)
                return f"{titulo_livro} retornado por {nome_membro}."
            else:
                return f"{titulo_livro} não foi emprestado para {nome_membro}."
        else:
            return "Livro ou membro não encontrado."

class Restaurante:
    def __init__(self):
        self.itens_menu = {
            "hamburger": 5.50,
            "batata frita": 2.00,
            "refrigerante": 1.50
        }
        self.pedidos = {}

    def adicionar_pedido(self, numero_pedido, pedido):
        self.pedidos[numero_pedido] = pedido

    def adicionar_item_pedido(self, numero_pedido, item, quantidade):
        if numero_pedido in self.pedidos and item in self.itens_menu:
            if item in self.pedidos[numero_pedido]:
                self.pedidos[numero_pedido][item] += quantidade
            else:
                self.pedidos[numero_pedido][item] = quantidade
        else:
            return "Pedido ou item não encontrado."

    def calcular_total_pedido(self, numero_pedido):
        if numero_pedido in self.pedidos:
            total = 0
            for item, quantidade in self.pedidos[numero_pedido].items():
                if item in self.itens_menu:
                    total += self.itens_menu[item] * quantidade
            return total
        else:
            return "Pedido não encontrado."

class Animal:
    def __init__(self, nome, especie, idade, dieta):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.dieta = dieta

    def descricao(self):
        return f"{self.nome} é um {self.especie} de {self.idade} anos que é {self.dieta}."

class Zoologico:
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
                return f"{nome} foi removido do zoológico."
        return f"{nome} não encontrado no zoológico."

    def listar_animais(self):
        for animal in self.animais:
            print(animal.descricao())

    def buscar_por_especie(self, especie):
        animais_especie = [animal for animal in self.animais if animal.especie == especie]
        return animais_especie

    def listar_animais_em_habitat(self, habitat):
        animais_habitat = [animal for animal in self.animais if hasattr(animal, 'habitat') and animal.habitat == habitat]
        return animais_habitat

class Jogo:
    def __init__(self, nome, categoria, taxa_entrada, id):
        self.nome = nome
        self.categoria = categoria
        self.taxa_entrada = taxa_entrada
        self.id = id

    def __str__(self):
        return f"Nome: {self.nome}, Categoria: {self.categoria}, Taxa de Entrada: {self.taxa_entrada}, ID: {self.id}"

class Plataforma:
    def __init__(self):
        self.jogos = []

    def adicionar_jogo(self, jogo):
        self.jogos.append(jogo)

    def remover_jogo(self, id):
        for jogo in self.jogos:
            if jogo.id == id:
                self.jogos.remove(jogo)
                return f"Jogo com ID {id} removido."
        return f"Jogo com ID {id} não encontrado."

    def listar_jogos(self):
        for jogo in self.jogos:
            print(jogo)

    def __str__(self):
        return f"Total de jogos na plataforma: {len(self.jogos)}"

class Estudante:
    def __init__(self, nome, idade, nota, id):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self.id = id

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Nota: {self.nota}, ID: {self.id}"

class Turma:
    def __init__(self):
        self.estudantes = []

    def adicionar_estudante(self, estudante):
        self.estudantes.append(estudante)

    def remover_estudante(self, id):
        for estudante in self.estudantes:
            if estudante.id == id:
                self.estudantes.remove(estudante)
                return f"Estudante com ID {id} removido."
        return f"Estudante com ID {id} não encontrado."

    def media_da_turma(self):
        if not self.estudantes:
            return "Nenhum estudante na turma."
        total_notas = sum(estudante.nota for estudante in self.estudantes)
        return total_notas / len(self.estudantes)

    def melhor_estudante(self):
        if not self.estudantes:
            return "Nenhum estudante na turma."
        melhor = max(self.estudantes, key=lambda estudante: estudante.nota)
        return melhor.informacoes()
