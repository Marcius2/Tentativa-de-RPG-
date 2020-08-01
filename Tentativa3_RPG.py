import random

print('\n                  ■■■■■■■■■■■■■■■■■■■□□□  NOWLOADING')

#lista = ['Guerreiro', 'Paladino', 'Mago']
inimigos = ['Esqueleto', 'Zumbi', 'Manticore']
enemies = random.choice(inimigos)
print('-----------------------------------------------------------------------')
print('|>Guerreiro:              >Paladino:             >Mago:               |\n|Dano do machado: 10-15 | Dano da espada: 11-16 | Dano do cajado: 9-16|\n|Vida maxima: 90        | Vida maxima: 100      | Vida maxima: 80     |')
print('-----------------------------------------------------------------------')

classe = input('Escolha sua classe: (Guerreiro/Paladino/Mago) -> ').lower()

#  _____  _                       
# |  __ \| |                      
# | |__) | | __ _ _   _  ___ _ __ 
# |  ___/| |/ _` | | | |/ _ \ '__|
# | |    | | (_| | |_| |  __/ |   
# |_|    |_|\__,_|\__, |\___|_|   
#                 __/ |          
#                |___/  

class character():
    def __init__(self, health):
        self.health = health
        

class guerreiro(character):
    def __init__(self, health, axe):
        super().__init__(health)
        self.axe = axe
        
    def machado(self):
        self.axe = random.randint(10,15)
        return self.axe
    def vida(self):
        self.health = 90 
        return self.health

warrior = guerreiro(90, random.randint(10,15))
health_w = warrior.vida()
#--------------------------------------------------------------------------------
class paladino(character):
    def __init__(self, health, sword):
        super().__init__(sword)
        self.sword = sword   
        
    def espada(self):
        self.sword = random.randint(11,16)
        return self.sword
    def vida(self):
        self.health = 100  
        return self.health

paladin = paladino(100, random.randint(11,16))
health_p = paladin.vida()
#---------------------------------------------------------------------------------
class mago(character):
    def __init__(self, health, staff):
        super().__init__(staff)
        self.staff = staff
    def cajado(self):
        self.staff = random.randint(9, 16)
        return self.staff
    def vida(self):
        self.health = 80 
        return self.health

mage = mago(80, random.randint(9, 16))
health_m = mage.vida()

if classe == 'guerreiro':
    print('\nVocê escolheu a classe:', classe,'e possui ', warrior.vida(), ' de vida inicial!')
if classe == 'paladino':
    print('\nVocê escolheu a classe:', classe,'e possui ', paladin.vida(), ' de vida inicial!')
if classe == 'mago':
    print('\nVocê escolheu a classe:', classe,'e possui ', mage.vida(), ' de vida inicial!')

#  ______                            
# |  ____|                           
# | |__   _ __   ___ _ __ ___  _   _ 
# |  __| | '_ \ / _ \ '_ ` _ \| | | |
# | |____| | | |  __/ | | | | | |_| |
# |______|_| |_|\___|_| |_| |_|\__, |
#                              __/ |
#                             |___/ 

class enemy():
    def __init__(self, enemy_health):
        self.enemy_health = enemy_health



class esqueleto(enemy):
    def __init__(self, enemy_health, bow):
        super().__init__(enemy_health)
        self.bow = bow
    def flechada(self):
        self.bow = random.randint(7,11)
        return self.bow
    def vida(self):
        self.enemy_health - random.randint(40,60)
        return self.enemy_health
    
skeleton = esqueleto(random.randint(40,60), random.randint(7,11))
health_s = skeleton.vida()
#---------------------------------------------------------------------------------
class zumbi(enemy):
    def __init__(self, enemy_health, bite):
        super().__init__(enemy_health)
        self.bite = bite
    def mordida(self):
        self.bite = random.randint(5,12)
        return self.bite
    def vida(self):
        self.enemy_health - random.randint(30,50)
        return self.enemy_health

