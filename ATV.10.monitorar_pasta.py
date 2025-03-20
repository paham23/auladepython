import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Pasta a ser monitorada
PASTA_MONITORADA = "arquivos_csv"

class MonitoradorCSV(FileSystemEventHandler):
    def on_created(self, event):
        """Executa quando um novo arquivo é adicionado à pasta."""
        if event.is_directory:
            return
        
        arquivo = event.src_path
        if arquivo.endswith(".csv"):
            print(f"Novo arquivo detectado: {arquivo}")
            processar_csv(arquivo)

def processar_csv(arquivo):
    """Lê o CSV, analisa e gera um relatório automático."""
    try:
        # 1️⃣ Ler o CSV
        df = pd.read_csv(arquivo)
        
        # 2️⃣ Calcular total vendido por produto
        df["Total_Vendido"] = df["Quantidade"] * df["Preço"]
        total_por_produto = df.groupby("Produto")["Total_Vendido"].sum().reset_index()

        # 3️⃣ Identificar o produto mais vendido
        produto_mais_vendido = total_por_produto.nlargest(1, "Total_Vendido")

        # 4️⃣ Salvar relatório em Excel
        nome_relatorio = "relatorio_vendas.xlsx"
        with pd.ExcelWriter(nome_relatorio) as writer:
            df.to_excel(writer, sheet_name="Vendas", index=False)
            total_por_produto.to_excel(writer, sheet_name="Total por Produto", index=False)
            produto_mais_vendido.to_excel(writer, sheet_name="Produto Mais Vendido", index=False)
        
        print(f"Relatório gerado: {nome_relatorio}")

    except Exception as e:
        print(f"Erro ao processar o CSV: {e}")

# 🔄 Iniciar monitoramento da pasta
if __name__ == "__main__":
    if not os.path.exists(PASTA_MONITORADA):
        os.makedirs(PASTA_MONITORADA)

    observador = Observer()
    evento_handler = MonitoradorCSV()
    observador.schedule(evento_handler, PASTA_MONITORADA, recursive=False)
    
    print(f"Monitorando a pasta: {PASTA_MONITORADA}...")
    observador.start()

    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        observador.stop()
        print("Monitoramento encerrado.")

    observador.join()
