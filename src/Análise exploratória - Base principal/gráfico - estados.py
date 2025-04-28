import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Lendo os dados (supondo que o arquivo está no mesmo diretório)
# Como o arquivo tem um formato específico, vou processar manualmente

# Extraindo os estados da coluna A (ignorando a primeira linha que é o cabeçalho)
with open('Pasta1 - referência.xlsx', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Processando os dados para extrair os estados
states = []
for line in lines[1:]:  # Pular o cabeçalho
    line = line.strip()
    if line and '(' in line and ')' in line:
        # Extrai o código do estado entre parênteses
        state_code = line[line.find('(')+1:line.find(')')]
        states.append(state_code)

# Contando a frequência de cada estado
state_counts = Counter(states)

# Convertendo para DataFrame para facilitar a visualização
df = pd.DataFrame.from_dict(state_counts, orient='index').reset_index()
df.columns = ['Estado', 'Quantidade']
df = df.sort_values('Quantidade', ascending=False)

# Criando o gráfico de barras
plt.figure(figsize=(12, 8))
bars = plt.bar(df['Estado'], df['Quantidade'], color='skyblue')

# Adicionando os valores em cima de cada barra
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom')

# Configurações do gráfico
plt.title('Distribuição por Estado', fontsize=16)
plt.xlabel('Estado', fontsize=14)
plt.ylabel('Quantidade', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Ajustando o layout para não cortar rótulos
plt.tight_layout()

# Mostrando o gráfico
plt.show()
