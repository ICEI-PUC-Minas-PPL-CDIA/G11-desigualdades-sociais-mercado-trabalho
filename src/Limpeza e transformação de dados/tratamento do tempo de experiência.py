import pandas as pd
import re
import math

# Carregar o arquivo Excel
file_path = "/mnt/data/tempo de experiência para tratamento.xlsx"
df = pd.read_excel(file_path)

# Função para extrair o menor valor da faixa e transformá-lo em número contínuo
def faixa_para_numero_continuo(valor):
    if isinstance(valor, str):
        match = re.search(r'(\d+)', valor)
        if match:
            return int(match.group(1))  # Pega o menor número da faixa
        elif "Menos de" in valor:
            return 0
        elif "Mais de" in valor:
            match = re.search(r'Mais de (\d+)', valor)
            if match:
                return int(match.group(1))
        elif "Não tenho experiência" in valor:
            return 0
    return None

# Aplicar a função na coluna de faixa de experiência (assumindo que seja a primeira coluna)
df[df.columns[0]] = df[df.columns[0]].apply(faixa_para_numero_continuo)

# Salvar em novo arquivo Excel
output_path = "/mnt/data/tempo_experiencia_tratado.xlsx"
df.to_excel(output_path, index=False)
