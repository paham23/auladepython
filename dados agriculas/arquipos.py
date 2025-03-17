import pandas as pd 
dadoscriaçãodepeixes = pd.read_csv("dadoscriaçãodepeixes.csv")
print(dadoscriaçãodepeixes)
#criando um  grafico de pizza
import matplotlib.pyplot as plt
peixes = ["tambaqui", "matrixan", "jaraqui"]
retabilidade2024 = [500, 6000, 10000]
plt.figure(figsize=(8,8))
plt.pie(rentabilidade2024, labes=peixes, autopct="%.1f%%", colors=["blue", "red", "yellow"])
plt.title("rentabilidade2024 (%)")
plt.show()