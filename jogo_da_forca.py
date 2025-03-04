import random

def escolher_palavra():
    palavras = ['computador', 'python', 'desenvolvimento', 'jogo', 'programacao']
    return random.choice(palavras)

def desenhar_boneco(tentativas_restantes):
    if tentativas_restantes == 6:
        print("  _______  ")
        print(" |       |  ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 5:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 4:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |       |  ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 3:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |      /|  ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 2:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |      /|\\ ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 1:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |      /|\\ ")
        print(" |      /   ")
        print(" |          ")
        print(" |          ")
    elif tentativas_restantes == 0:
        print("  _______  ")
        print(" |       |  ")
        print(" |       O  ")
        print(" |      /|\\ ")
        print(" |      / \\ ")
        print(" |          ")
        print(" |          ")
        print(" Você perdeu! ")
      

def jogar():
    palavra = escolher_palavra()
    letras_corretas = ['_'] * len(palavra)
    letras_erradas = []
    tentativas_restantes = 6
    
    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas_restantes > 0:
        print(f"\nPalavra: {' '.join(letras_corretas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        print(f"Letras erradas: {', '.join(letras_erradas)}")
        
        # Chama a função para desenhar o boneco com base nas tentativas restantes
        desenhar_boneco(tentativas_restantes)
        
        letra = input("Digite uma letra: ").lower()
        
        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    letras_corretas[i] = letra
            print(f"Boa! A letra '{letra}' está na palavra.")
        else:
            tentativas_restantes -= 1
            letras_erradas.append(letra)
            print(f"Ops! A letra '{letra}' não está na palavra.")
        
        if '_' not in letras_corretas:
            print(f"Parabéns! Você acertou a palavra: {palavra}")
            break

        else:
            print(f"\nVocê perdeu! A palavra era: {palavra}")
            
    else:
        desenhar_boneco(tentativas_restantes)
        

jogar()

