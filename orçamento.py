def adicionar_entrada(lista, tipo):
    while True:
        nome = input(f"Digite o nome da {tipo} (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        try:
            valor = float(input(f"Digite o valor da {tipo} '{nome}': R$ "))
            categoria = input(f"Digite a categoria da {tipo} '{nome}': ")
            lista.append({'nome': nome, 'valor': valor, 'categoria': categoria})
        except ValueError:
            print("Valor inválido. Tente novamente.")


def mostrar_resumo(receitas, despesas):
    total_receitas = sum(item['valor'] for item in receitas)
    total_despesas = sum(item['valor'] for item in despesas)
    saldo = total_receitas - total_despesas

    print("\n🔹 RESUMO FINANCEIRO 🔹")
    print(f"Total de Receitas: R$ {total_receitas:.2f}")
    print(f"Total de Despesas: R$ {total_despesas:.2f}")
    print(f"Saldo Final: R$ {saldo:.2f}")
    print("Situação:", "✅ Positiva" if saldo >= 0 else "❌ Negativa")


def main():
    receitas = []
    despesas = []

    print("=== CALCULADORA DE ORÇAMENTO PESSOAL ===")

    print("\n--- Adicionar Receitas ---")
    adicionar_entrada(receitas, "receita")

    print("\n--- Adicionar Despesas ---")
    adicionar_entrada(despesas, "despesa")

    mostrar_resumo(receitas, despesas)


if __name__ == "__main__":
    main()
