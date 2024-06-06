from datetime import date

def calcular_idade(ano_nascimento):
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = int(input("Digite o ano de seu nascimento (entre 1922 e 2021): "))

    if ano_nascimento < 1922 or ano_nascimento > 2021:
        print("Ano de nascimento inválido. Por favor, digite um ano entre 1922 e 2021.")
        return

    idade = calcular_idade(ano_nascimento)
    print(f"Olá, {nome_completo}! Você completou ou completará {idade} anos em 2024.")

if __name__ == "__main__":
    main()
