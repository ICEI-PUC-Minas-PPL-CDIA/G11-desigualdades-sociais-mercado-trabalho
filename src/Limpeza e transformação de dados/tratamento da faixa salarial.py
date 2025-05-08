import pandas as pd
import re

# Caminho do arquivo original
file_path = "/mnt/data/faixa salarial para tratamento .xlsx"

# Carrega o arquivo Excel
df = pd.read_excel(file_path)

# Renomeia a coluna para facilitar
df.columns = ['Faixa salarial']

# Função que extrai a média da faixa salarial
def extrair_media(faixa):
    # Remove pontos e extrai os números
    numeros = list(map(int, re.findall(r'\d+', faixa.replace('.', ''))))
    if len(numeros) == 2:
        media = sum(numeros) // 2
    elif len(numeros) == 1:
        media = numeros[0]
    else:
        return None
    return media

# Aplica a função para calcular o salário médio
df['Salário Médio (R$)'] = df['Faixa salarial'].apply(extrair_media)

# Caminho do novo arquivo
output_path = "/mnt/data/faixa_salarial_convertida.xlsx"

# Salva o novo DataFrame em um arquivo Excel
df.to_excel(output_path, index=False)
