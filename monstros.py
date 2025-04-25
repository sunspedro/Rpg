from habilidade import meditar
class Monstro:
    def __init__(self, nome, ataque, hp, xpGanho):
        self.nome = nome
        self.ataque = ataque
        self.hp = hp
        self.xpGanho = xpGanho

    def batalha(self, personagem):
        self.hpAtual = self.hp
        personagem.ataqueBase = personagem.classe.ataque
        personagem.vidaBase = personagem.classe.vida

        print(f"\nA batalha contra {self.nome} começou!")

        while self.hpAtual > 0 and personagem.vidaAtual > 0:
            action = input("\nO que deseja fazer?\n1. Atacar\n2. Defender\n3. Usar habilidade\nEscolha: ")

            if action == "1":
                dano = round(personagem.classe.ataque)
                self.hpAtual -= dano
                print(f"\nVocê atacou o {self.nome} causando {dano} de dano!")
                if personagem.classe.nome == "Paladino":
                    cura = round(dano * 0.5)
                    personagem.vidaAtual = min(personagem.vidaAtual + cura, personagem.classe.vida)
                    print(f"Passiva do Paladino ativada! Você recuperou {cura} de vida.")
            
            elif action == "2":
                danoRecebido = round(self.ataque * 0.3)
                personagem.vidaAtual -= danoRecebido
            
            elif action == "3":
                print("Você possui as seguintes habilidades:")
                
                for i, h in enumerate(personagem.habilidadesAprendidas, 1):
                    print(f"{i}. {h.nome} | Custo de mana: {h.custoMana}")
                
                escolha_habilidade = input("Escolha a habilidade (número): ")

                if escolha_habilidade.isdigit() and 1 <= int(escolha_habilidade) <= len(personagem.habilidadesAprendidas):
                    habilidade = personagem.habilidadesAprendidas[int(escolha_habilidade)-1]

                    if personagem.manaAtual >= habilidade.custoMana:
                        personagem.manaAtual -= habilidade.custoMana
                        habilidade.efeito(personagem, self)
                        
                    else:
                        print(f"Personagem não tem mana suficiente para usar a {habilidade.nome}")
                
                else:
                    print("Escolha inválida.")
            else:
                print("Ação inválida. Você perdeu o turno.")

            if self.hpAtual > 0:
                if action != "2":
                    if hasattr(personagem, 'resistencia'):  #hasattr = has attribute / basicamente verifica se o personagem esta com o atritubo ativo
                        danoRecebido = round(self.ataque * personagem.resistencia  ) 
                    else:
                        danoRecebido = round(self.ataque)   
                    
                    personagem.vidaAtual -= danoRecebido   
                    print(f"O {self.nome} atacou você e causou {danoRecebido} de dano!")
                else:
                    print(f"Você se defendeu e recebeu {danoRecebido} de dano.")

            print(f"Seu HP: {personagem.vidaAtual}")
            print(f"Sua Mana: {personagem.manaAtual}")
            personagem.manaRegenerada = round(personagem.classe.mana * 0.4)
            personagem.manaAtual += personagem.manaRegenerada
            if personagem.classe.nome =="Mago":
                meditar(personagem)
            print(f"Mana regenerada em {personagem.manaRegenerada} pontos")
            print(f"HP do {self.nome}: {self.hpAtual}")

        if personagem.vidaAtual > 0:
            personagem.xp += self.xpGanho
            
            print(f"\nVocê venceu o {self.nome} e ganhou {self.xpGanho} de XP!")
        else:
            print(f"\nVocê foi derrotado pelo {self.nome}...")
        personagem.classe.ataque = personagem.ataqueBase
        personagem.classe.vida = personagem.vidaBase
        personagem.verificarNivel()
        personagem.vidaAtual = personagem.classe.vida
        personagem.manaAtual = personagem.classe.mana

