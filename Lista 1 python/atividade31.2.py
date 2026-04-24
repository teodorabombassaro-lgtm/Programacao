peso = float(input("Peso: "))
opcao = input("Deseja ver cenário de [A]umento ou [R]edução? ").upper()

if opcao == 'A':
    print(f"Novo peso (+15%): {peso * 1.15:.2f}kg")
elif opcao == 'R':
    print(f"Novo peso (-20%): {peso * 0.8:.2f}kg")