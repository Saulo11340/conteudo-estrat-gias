import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Dados formatados para o padrão brasileiro, com sinal de %
formatted_data_with_percent = {
    "Brasil": ["80,85%", "10,64%", "2,13%", "4,26%", "2,13%"],
    "EUA": ["85,37%", "7,32%", "2,44%", "4,88%", "0,00%"],
    "UE": ["62,42%", "31,54%", "3,36%", "1,34%", "1,34%"]
}

# Tipos de cooperação
tipos_cooperacao = ["Multiatores", "Internacional", "Setor Público", "Acadêmico-Científica", "Setor Privado"]

# Dados numéricos para o mapa de calor
data = {
    "Brasil": [80.85, 10.64, 2.13, 4.26, 2.13],
    "EUA": [85.37, 7.32, 2.44, 4.88, 0.00],
    "UE": [62.42, 31.54, 3.36, 1.34, 1.34]
}

# Criando o DataFrame
df = pd.DataFrame(data, index=tipos_cooperacao)
df_formatted_with_percent = pd.DataFrame(formatted_data_with_percent, index=tipos_cooperacao)

# Criando o gráfico com as modificações
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=df_formatted_with_percent, cmap="YlOrRd", fmt="s")
plt.ylabel("Tipo de Cooperação")
plt.xlabel("País")
plt.show()
