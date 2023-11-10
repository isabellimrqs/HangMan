import random

def desenhar_forca(erros):
    partes_forca = [
        "   ____\n  |    |\n      |\n      |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n      |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n  |    |\n      |\n      |\n",    #Desenho da forca
        "   ____\n  |    |\n  O    |\n /|    |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n      |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n /     |\n      |\n",
        "   ____\n  |    |\n  O    |\n /|\\   |\n / \\   |\n      |\n"
    ]
    return partes_forca[erros]

def ler_palavras_e_dicas():
    try:
        with open("palavras.txt", "r") as arquivo_palavras:
            palavras = [linha.strip() for linha in arquivo_palavras.readlines()]   #Abrir TXT de dicas e palavras
        with open("dicas.txt", "r") as arquivo_dicas:
            dicas = [linha.strip() for linha in arquivo_dicas.readlines()]

        return palavras, dicas
    except FileNotFoundError:
        print("Arquivo 'palavras.txt' ou 'dicas.txt' não encontrado.")
        exit(1)

def escolher_palavra_e_dica(palavras, dicas):
    indice = random.randint(0, len(palavras) - 1)
    palavra_secreta = palavras[indice]
    dica = dicas[indice]
    return palavra_secreta, dica

def ocultar_letras(palavra, letras_corretas):
    oculto = ""
    for letra in palavra:
        if letra in letras_corretas:
            oculto += letra
        else:
            oculto += "_"
    return oculto

def adicionar_palavra():
    nova_palavra = input("Digite a nova palavra: ").strip().lower()
    if nova_palavra:
        try:
            with open("palavras.txt", "a") as arquivo_palavras:
                arquivo_palavras.write(f"\n{nova_palavra}")
            print(f"A palavra '{nova_palavra}' foi adicionada com sucesso!")        #Adicionar nova palavra
        except Exception as e:
            print(f"Erro ao adicionar a palavra: {str(e)}")

palavras, dicas = ler_palavras_e_dicas()
letras_corretas = []
letras_erradas = []     #Armazena letras erradas
tentativas = 6          #Condições da forca
acertou = False

print("Bem-vindo ao Jogo da Forca! :)")

palavra_secreta, dica = escolher_palavra_e_dica(palavras, dicas)
print("Dica:", dica)

while tentativas > 0:
    print(desenhar_forca(6 - tentativas))

    palavra_oculta = ocultar_letras(palavra_secreta, letras_corretas)
    print("Palavra: ", palavra_oculta)

    letra = input("Digite uma letra ou 'adicionar' para incluir uma nova palavra: ").strip().lower()

    if letra == 'adicionar':
        adicionar_palavra()
        continue

    if letra in letras_corretas:
        print("Você já escolheu essa letra.")
        continue

    if letra in letras_erradas:
        print("Você já tentou esta letra e errou.")
        continue

    if letra in palavra_secreta:
        letras_corretas.append(letra)
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print(f"Letra {letra} não encontrada. Você tem {tentativas} tentativas restantes.")
        print("Letras erradas:", letras_erradas)

    if set(letras_corretas) == set(palavra_secreta):
        acertou = True
        break

if acertou:
    print(f"Parabéns! Você adivinhou a palavra: {palavra_secreta}")
else:
    print("Você perdeu. A palavra era:", palavra_secreta)
    print(desenhar_forca(6 - tentativas))
