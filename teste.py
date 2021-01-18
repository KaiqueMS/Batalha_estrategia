invocacoes = {'atron': {'ataque': 10, 'defesa': 10, 'agilidade': 5,
                        'magias': {'fogo': {'dano': 5, 'velocidade': 10},
                                   'gelo': {'dano': 10, 'velocidade': 5}}},
              'dragão': {'ataque': 20, 'defesa': 15, 'agilidade': 10,
                         'magias': {'cuspir fogo': {'dano': 15, 'velocidade': 5},
                                    'cuspir gelo': {'dano': 15, 'velocidade': 15}}}
              }


print(invocacoes)
# escolha = input('Escolha uma invocacao: ')
escolha = 'atron'
if escolha in invocacoes:
    print(f'Voce invocou {escolha}... Suas habilidades são: ')
    print(f'Seu poder de ataque é: {invocacoes[escolha]["ataque"]}')
    print(f'Sua defesa é: {invocacoes[escolha]["defesa"]}')
    print(f'Sua agilidade é: {invocacoes[escolha]["agilidade"]}')
    if 'magias' in invocacoes[escolha]:
        print('Contendo as magias: ')
        for magia, especifica in invocacoes[escolha]['magias'].items():
            print(
                f'Sua magias são: {magia} com dano de {especifica["dano"]} e velocidade de {especifica["velocidade"]}')
