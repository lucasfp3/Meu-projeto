import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv("gasolina.csv")

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="dia", y="venda", marker="o", label="Preço da Gasolina", color="blue")

# Configurações do gráfico
plt.title("Evolução do Preço da Gasolina em São Paulo - Julho/2021", fontsize=16)
plt.xlabel("Dias", fontsize=12)
plt.ylabel("Preço Médio (R$)", fontsize=12)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title="Legenda", fontsize=10)

# Salvar o gráfico como gasolina.png
plt.savefig("gasolina.png")

# Exibir o gráfico (opcional no ambiente local)
plt.show()
