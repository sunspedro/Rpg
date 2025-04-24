from personagem import Personagem, ClassePersonagem
from cap0 import cidadeInicial
from cap1 import fasePlanicies
from cap2 import faseFloresta

personagem = Personagem(xp=0, xpUp=30, nivel=1)
personagem.verificarNivel()

cidadeInicial(personagem)
fasePlanicies(personagem)
faseFloresta(personagem)
