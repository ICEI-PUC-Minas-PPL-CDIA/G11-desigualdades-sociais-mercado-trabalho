# Corrigir nome da coluna de salário para facilitar manipulação
df.columns = [col[1] if isinstance(col, tuple) else col for col in df.columns]
df.rename(columns={"Salário  (R$)": "Salario"}, inplace=True)

# Verificar estatísticas descritivas para definir um critério de corte
salario_describe = df["Salario"].describe()

# Usar a mediana como critério estatístico para classificar entre Baixo e Alto
mediana_salario = salario_describe["50%"]

# Criar nova coluna com classificação
df["Salario_Classificacao"] = df["Salario"].apply(lambda x: "Alto" if x > mediana_salario else "Baixo")

# Salvar novo arquivo com classificação
output_path = "/mnt/data/Base_salario_classificado.xlsx"
df.to_excel(output_path, index=False)

import ace_tools as tools; tools.display_dataframe_to_user(name="Base com Classificação Salarial", dataframe=df)