def criarMonstros():
    # Planície
    slime = Monstro("Slime", 4, 18, 2)
    porco = Monstro("Porco", 5, 20, 3)
    cobra = Monstro("Cobra", 6, 22, 3)
    
    # Planície Noturna
    javali = Monstro("Javali", 6, 24, 5)
    bandido = Monstro("Bandido", 7, 28, 7)
    caçadorRecompensa = ("Caçador de recompensas", 9,30,7)

    # Floresta
    goblin = Monstro("Goblin", 8, 30, 9)
    goblinLanceiro = Monstro("Goblin Lanceiro", 9, 34, 9)
    orc = Monstro("Orc", 13, 40, 10)

    goblinRei = Monstro("Rei Goblin", 15, 60, 25)
    goblinReiDificil = Monstro("Rei Goblin", 17,80,25)

    # darama
    escorpiao = Monstro("Escorpião Gigante", 10, 45, 16)
    escaravelho = Monstro("Escaravelho", 11, 40, 16)
    hiena = Monstro("Hiena", 12, 44, 18)
    #dentro da piramide
    ladraoDeTumba = Monstro("Ladrão de tumba", 13, 48, 20)
    mumia = Monstro("Múmia Antiga", 12, 50, 22)
    dragaoReiDeserto = Monstro("Sarithar, o Eco do Deserto", 15, 70, 40)

    # khaldrós
    lobo = Monstro("Lobo do Gelo", 14, 55, 22)
    elementalDeGelo = Monstro("Elemental de Gelo", 15, 60, 25)
    elfoDasMontanhas = Monstro("Elfo das Montanhas", 16, 65, 28)
    
    #dentro da caverna
    morcegoGigante = Monstro("Morcego Gigante", 17, 68, 30)
    golem = Monstro("Golem de Neve", 16, 90, 35)
    dragaoReiGelo = Monstro("Glavendral, o Sussurro das Geleiras", 18, 140, 65)

    # chegando em  Thar'Khal (vulcao)
    salamandra = Monstro("Salamandra", 18, 72, 37)
    trollDeCinzas = Monstro("Troll de Cinzas", 19, 78, 40)
    diabreteDeFumaça = Monstro("Diabrete de fumaça", 20, 80, 52)
    #na subida até o topo
    dragaoBebe = Monstro("Dragão Bebê", 18, 85, 44)
    elemental = Monstro("Elemental de Fogo", 20, 95, 47)
    dragraoReiVulcao = Monstro("Volgareth, a Ira das Chamas", 23, 180, 100)

    # Vale dos Lamentos (cemiterio)
    esqueleto = Monstro("Esqueleto Guerreiro", 20, 90, 55)
    fantasma = Monstro("Fantasma Sombrio", 22, 100, 57)
    necromante = Monstro("Necromante", 23, 105, 60)
    vampiro = Monstro("Lorde Vampiro", 24, 110, 65)
    dragaoReiCemiterio = Monstro("Nyxarion, o Último Véu", 30, 200, 150)

    # Boss Final
    bossFinal = Monstro("Zharik", 30, 300, 35)

    return {
        "planiceDia": [slime, cobra, porco],
        "planiceNoite": [javali, bandido, caçadorRecompensa],
        "floresta": [goblin, goblinLanceiro, orc],
        "florestaBoss": [goblinRei],
        "florestaBossDificil": [goblinReiDificil],
        "deserto": [escorpiao, escaravelho, hiena, ladraoDeTumba, mumia],
        "desertoBoss":[dragaoReiDeserto],
        "gelo": [lobo, elementalDeGelo, elfoDasMontanhas, morcegoGigante, golem],
        "geloBoss": [dragaoReiGelo],
        "vulcao": [salamandra, trollDeCinzas, diabreteDeFumaça, dragaoBebe, elemental],
        "vulcaoBoss": [dragraoReiVulcao],
        "cemiterio": [esqueleto, fantasma, necromante, vampiro],
        "cemiterioBoss": [dragaoReiCemiterio],
        "boss": [bossFinal]
    }
