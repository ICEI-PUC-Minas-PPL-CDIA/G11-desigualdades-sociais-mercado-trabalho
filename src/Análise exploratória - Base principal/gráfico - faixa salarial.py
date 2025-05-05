import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Dados da tabela
data = {
    "Faixa Salarial": [
        "Menos de R$ 1.000/mês",
        "de R$ 1.001/mês a R$ 2.000/mês",
        "de R$ 2.001/mês a R$ 3.000/mês",
        "de R$ 3.001/mês a R$ 4.000/mês",
        "de R$ 4.001/mês a R$ 6.000/mês",
        "de R$ 6.001/mês a R$ 8.000/mês",
        "de R$ 8.001/mês a R$ 12.000/mês",
        "de R$ 12.001/mês a R$ 16.000/mês",
        "de R$ 16.001/mês a R$ 20.000/mês",
        "de R$ 20.001/mês a R$ 25.000/mês",
        "de R$ 25.001/mês a R$ 30.000/mês",
        "de R$ 30.001/mês a R$ 40.000/mês",
        "Acima de R$ 40.001/mês"
    ],
    "Quantidade": [
        30, 215, 288, 352, 745, 637, 1026,
        650, 419, 195, 128, 86, 72
    ]
}

# Criar o DataFrame
df = pd.DataFrame(data)

# Estilo do Seaborn
sns.set(style="whitegrid")

# Criar o gráfico
plt.figure(figsize=(10, 8))
barplot = sns.barplot(
    x="Quantidade", 
    y="Faixa Salarial", 
    data=df,
    palette="viridis"
)

# Títulos e rótulos
plt.title("Distribuição por Faixa Salarial", fontsize=16)
plt.xlabel("Quantidade de Pessoas")
plt.ylabel("Faixa Salarial")

# Exibir o gráfico
plt.tight_layout()
plt.show()

