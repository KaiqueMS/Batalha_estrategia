from random import randint


def lutar(ataqueM, vidaI, defesaI, agilidadeI, posicaoI):
    ATK = randint(1, 20)
    if posicaoI == 'DEF':
        defesaI = defesaI + 3
        ATK = ATK + ataqueM
        if ATK >= defesaI:
            vidaI = vidaI - ATK
            print(f'Voce atingiu seu alvo e causou {ATK} de dano de ataque')
            print(f'Seu inimigo ficou com {vidaI} pontos de vida\n')
            return vidaI
        else:
            print(f'Seu ataque foi fraco demais...\n')
            return vidaI
    elif posicaoI == 'ESPERA':
        agilidadeI = agilidadeI + 3
        ATK = ATK + ataqueM
        if ATK > agilidadeI:
            vidaI = vidaI - ATK
            print(f'Voce atingiu seu alvo e causou {ATK} de dano de ataque')
            print(f'Seu inimigo ficou com {vidaI} pontos de vida\n')
            return vidaI
        else:
            print(f'Seu ataque errou o alvo...\n')
            return vidaI
    elif posicaoI == 'ATAQUE':
        ATK = ATK + ataqueM
        if ATK >= defesaI:
            vidaI = vidaI - ATK
            print(f'Voce atingiu seu alvo e causou {ATK} de dano de ataque')
            print(f'Seu inimigo ficou com {vidaI} pontos de vida\n')
            return vidaI
        else:
            print(f'Seu ataque foi fraco demais...\n')
            return vidaI
    else:
        ATK = ATK + ataqueM
        vidaI = vidaI - ATK
        print(f'Voce atingiu seu alvo e causou {ATK} de dano de ataque')
        print(f'Seu inimigo ficou com {vidaI} pontos de vida\n')
        return vidaI
