import random

def escolher_palavra():
    palavras = ["python", "programacao", "computador", "inteligencia", "openai", "desenvolvimento"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_certas = []
    letras_erradas = []
    tentativas = 6
    
    print("Bem-vindo ao jogo da forca!")
    
    while True:
        palavra_escondida = ""
        for letra in palavra:
            if letra in letras_certas:
                palavra_escondida += letra
            else:
                palavra_escondida += "_"
        
        print("\nPalavra: " + palavra_escondida)
        print("Letras erradas: " + ", ".join(letras_erradas))
        print("Tentativas restantes: " + str(tentativas))
        
        if palavra_escondida == palavra:
            print("\nParabéns! Você ganhou!")
            break
        
        if tentativas == 0:
            print("\nGame over! A palavra era: " + palavra)
            break
        
        tentativa = input("\nDigite uma letra: ").lower()
        
        if len(tentativa) != 1 or not tentativa.isalpha():
            print("Por favor, digite apenas uma letra do alfabeto.")
            continue
        
        if tentativa in letras_certas or tentativa in letras_erradas:
            print("Você já tentou esta letra.")
            continue
        
        if tentativa in palavra:
            letras_certas.append(tentativa)
        else:
            letras_erradas.append(tentativa)
            tentativas -= 1

jogar_forca()
