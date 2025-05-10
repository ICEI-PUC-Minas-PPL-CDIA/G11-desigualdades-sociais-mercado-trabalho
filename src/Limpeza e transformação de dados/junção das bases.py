import pandas as pd

# Caminhos dos arquivos
base_principal_path = "Base de dados principal TRATADA.xlsx"
base_auxiliar_path = "atributos - base auxliar.xlsx"

# Ler a base principal
df_principal = pd.read_excel(base_principal_path)

# Ler a base auxiliar (planilha correta com o IDH)
df_auxiliar = pd.read_excel(base_auxiliar_path, sheet_name="Planilha1")

# Renomear colunas da base auxiliar
df_auxiliar.columns = ["Estado", "IDH"]

# Renomear a coluna de estado na base principal para facilitar a junção
df_principal.rename(columns={df_principal.columns[5]: "Estado"}, inplace=True)

# Remover a sigla entre parênteses da coluna de Estado (ex: "Minas Gerais (MG)" → "Minas Gerais")
df_principal["Estado"] = df_principal["Estado"].str.extract(r'^(.*) \(')[0]

# Realizar o merge entre as bases pela coluna "Estado"
df_resultado = pd.merge(df_principal, df_auxiliar, on="Estado", how="left")

# Exportar o resultado final para novo arquivo Excel
df_resultado.to_excel("Base_com_IDH.xlsx", index=False)
