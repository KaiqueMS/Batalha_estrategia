from random import randint
from csv import reader
from copy import deepcopy

lista = list()  # Criação da lista a qual serão armazenadas as informações do csv
with open('Monstros.csv') as arquivoCSV:
    csv_monstros = reader(arquivoCSV,
                          delimiter=',')  # Armazenamento das informações do csv dentro da variavel csv_monstros

    for row in csv_monstros:
        lista.append(row[:7][:7])  # Aqui é armazenado as informações dentro da lista

cont = 0  # Contador
for monstro in lista:  # For feito para se saber quantos monstros tem na lista, ignorando a primeira linha.
    cont = cont + 1
cont -= 1

dicionario = dict()  # Criação do diccionario no qual serão melhor organizados as informações da lista

lista2 = list()  # Criação da lista na qual será armezanado o dicionario

# Variaveis contadoras abaixo
cont2 = 0
cont4 = 0
cont3 = 1

for tot in range(0, cont):  # Esse for irá se repetir na mesma quantidade de monstros da variavel contadora cont
    for pup in range(1, 8):  # Esse for se repete n vezes onde é quantidade de campos em uma linha do arquivo csv
        dicionario[lista[0][cont2]] = lista[cont3][
            cont4]  # Aqui é armazena no dicionario todas as informações apropriadamente
        """Esse é o processo feito dentro desse for
            dicionario[lista[0][0]] = lista[1][0]
            dicionario[lista[0][1]] = lista[1][1]
            dicionario[lista[0][2]] = lista[1][2]
            dicionario[lista[0][3]] = lista[1][3]
            dicionario[lista[0][4]] = lista[1][4]
            dicionario[lista[0][5]] = lista[1][5]"""
        # Acumulo das variaveis contadoras
        cont2 += 1
        cont4 += 1
    cont3 += 1
    cont2 = 0
    cont4 = 0
    lista2.append(
        deepcopy(dicionario))  # Aqui é feita uma cópia do dicionario a qual é armazenado dentro da lista lista2
    dicionario.clear()  # Aqui o dicionario original é apagado

print(f"Print da lista2 {lista2}")


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