zombie = zumbi(random.randint(30, 50), random.randint(5,12))
health_z = zombie.vida()
#---------------------------------------------------------------------------------
class manticoria(enemy):
    def __init__(self, enemy_health, sting):
        super().__init__(enemy_health)
        self.sting = sting
        #self.fangs = fangs
    def rugido(self):
        print('ROOOOAR')
    def ferroada(self):
        self.sting = random.randint(10,15)
        return self.sting
    def vida(self):
        self.enemy_health - random.randint(60,80)
        return self.enemy_health

manticore = manticoria(random.randint(60,80), random.randint(10,15))
health_mant = manticore.vida()

def spawn():
    global enemies
    global health_s
    global health_z
    global health_mant
    if health_s <= 0 or health_z <= 0 or health_mant <= 0:
        enemies = random.choice(inimigos)
        print(enemies)

def enemy_appear():
    
    print('\nVocê entra na masmorra e se depara com um ', enemies)
    if enemies == 'Esqueleto':
        print('\nO esqueleto prepara seu arco')        
    elif enemies == 'Zumbi':
        print('\nO morto vivo corre em sua direção')      
    else:
        print('\nUm grande manticore cai do céu diante de você e se prepara para a batalha\n', manticore.rugido()) 
enemy_appear()


#   _____                _           _         _____  _                       
#  / ____|              | |         | |       |  __ \| |                      
# | |     ___  _ __ ___ | |__   __ _| |_ ___  | |__) | | __ _ _   _  ___ _ __ 
# | |    / _ \| '_ ` _ \| '_ \ / _` | __/ _ \ |  ___/| |/ _` | | | |/ _ \ '__|
# | |___| (_) | | | | | | |_) | (_| | ||  __/ | |    | | (_| | |_| |  __/ |   
#  \_____\___/|_| |_| |_|_.__/ \__,_|\__\___| |_|    |_|\__,_|\__, |\___|_|   
#                                                              __/ |          
#                                                             |___/        
                                                                
def combate_p():
    global health_s                     #health_s = skeleton.vida()
    global health_z                     #health_z = zombie.vida()
    global health_mant                  #health_mant = manticore.vida()
    espadada = paladin.espada()
    machadada = warrior.machado()
    cajadada = mage.cajado()

    if classe == 'mago':
        if enemies == 'Esqueleto':
            health_s = health_s - cajadada
            print('\n(∩｀-´)⊃━━━━━O:｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆')
            print('O esqueleto sofreu ', cajadada, 'de dano, agora ele possui ', health_s, ' de vida\n')
            if health_s <= 0:
                print('E com um poderoso feixe de luz, o esqueleto inimigo foi transformado em cinzas\n')
                exit(0)
                spawn()
        elif enemies == 'Zumbi':
            health_z = health_z - cajadada
            print('\n(∩｀-´)⊃━━━━━O:｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆')
            print('O zumbi sofreu ', cajadada, 'de dano, agora ele possui ', health_z, ' de vida\n')
            if health_z <= 0:
                print('E com um poderoso feixe de luz, o zumbi inimigo foi transformado em cinzas\n')
                exit(0)
                spawn()
        elif enemies == 'Manticore':
            health_mant = health_mant - cajadada
            print('\n(∩｀-´)⊃━━━━━O:｡･:*:･ﾟ’★,｡･:*:♪･ﾟ’☆')
            print('O manticore sofreu ', cajadada, 'de dano, agora ele possui ', health_mant, ' de vida\n')
            if health_mant <= 0:
                print('E com um poderoso feixe de luz, o temível manticore foi destruído\n')
                exit(0)
                spawn()

    elif classe == 'paladino':
        if enemies == 'Esqueleto':
            health_s = health_s - espadada
            print('\n▬▬ι═════════════════════ﺤ')
            print('O esqueleto sofreu ', espadada, 'de dano, agora ele possui ', health_s, ' de vida\n')
            if health_s <= 0:
                print('E com um poderoso golpe de sua espada, a maldição do esqueleto foi desfeita e os ossos caem diante de seus pés\n')
                exit(0)
                spawn()
        elif enemies == 'Zumbi':
            health_z = health_z - espadada
            print('\n▬▬ι═════════════════════ﺤ')
            print('O zumbi sofreu ', espadada, 'de dano, agora ele possui ', health_z, ' de vida\n')
            if health_z <= 0:
                print('E com um poderoso golpe de sua espada, o morto vivo foi derrotado, e dessa vez, nunca mais se levantará\n')
                exit(0)
                spawn()
        elif enemies == 'Manticore':
            health_mant = health_mant - espadada
            print('\n▬▬ι═════════════════════ﺤ')
            print('O manticore sofreu ', espadada, 'de dano, agora ele possui ', health_mant, ' de vida\n')
            if health_mant <= 0:
                print('E com um golpe preciso de sua espada reluzente, o coração da besta é perfurando e ela\n nunca mais trará caos ao reino\n')
                exit(0)
                spawn()

    elif classe == 'guerreiro':
        if enemies == 'Esqueleto':
            health_s = health_s - machadada
            print('\n               +-+')
            print('  =============| |')
            print('              `:_;')
            print('\nO esqueleto sofreu ', machadada, 'de dano, agora ele possui ', health_s, ' de vida\n')
            if health_s <= 0:
                print('E com um poderoso golpe de machado, o esqueleto inimigo foi pulverizado\n')
                exit(0)
                spawn()
        elif enemies == 'Zumbi':
            health_z = health_z - machadada
            print('\n               +-+')
            print('  =============| |')
            print('              `:_;')
            print('\nO zumbi sofreu ', machadada, 'de dano, agora ele possui ', health_z, ' de vida\n')
            if health_z <= 0:
                print('E com um poderoso golpe de machado, o zumbi inimigo foi partido ao meio\n')
                exit(0)
                spawn()
        elif enemies == 'Manticore':
            health_mant = health_mant - machadada
            print('\n               +-+')
            print('  =============| |')
            print('              `:_;')
            print('\nO manticore sofreu ', machadada, 'de dano, agora ele possui ', health_mant, ' de vida\n')
            if health_mant <= 0:
                print('E com um poderoso golpe de machado, o manticore inimigo foi abatido\n')
                exit(0)
                spawn()
        

