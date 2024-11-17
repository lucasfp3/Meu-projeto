import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
df = pd.read_csv("gasolina.csv")

# Criar o gráfico de linha
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x="dia", y="venda", marker="o", label="Preço da Gasolina")
plt.title("Preço da Gasolina - São Paulo (Julho/2021)")
plt.xlabel("Dia")
plt.ylabel("Preço (R$)")
plt.grid(True)
plt.legend()

# Salvar o gráfico em gasolina.png
plt.savefig("gasolina.png")
