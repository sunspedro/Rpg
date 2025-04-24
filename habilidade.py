import random 

class Habilidades:
    def __init__(self, nome, custoMana, efeito=None, passiva=False, tipo_alvo="inimigo"):
        self.nome = nome
        self.custoMana = custoMana
        self.efeito = efeito 
        self.passiva = passiva
        self.tipo_alvo = tipo_alvo  

def estruturaInabalavel(personagem, alvo=None):
    personagem.classe.vida *= 1.2  
estruturaInabalavel.passiva = True

def berserk(personagem, alvo=None): 
    personagem.classe.ataque *= 1.3  
    personagem.resistencia = 0.5
    print(f"Usou Berserk, ataque aumentado em 30%\n")

def espadaGiratoria(personagem, Monstro):
    dano = round(personagem.classe.ataque * 1.5) 
    Monstro.hpAtual -= dano
    print(f"Usou Espada giratoria e causou {dano} de dano\n")

def espadaHeroica(personagem, Monstro):
    dano = round(personagem.classe.ataque * 1.7)
    Monstro.hpAtual -= dano
    print(f"Usou Espada Heroica e causou {dano} de dano\n")

def pesLeves(personagem, alvo=None):
    personagem.classe.sorte *= 1.2   #calcular esquiva
pesLeves.passiva = True

def saraivada(personagem, Monstro):
    dano = round(personagem.classe.ataque * 1.5)
    Monstro.hpAtual -= dano
    print(f"Lançou uma Saraivada causando {dano} de dano\n")

def tiroDuplo(personagem, Monstro):
    dano = round(personagem.classe.ataque * 2) 
    Monstro.hpAtual -= dano
    print(f"Disparou um Tiro Duplo e causou {dano} de dano\n")

def headshot(personagem, Monstro):
    dano = round(personagem.classe.ataque * 2.5)
    Monstro.hpAtual -= dano
    print(f"Executou um Headshot causando {dano} de dano crítico\n")

def meditar(personagem, alvo=None):
    ganho = round(personagem.classe.mana * 0.4)
    personagem.manaAtual += ganho
    print(f"Ativou a passiva Meditar e recuperou {ganho} de mana\n")
meditar.passiva = True

def bolaDeFogo(personagem, Monstro):
    dano = round(personagem.classe.mana * 0.7)
    Monstro.hpAtual -= dano
    print(f"Lançou Bola de Fogo causando {dano} de dano\n")

def cristalDeGelo(personagem, Monstro):
    dano = round(personagem.classe.mana * 0.9)
    Monstro.hpAtual -= dano
    print(f"Lançou Cristal de Gelo causando {dano} de dano!\n")

def magiaElemental(personagem, Monstro):
    dano = round(personagem.classe.mana * 1.3)
    Monstro.hpAtual -= dano
    print(f"Conjurou Magia Elemental e causou {dano} de dano\n")

def vampirismo(personagem, monstro):
    dano = personagem.classe.ataque
    monstro.hpAtual -= dano
    cura = round(dano * 0.5)
    
    print(f"Você ataca causando {dano} de dano e recupera {cura:.1f} de vida!\n")
    return True

vampirismo.passiva = True

def espadaDivina(personagem, Monstro):
    dano = round(personagem.classe.ataque * 1.5)
    cura = round(personagem.classe.vida * 0.2)
    Monstro.hpAtual -= dano
    personagem.vidaAtual += cura   
    print(f"Atacou com Espada Divina: causou {dano} de dano e se curou em {cura}\n")

def santificar(personagem, alvo=None):
    personagem.vidaAtual += round(0.45 * personagem.classe.vida) + personagem.classe.vida
    print(f"Usou Santificar, vida ajustada para {personagem.classe.vida}\n")

def bencao(personagem, Monstro):
    dano = round(personagem.classe.ataque * 1.9)
    cura = round(personagem.classe.vida * 0.4)
    Monstro.hpAtual -= dano
    personagem.vidaAtual += cura 
    print(f"Usou Bênção: causou {dano} de dano e curou {cura} de vida\n")

estruturaInabalavel = Habilidades(nome="Estrutura Inabalável", custoMana=0, efeito=estruturaInabalavel, passiva=True, tipo_alvo="self")
berserk_ = Habilidades(nome="Berserk", custoMana=5, efeito=berserk, tipo_alvo="self")
espadaGiratoria_ = Habilidades(nome="Espada Giratória", custoMana=9, efeito=espadaGiratoria, tipo_alvo="inimigos")
espadaHeroica_ = Habilidades(nome="Espada Heroica", custoMana=15, efeito=espadaHeroica, tipo_alvo="inimigo")

guerreiroHabilidades = [
    berserk_,
    espadaGiratoria_,
    espadaHeroica_
]

pesLeves_ = Habilidades(nome="Pés Leves", custoMana=0, efeito=pesLeves, passiva=True, tipo_alvo="self")
saraivada_ = Habilidades(nome="Saraivada", custoMana=4, efeito=saraivada, tipo_alvo="inimigos")
tiroDuplo_ = Habilidades(nome="Tiro Duplo", custoMana=6, efeito=tiroDuplo, tipo_alvo="inimigo")
headshot_ = Habilidades(nome="Headshot", custoMana=10, efeito=headshot, tipo_alvo="inimigo")

arqueiroHabilidades = [
    saraivada_,
    tiroDuplo_,
    headshot_
]

meditar_ = Habilidades(nome="Meditar", custoMana=0, efeito=meditar, passiva=True, tipo_alvo="self")
bolaDeFogo_ = Habilidades(nome="Bola de Fogo", custoMana=10, efeito=bolaDeFogo, tipo_alvo="inimigo")
cristalDeGelo_ = Habilidades(nome="Cristal de Gelo", custoMana=12, efeito=cristalDeGelo, tipo_alvo="inimigo")
magiaElemental_ = Habilidades(nome="Magia Elemental", custoMana=18, efeito=magiaElemental, tipo_alvo="inimigo")

magoHabilidades = [
    bolaDeFogo_,
    cristalDeGelo_,
    magiaElemental_
]

vampirismo_ = Habilidades(nome="Contra ataque", custoMana=0, efeito=vampirismo, passiva=True, tipo_alvo="inimigo")
espadaDivina_ = Habilidades(nome="Espada Divina", custoMana=14, efeito=espadaDivina, tipo_alvo="inimigo")
santificar_ = Habilidades(nome="Santificar", custoMana=18, efeito=santificar, tipo_alvo="self")
bencao_ = Habilidades(nome="Bênção", custoMana=22, efeito=bencao, tipo_alvo="inimigo")

paladinoHabilidades = [
    espadaDivina_,
    santificar_,
    bencao_
]
