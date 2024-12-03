import random
import string

def gerar_senha(comprimento=12, incluir_maiusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase

    if incluir_maiusculas:
        caracteres += string.ascii_uppercase

    if incluir_numeros:
        caracteres += string.digits

    if incluir_simbolos:
        caracteres += string.punctuation

    senha = ''.join(random.choice(caracteres) for i in range(comprimento))

    return senha

def main():
    print("Bem-vindo ao Gerador de Senhas Aleatórias!")

    while True:
        comprimento_input = input("Digite o comprimento da senha (exemplo: 12): ").strip()

        if comprimento_input.isdigit():
            comprimento = int(comprimento_input)
            if comprimento >= 6 and comprimento <= 50:
                break 
            else:
                print("Por favor, digite um comprimento de senha entre 6 e 50 caracteres.")
        else:
            print("Por favor, digite um número inteiro válido para o comprimento da senha.")

    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_simbolos = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

    senha_gerada = gerar_senha(comprimento, incluir_maiusculas, incluir_numeros, incluir_simbolos)

    print(f"Sua senha gerada é: {senha_gerada}")

if __name__ == "__main__":
    main()
