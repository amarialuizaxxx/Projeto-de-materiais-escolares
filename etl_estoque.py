import pandas as pd

# 1️⃣ EXTRAÇÃO — Ler o arquivo CSV
df = pd.read_csv("estoque.csv")

print("=== DADOS ORIGINAIS ===")
print(df)
print("\n")

# 2️⃣ TRANSFORMAÇÃO — Limpeza, filtro e criação de métricas

# a) Remover linhas com valores nulos
df = df.dropna()

# b) Filtrar produtos com quantidade abaixo de 20 (baixa quantidade)
estoque_baixo = df[df["quantidade"] < 20]

# c) Criar uma nova coluna: valor_total (quantidade × preço)
df["valor_total"] = df["quantidade"] * df["preco"]

print("=== ESTOQUE COM VALOR TOTAL ===")
print(df)
print("\n")

print("=== PRODUTOS COM BAIXO ESTOQUE (menos de 20 unidades) ===")
print(estoque_baixo)
print("\n")

# 3️⃣ CARREGAMENTO — Salvar resultado final
df.to_csv("estoque_transformado.csv", index=False)
estoque_baixo.to_csv("estoque_baixo.csv", index=False)

print("Arquivos gerados com sucesso:")
print("- estoque_transformado.csv")
print("- estoque_baixo.csv")