import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Função para carregar e processar o CSV
def carregar_csv():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos CSV", "*.csv")])
    
    if not arquivo:
        return
    
    try:
        df = pd.read_csv(arquivo)
        df["Preço"] = pd.to_numeric(df["Preço"], errors="coerce")
        df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors="coerce")
        
        # Calcular métricas
        receita_total = (df["Quantidade"] * df["Preço"]).sum()
        total_vendas = df["Quantidade"].sum()
        ticket_medio = receita_total / total_vendas if total_vendas > 0 else 0
        produto_mais_vendido = df.groupby("Produto")["Quantidade"].sum().idxmax()

        # Exibir resumo no Tkinter
        resumo_texto.set(f"Resumo das Vendas:\n"
                         f"Receita Total: R$ {receita_total:.2f}\n"
                         f"Total de Vendas: {total_vendas}\n"
                         f" Ticket Médio: R$ {ticket_medio:.2f}\n"
                         f" Produto Mais Vendido: {produto_mais_vendido}")
        
        # Criar gráfico de barras
        plotar_grafico(df)

    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao carregar CSV: {e}")

# Função para criar o gráfico
def plotar_grafico(df):
    for widget in frame_grafico.winfo_children():
        widget.destroy()
    
    df_grouped = df.groupby("Produto")["Quantidade"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(df_grouped["Produto"], df_grouped["Quantidade"], color="skyblue")
    ax.set_xlabel("Produto")
    ax.set_ylabel("Quantidade Vendida")
    ax.set_title("Vendas por Produto")
    ax.tick_params(axis="x", rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Criar a interface gráfica com Tkinter
root = tk.Tk()
root.title("Dashboard de Vendas")
root.geometry("600x500")

# Criar um botão para carregar o CSV
btn_carregar = tk.Button(root, text="📂 Carregar CSV", command=carregar_csv, font=("Arial", 12), bg="lightblue")
btn_carregar.pack(pady=10)

# Criar um label para mostrar o resumo
resumo_texto = tk.StringVar()
lbl_resumo = tk.Label(root, textvariable=resumo_texto, font=("Arial", 12), justify="left")
lbl_resumo.pack(pady=10)

# Criar um frame para o gráfico
frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=10, fill="both", expand=True)

# Iniciar a aplicação
root.mainloop()
