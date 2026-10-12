
import random

opcoes = ["pedra", "papel", "tesoura"]

vitorias = 0
derrotas = 0
empates = 0

print("=== PEDRA, PAPEL E TESOURA ===")

while True:
    jogador = input(
        "\nEscolha pedra, papel ou tesoura (ou sair): "
    ).strip().lower()

    if jogador == "sair":
        break

    if jogador not in opcoes:
        print("Opção inválida!")
        continue

    computador = random.choice(opcoes)

    print(f"Você escolheu: {jogador}")
    print(f"Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
        empates += 1

    elif (
        (jogador == "pedra" and computador == "tesoura")
        or (jogador == "papel" and computador == "pedra")
        or (jogador == "tesoura" and computador == "papel")
    ):
        print("Você venceu!")
        vitorias += 1

    else:
        print("Você perdeu!")
        derrotas += 1

    print(
        f"Placar: Vitórias {vitorias} | "
        f"Derrotas {derrotas} | Empates {empates}"
    )

print("\n=== PLACAR FINAL ===")
print(f"Vitórias: {vitorias}")
print(f"Derrotas: {derrotas}")
print(f"Empates: {empates}")
print("Obrigado por jogar!")