#   _____                _           _         _____       _           _             
#  / ____|              | |         | |       |_   _|     (_)         (_)            
# | |     ___  _ __ ___ | |__   __ _| |_ ___    | |  _ __  _ _ __ ___  _  __ _  ___  
# | |    / _ \| '_ ` _ \| '_ \ / _` | __/ _ \   | | | '_ \| | '_ ` _ \| |/ _` |/ _ \ 
# | |___| (_) | | | | | | |_) | (_| | ||  __/  _| |_| | | | | | | | | | | (_| | (_) |
#  \_____\___/|_| |_| |_|_.__/ \__,_|\__\___| |_____|_| |_|_|_| |_| |_|_|\__, |\___/ 
#                                                                         __/ |      
#                                                                        |___/       

def combate_e():
    global health_m                 #health_m = mage.vida()
    global health_p                 #health_p = paladin.vida()
    global health_w                 #health_w = warrior.vida()
    arrow = skeleton.flechada()
    nhac = zombie.mordida()
    ferroada = manticore.ferroada()

    if classe == 'mago':
        if enemies == 'Esqueleto':
            health_m = health_m - arrow
            print('\n                             »»————————————————————►')
            print('Você sofreu ', arrow, 'de dano, agora você possui ', health_m, ' de vida\n')
            if health_m <= 0:
                print('E com um poderoso golpe, o grande mago foi derrotado')
                exit(0)
        elif enemies == 'Zumbi':
            health_m = health_m - nhac
            print('Você sofreu ', nhac, 'de dano, agora você possui ', health_m, ' de vida\n')
            if health_m <= 0:
                print('E com um poderoso golpe, o grande mago foi derrotado')
                exit(0)
        elif enemies == 'Manticore':
            health_m = health_m - ferroada
            print('Você sofreu ', ferroada, 'de dano, agora você possui ', health_m, ' de vida\n')
            if health_m <= 0:
                print('E com um poderoso golpe, o grande mago foi derrotado')
                exit(0)

    elif classe == 'paladino':
        if enemies == 'Esqueleto':
            health_p = health_p - arrow
            print('\n                             »»————————————————————►')
            print('Você sofreu ', arrow, 'de dano, agora você possui ', health_p, ' de vida\n')
            if health_p <= 0:
                print('E com um poderoso golpe, o grande paladino foi derrotado')
                exit(0)
        elif enemies == 'Zumbi':
            health_p = health_p - nhac
            print('Você sofreu ', nhac, 'de dano, agora você possui ', health_p, ' de vida\n')
            if health_p <= 0:
                print('E com um poderoso golpe, o grande paladino foi derrotado')
                exit(0)
        elif enemies == 'Manticore':
            health_p = health_p - ferroada
            print('Você sofreu ', ferroada, 'de dano, agora você possui ', health_p, ' de vida\n')
            if health_p <= 0:
                print('E com um poderoso golpe, o grande paladino foi derrotado')
                exit(0)

    elif classe == 'guerreiro':
        if enemies == 'Esqueleto':
            health_w = health_w - arrow
            print('\n                             »»————————————————————►')
            print('Você sofreu ', arrow, 'de dano, agora você possui ', health_w, ' de vida\n')
            if health_w <= 0:
                print('E com um poderoso golpe, o grande guerreiro foi derrotado')
                exit(0)
        elif enemies == 'Zumbi':
            health_w = health_w - nhac
            print('Você sofreu ', nhac, 'de dano, agora você possui ', health_w, ' de vida\n')
            if health_w <= 0:
                print('E com um poderoso golpe, o grande guerreiro foi derrotado')
                exit(0)        
        elif enemies == 'Manticore':
            health_w = health_w - ferroada
            print('Você sofreu ', ferroada, 'de dano, agora você possui ', health_w, ' de vida\n')
            if health_w <= 0:
                print('E com um poderoso golpe, o grande guerreiro foi derrotado')
                exit(0)
