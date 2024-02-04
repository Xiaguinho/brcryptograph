import random
import string

def generate_key(seed, difficulty, tamanho):
    random.seed(seed)
    
    if difficulty == '1':
        characters = string.digits  # Apenas números
    elif difficulty == '2':
        characters = string.ascii_lowercase  # Apenas letras minúsculas
    elif difficulty == '3':
        characters = string.ascii_uppercase  # Apenas letras maiúsculas
    elif difficulty == '4':
        characters = string.ascii_letters  # Letras minúsculas + letras maiúsculas
    elif difficulty == '5':
        characters = string.ascii_letters + string.digits  # Letras + números
    elif difficulty == '6':
        characters = string.printable  # Letras + números + caracteres especiais
    else:
        raise ValueError("Dificuldade não reconhecida.")

    key = {}
    for char in characters:
        key[char] = ''.join(random.choice(characters) for _ in range(tamanho))
    return key

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        encrypted_message += key.get(char, char)
    return encrypted_message

seed = input("Digite a chave: ")

modo = input("""Escolha o modo
[1] Criptografar
: """).lower()

tamanho = int(input("Escolha quantos caracteres a criptografia vai ter: "))

dificuldade = input("""Escolha a dificuldade
[1] Numeros
[2] Letras minusculas
[3] Letras maiusculas
[4] Letras minusculas + letras maiúsculas
[5] Letras minusculas + letras maiúsculas + números
[6] Letras minusculas + letras maiúsculas + números + caracteres especiais
: """)

mensagem = input("Digite a mensagem: ")

key = generate_key(seed, dificuldade, tamanho)

if modo == "1" or modo == "criptografar":
    mensagem_criptografada = encrypt(mensagem, key)
    print("Mensagem Criptografada:", mensagem_criptografada)
else:
    print("Modo não reconhecido. Escolha '1' para criptografar ou '2' para descriptografar.")

# Adiciona uma pausa antes de encerrar
input("Pressione Enter para sair.")