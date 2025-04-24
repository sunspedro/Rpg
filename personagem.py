from habilidade import paladinoHabilidades, guerreiroHabilidades, arqueiroHabilidades, magoHabilidades
from colorama import init, Fore

init()

class ClassePersonagem:
    def __init__(self, nome, ataque, vida, sorte, mana, habilidade):
        self.nome = nome
        self.ataque = ataque
        self.vida = vida
        self.sorte = sorte
        self.mana = mana
        self.habilidade = habilidade

class Personagem:
    def __init__(self, xp, xpUp, nivel):
        self.nome = input("Digite o nome do seu personagem: ")
        self.xp = xp
        self.xpUp = xpUp
        self.nivel = nivel
        self.habilidadesAprendidas = []

        self.opcoes_classe = {
            "1": ClassePersonagem("Guerreiro", 12, 40, 5, 9, guerreiroHabilidades),
            "2": ClassePersonagem("Paladino", 10, 35, 9, 15, paladinoHabilidades),
            "3": ClassePersonagem("Mago", 6, 20, 8, 25, magoHabilidades),
            "4": ClassePersonagem("Arqueiro", 11, 30, 12, 15, arqueiroHabilidades)
        }

        print("\nEscolha a classe do personagem:")
        print("1 - Guerreiro")
        print("2 - Paladino")
        print("3 - Mago")
        print("4 - Arqueiro")
        escolha = input("Digite o número da classe: ")
        self.classe = self.opcoes_classe.get(escolha) or self.opcoes_classe["1"]

        self.vidaAtual = self.classe.vida
        self.manaAtual = self.classe.mana

        self.habilidadesAprendidas.append(self.classe.habilidade[0])

    def exibirInfo(self):
        print(f"\n{self.nome} é um {self.classe.nome}")
        print(f"Ataque: {self.classe.ataque}")
        print(f"Vida: {self.classe.vida}")
        print(f"Sorte: {self.classe.sorte}")
        print(f"Mana: {self.classe.mana}")
        print(f"Habilidades: {[h.nome for h in self.habilidadesAprendidas]}")
        print(f"Nivel: {self.nivel}")
        print(f"XP Necessário para upar: {self.xpUp} | XP Atual: {self.xp}")

    def verificarNivel(self):
        while self.xp >= self.xpUp:
            self.nivel += 1
            self.xp -= self.xpUp
            self.xpUp = round(self.xpUp * 1.3)

            print(Fore.LIGHTBLUE_EX+f"\nVocê upou para o nivel {self.nivel}!")

            self.classe.vida = round(self.classe.vida * 1.2)
            self.classe.ataque = round(self.classe.ataque * 1.2)
            self.classe.mana = round(self.classe.mana * 1.1)

            if self.nivel == 5 and not any(h.nome == self.classe.habilidade[1].nome for h in self.habilidadesAprendidas):
                self.habilidadesAprendidas.append(self.classe.habilidade[1])
            if self.nivel == 9 and not any(h.nome == self.classe.habilidade[2].nome for h in self.habilidadesAprendidas):
                self.habilidadesAprendidas.append(self.classe.habilidade[2])