#  ______                 
# |  ____|                
# | |__ _   _  __ _  __ _ 
# |  __| | | |/ _` |/ _` |
# | |  | |_| | (_| | (_| |
# |_|   \__,_|\__, |\__,_|
#               _/ |      
#              |___/      

def flee():
    dado = random.randint(0,5)
    if dado == 0:
        combate_e()
        print('Você tenta fugir mas seu inimigo é mais rápido!')
    else:
        print('Você conseguiu fugir!\n')
        exit(0)

#   _____                
#  / ____|               
# | |    _   _ _ __ __ _ 
# | |   | | | | '__/ _` |
# | |___| |_| | | | (_| |
#  \_____\__,_|_|  \__,_|
                       
def potion():
    global health_m
    global health_p
    global health_w
    num_pot = 0
    #num_pot = 5
    #pots = range(0,5)
    #for x in pots:
    if escolha == 'curar' and classe == 'mago':
        health_m += 20
        num_pot += 1
        print('Você acaba de usar ', num_pot, ' poções e tem ', health_m, ' de vida!')
            #break
    elif escolha == 'curar' and classe == 'paladino':
        health_p += 20
        num_pot += 1
        print('Você acaba de usar ', num_pot, ' poções e tem ', health_p, ' de vida!')
            #break
    elif escolha == 'curar' and classe == 'guerreiro':
        health_w += 20
        num_pot += 1
        print('Você acaba de usar ', num_pot, ' poções e tem ', health_w, ' de vida!')
            #break 
    elif num_pot >= 5:
        print('Você não tem mais poções para usar')


while True:
    print('--------------------------------------------------------------------')
    escolha = input('\nEscolha o que deseja fazer: (atacar/fugir/curar) -> ').lower()
    dicio = {'atacar':'attack', 'fugir':'flee', 'curar':'heal'}
    print('\nVocê escolheu:', dicio[escolha])

    if escolha == 'atacar':
        combate_p()
        combate_e()
    elif escolha == 'fugir':
        flee()
    elif escolha == 'curar':
        potion()
        '''
    elif health_s <= 0 or health_z <= 0 or health_mant <= 0:
        if health_m > 0 or health_p > 0 or health_w > 0:
            exit(0)
            spawn()
        else:
            exit(0)
            '''
    else:
        print('Escolha sua ação corretamente')
        pass


#https://codereview.stackexchange.com/questions/60571/battle-a-random-enemy/60574
#esse link não foi usado, só queria salvar em algum lugar mesmo pq pareceu legal 