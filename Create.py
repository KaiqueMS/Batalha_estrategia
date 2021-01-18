from random import randint


class PersonagemP:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = ''
        self.pontosATK = randint(5, 20)
        self.pontosDEF = randint(5, 20)
        self.pontosRFL = randint(5, 20)
        self.pontosLife = 50
        self.barraEspecial = 3
        self.barraMP = randint(5, 30)


class Criatura:
    def __init__(self, nome):
        self.monsterNome = nome
        self.monsterPocicao = ''
        self.monsterEndurecimento = 0
        self.monsterAtaque = 0
        self.monsterAgilidade = 0
        self.monsterVida = 0
        self.monsterEspecial = 0
        self.monsterHabilidades = []
        self.monsterMagias = []
        self.monsterBarraMP = 0


class Invocador(PersonagemP):
    def __init__(self, nome):
        super().__init__(nome)
        self.invocadorNome = nome
        self.invocadorATK = self.pontosATK - 3
        self.invocadorDEF = self.pontosDEF - 3
        self.invocadorRFL = self.pontosRFL - 3
        self.invocadorLife = self.pontosLife + 5
        self.invocadorEspecial = self.barraEspecial + 3
        self.invocadorClasse = 'Invocador'
        self.invocadorBarraMP = self.barraMP + 10
        self.invocadorMagia = ['Summon']
        self.summon = False


# Invocações
class Dragao(Criatura):
    def __init__(self, nome):
        super().__init__(nome)
        self.dragao1Nome = 'Dragão Vermelho'
        self.dragao1Level = 5
        self.dragao1Posicao = ''
        self.dragao1Endurecimento = 30
        self.dragao1Ataque = 20
        self.dragao1Agilidade = 25
        self.dragao1Vida = 100
        self.dragao1Especial = 5
        self.dragao1Habilidades = [
            {'Predominancia sobre o fogo': {'Ativação': 'Fogo', 'Efeito em ataques magicos atributo(fogo)': 10}, },
            {'Voar': {'Ativação': 'céu', 'Efeito em agilidade': 10}}]
        self.dragao1Magias = [{'Cuspir fogo': {'CustoMP': 11, 'Dano': 10}},
                              {'Cuspir gelo': {'CustoMP': 15, 'Dano': 10}}]
        self.dragao1MP = self.monsterBarraMP + 10
