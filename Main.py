import pygame
from time import sleep
from random import randint
from Create import PersonagemP
from Create import Invocador
from Create import Dragao
from Luta import lutar

'''Objetos Criados'''

'''Protagonista'''
Main1 = Invocador('Pedro')
nomeM = Main1.nome
vidaM = Main1.invocadorLife
ATKM = Main1.invocadorATK
defesaM = Main1.invocadorDEF
posicaoM = Main1.posicao
AGIL_M = Main1.invocadorDEF
barraEspecialM = Main1.invocadorEspecial
classeM = Main1.invocadorClasse
mpM = Main1.invocadorBarraMP
magiasM = Main1.invocadorMagia
magiaActiveM = Main1.summon

'''Inimigo'''
inimigoN = PersonagemP('Inimigo1')
nomeE = inimigoN.nome
vidaE = inimigoN.pontosLife
ATKE = inimigoN.pontosATK
defesaE = inimigoN.pontosDEF
posicaoE = inimigoN.posicao
AGIL_E = inimigoN.pontosRFL
barraEspecialE = inimigoN.barraEspecial

'''Invocador(invocações)'''
dragaoinvoc = Dragao('')
dragaoLevel = dragaoinvoc.dragao1Level
dragaoPosicao = dragaoinvoc.dragao1Posicao
dragaoName = dragaoinvoc.dragao1Nome
dragaoATK = dragaoinvoc.dragao1Ataque
dragaoDEF = dragaoinvoc.dragao1Endurecimento
dragaoAGL = dragaoinvoc.dragao1Agilidade
dragaoEspecial = dragaoinvoc.dragao1Especial
dragaoHabilit = dragaoinvoc.dragao1Habilidades
dragaoMP = dragaoinvoc.dragao1MP
dragaoMagias = dragaoinvoc.dragao1Magias
dragaoLife = dragaoinvoc.dragao1Vida


print(f'A batalha entre {nomeM} e {nomeE} começa\n')
print('*' * 30, '\n')

while vidaM > 0 and vidaE > 0:

    print(f'Vez de {nomeM}')
    escolhaActionM = int(input("Você deseja 1.atacar, 2.defender, 3.esperar, 4.Conjurar magia ou 5.Checar estado? "))
    if escolhaActionM == 1:
        print(f'Os pontos de vida de {nomeE} sao: {vidaE}')
        posicaoM = 'ATAQUE'
        vidaE = lutar(ATKM, vidaE, defesaE, AGIL_E, posicaoE)
        sleep(2.0)
    elif escolhaActionM == 2:
        posicaoM = 'DEF'
        print('Defendendo...\n')
        sleep(2.0)
    elif escolhaActionM == 3:
        posicaoM = 'ESPERA'
        print('Esperando...\n')
        sleep(2.0)
    elif escolhaActionM == 4:
        magiaActiveM = True
        mpM -= dragaoLevel
        print(f'Voce utilizou {dragaoLevel} de MP!')
        print(f'Um circulo magico aparece no chão...')
        sleep(1.0)
        print(f'Dentro dele chamas cuspidas para fora...')
        sleep(1.0)
        print(f'Ouvi-se o rosnar da criatura alada...')
        sleep(1.0)
        print(f'E do circulo surge um {dragaoName} aos seus comandos...\n')
        sleep(1.0)
    elif escolhaActionM == 5:
        print('-=-=-=-Seu status-=-=-=-')
        print(f'Vida: {vidaM}')
        print(f'MP: {mpM}')
        print(f'Posição: {posicaoM}\n')

    if magiaActiveM:
        print(f'Vez do {dragaoName}')
        escolhaActionInvoc = randint(1, 4)
        print(f'O valor da escolha foi {escolhaActionInvoc}')
        if escolhaActionInvoc == 1:
            dragaoPosicao = 'ATAQUE'
            print(f'Os pontos de vida de {dragaoName} sao: {dragaoLife}')
            vidaE = lutar(dragaoATK, vidaE, defesaE, AGIL_E, posicaoE)
            sleep(2.0)
        elif escolhaActionInvoc == 2:
            dragaoPosicao = 'DEF'
            print('Defendendo...\n')
            sleep(2.0)
        elif escolhaActionInvoc == 3:
            dragaoPosicao = 'ESPERA'
            print('Esperando...\n')
            sleep(2.0)
        elif escolhaActionInvoc == 4:
            escolhaActionInvoc = randint(1, 2)
            if escolhaActionInvoc == 1:
                print(f'{dragaoName} lançou a magia Cuspir fogo!\n'
                      f'Causando {dragaoMagias[0]["Cuspir fogo"]["Dano"]} de dano ao {nomeE}')
                sleep(2.0)
                vidaE = vidaE - dragaoMagias[0]["Cuspir fogo"]["Dano"]
            elif escolhaActionInvoc == 2:
                print(f'{dragaoName} lançou a magia Cuspir gelo!\n'
                      f'Causando {dragaoMagias[1]["Cuspir gelo"]["Dano"]} de dano ao {nomeE}')
                sleep(2.0)
                vidaE = vidaE - dragaoMagias[1]["Cuspir gelo"]["Dano"]

    print(f"\nVez de {nomeE}")
    escolhaActionE = randint(1, 3)
    print(f'O valor da escolha foi {escolhaActionE}')
    if escolhaActionE == 1:
        posicaoE = 'ATAQUE'
        print(f'Os pontos de vida do protagonista {nomeM} sao: {vidaM}')
        vidaM = lutar(ATKE, vidaM, defesaM, AGIL_M, posicaoM)
        sleep(2.0)
    elif escolhaActionE == 2:
        posicaoE = 'DEF'
        print('Defendendo...\n')
        sleep(2.0)
    elif escolhaActionE == 3:
        posicaoE = 'ESPERA'
        print('Esperando...\n')
        sleep(2.0)
