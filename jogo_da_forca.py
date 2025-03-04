import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'forca', 'computador']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_acertadas):
    return ' '.join([letra if letra in letras_acertadas else '_' for letra in palavra])

def jogar():
    palavra = escolher_palavra()
    letras_acertadas = []
    tentativas = 6
    letras_erradas = []

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0:
        print(f"\nPalavra: {mostrar_palavra(palavra, letras_acertadas)}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras erradas: {' '.join(letras_erradas)}")
        
        # Solicitar uma letra do usuário
        palpite = input("Digite uma letra: ").lower()
        
        if palpite in letras_acertadas or palpite in letras_erradas:
            print("Você já tentou essa letra.")
            continue
        
        if palpite in palavra:
            letras_acertadas.append(palpite)
            print(f"Boa! A letra '{palpite}' está na palavra.")
        else:
            letras_erradas.append(palpite)
            tentativas -= 1
            print(f"Que pena! A letra '{palpite}' não está na palavra.")
        
        # Verificar se o jogador ganhou
        if all(letra in letras_acertadas for letra in palavra):
            print(f"\nParabéns! Você acertou a palavra: {palavra}")
            break
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

# Iniciar o jogo
jogar()
