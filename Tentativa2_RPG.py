import random

#escolha = input('Escolha o que deseja fazer: (atacar/fugir) ').lower()

#dicio = {'atacar':'attack', 'fugir':'flee'}

health = 100
enemy_health = random.randint(50, 80)
ataque = random.randint(10, 15)
ataque_inimigo = random.randint(6, 12)
fuga = random.randint(0,5)
nome = input('Digite seu nome: ')

print('Olá ', nome, ' bem vindo à cidade!')
masmorra = input('Deseja entrar na masmorra? (sim/não) ').lower()
#o()xxxx[{::::::::::::::::::::::::::::::::::>
if masmorra == 'sim':
    print('\n |`-._/\_.-`|')
    print(   '.|    ||    |')
    print(   '.|___o()o___|')
    print(   '.|__((<>))__|')
    print(   '.\   o\/o   /')
    print(   '..\   ||   /')
    print(    '...\  ||  /')
    print(      '......||.')
    print(        '......``')
    print('Bem-vindo a masmorra, boa sorte!')
else:
    print('A porta atrás se fecha e você se encotra na masmorra')
#print('Você escolheu:', dicio[escolha])
    
while True:
        
    escolha = input('Escolha o que deseja fazer: (atacar/fugir) ').lower()
    dicio = {'atacar':'attack', 'fugir':'flee'}
    print('Você escolheu:', dicio[escolha])
    
    if enemy_health >= 75:
        print('\n*****BOSS ROOM*****\n')

    if escolha == 'atacar':
        print('\nO inimigo tem ', enemy_health, 'de vida!\n')
        

        dano =  enemy_health - ataque 
        novo_dano = dano
        enemy_health = novo_dano

        print('▬▬ι═════════════════════ﺤ')
        print('Você deu ', ataque, 'de dano ao inimigo, agora ele possui ', dano, 'de vida!')
        
        if escolha == 'atacar':

            vida = health - ataque_inimigo
            nova_vida = vida
            health = nova_vida

            print('\n-═════════════════════ι▬▬')
            print('O inimigo revida e inflinge ', ataque_inimigo, ' de dano, agora você possui ', vida, ' de vida!\n ')


        if enemy_health <= 0:
            print('O inimigo foi derrotado!')
            exit(0)                 #quando a vida do inimigo for <= 0, o programa para

    elif escolha == 'fugir':
        if fuga == 0:
            dano_tomado = health - ataque_inimigo
            print('\nVocê tentou fugir, mas seu inimigo foi mais rápido e te deu ', ataque_inimigo, 'de dano, agora você tem ', dano_tomado, 'de vida')
        else:
            print('\nVocê conseguiu fugir!')
    #if enemy_health <= 0:
    #    print('O inimigo foi derrotado!')
        
    else:
        #print('\nVocê foge da batalha...')
        #enemy_health = 0
        pass

    #if ataque > 0:
    #    break