# src\extract.py - VERSÃO COMPLETA
import pandas as pd
import os

def extrair_dados(fonte="lista"):
    """Extrai dados de diferentes fontes"""
    
    print(f"🔍 Extraindo dados da fonte: {fonte}")
    
    if fonte == "csv":
        # Tentar ler do CSV
        csv_path = os.path.join("data", "input", "clientes.csv")
        if os.path.exists(csv_path):
            print(f"📄 Lendo dados de: {csv_path}")
            try:
                df = pd.read_csv(csv_path, encoding='utf-8-sig')
                print(f"✅ CSV carregado com {len(df)} registros")
                return df
            except Exception as e:
                print(f"❌ Erro ao ler CSV: {e}")
                print("Usando dados de exemplo como fallback...")
                return extrair_dados("lista")
        else:
            print("⚠️  Arquivo CSV não encontrado.")
            print(f"Procurando em: {csv_path}")
            print("Usando dados de exemplo...")
            return extrair_dados("lista")
    
    elif fonte == "lista":
        # Dados de exemplo
        print("📝 Usando dados de exemplo...")
        dados = [
            {"id": 1, "nome": "Maria Silva", "saldo": 1500.50, "cidade": "São Paulo"},
            {"id": 2, "nome": "João Santos", "saldo": 2500.00, "cidade": "Rio de Janeiro"},
            {"id": 3, "nome": "Ana Costa", "saldo": 3500.75, "cidade": "Belo Horizonte"},
            {"id": 4, "nome": "Carlos Lima", "saldo": 800.00, "cidade": "Porto Alegre"},
            {"id": 5, "nome": "Beatriz Souza", "saldo": 5200.25, "cidade": "Curitiba"},
        ]
        df = pd.DataFrame(dados)
        print(f"✅ {len(df)} registros de exemplo criados")
        return df
    
    else:
        print("⚠️  Fonte desconhecida. Usando dados de exemplo.")
        return extrair_dados("lista")

def extrair_com_escolha():
    """Pergunta ao usuário a fonte de dados"""
    print("\n📋 ESCOLHA A FONTE DE DADOS:")
    print("1. CSV (clientes.csv)")
    print("2. Dados de exemplo")
    print("3. Sair")
    
    while True:
        escolha = input("\nDigite 1, 2 ou 3: ").strip()
        
        if escolha == "1":
            return extrair_dados("csv")
        elif escolha == "2":
            return extrair_dados("lista")
        elif escolha == "3":
            print("Saindo...")
            return pd.DataFrame()  # DataFrame vazio
        else:
            print("❌ Opção inválida. Tente novamente.")