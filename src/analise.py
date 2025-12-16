import pandas as pd
import os

COLUNAS_OBRIGATORIAS = [
    'data',
    'produto',
    'categoria',
    'quantidade',
    'valor_unitario'
]

def carregar_dados(nome_arquivo):
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        caminho = os.path.join(base_dir, '..', 'dados', nome_arquivo)

        df = pd.read_csv(caminho)

        if df.empty:
            raise ValueError("O arquivo CSV está vazio.")

        for coluna in COLUNAS_OBRIGATORIAS:
            if coluna not in df.columns:
                raise ValueError(f"Coluna obrigatória ausente: {coluna}")

        return df

    except FileNotFoundError:
        print("❌ Erro: arquivo de dados não encontrado.")
        return None

    except ValueError as erro:
        print(f"❌ Erro nos dados: {erro}")
        return None

def calcular_faturamento(df):
    df['faturamento'] = df['quantidade'] * df['valor_unitario']
    return df

def gerar_relatorio(df):
    faturamento_total = df['faturamento'].sum()
    produto_mais_vendido = df.groupby('produto')['quantidade'].sum().idxmax()
    faturamento_por_categoria = df.groupby('categoria')['faturamento'].sum()

    print("\n📊 RELATÓRIO DE VENDAS")
    print("-" * 30)
    print(f"Faturamento total: R$ {faturamento_total:.2f}")
    print(f"Produto mais vendido: {produto_mais_vendido}")
    print("\nFaturamento por categoria:")
    print(faturamento_por_categoria)

def main():
    df = carregar_dados('vendas.csv')

    if df is None:
        print("⛔ Execução interrompida.")
        return

    df = calcular_faturamento(df)
    gerar_relatorio(df)

if __name__ == "__main__":
    main()
