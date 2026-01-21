# src\load.py
import pandas as pd
import os
from datetime import datetime

def salvar_arquivos(df, pasta="data\\output"):
    """Salva dados em diferentes formatos"""
    
    print("💾 Iniciando salvamento de arquivos...")
    
    # Criar pasta se não existir
    os.makedirs(pasta, exist_ok=True)
    
    # Gerar timestamp para nome único
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Salvar CSV (compatível com Excel no Windows)
    csv_path = os.path.join(pasta, f"resultado_{timestamp}.csv")
    try:
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')
        print(f"✅ CSV salvo: {csv_path}")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {e}")
        csv_path = None
    
    # Salvar TXT com relatório
    txt_path = os.path.join(pasta, f"relatorio_{timestamp}.txt")
    try:
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("=" * 50 + "\n")
            f.write("RELATÓRIO DO PROCESSAMENTO ETL\n")
            f.write("=" * 50 + "\n\n")
            
            f.write(f"Data/hora: {timestamp}\n")
            f.write(f"Total de registros: {len(df)}\n\n")
            
            f.write("COLUNAS DISPONÍVEIS:\n")
            for col in df.columns:
                f.write(f"  • {col}\n")
            
            f.write("\nESTATÍSTICAS:\n")
            if 'saldo' in df.columns:
                f.write(f"  • Saldo total: R${df['saldo'].sum():.2f}\n")
                f.write(f"  • Saldo médio: R${df['saldo'].mean():.2f}\n")
            
            if 'idade' in df.columns:
                f.write(f"  • Idade média: {df['idade'].mean():.1f} anos\n")
            
            f.write("\nPRIMEIRAS 5 LINHAS:\n")
            f.write(df.head().to_string())
        
        print(f"✅ Relatório TXT salvo: {txt_path}")
    except Exception as e:
        print(f"❌ Erro ao salvar TXT: {e}")
        txt_path = None
    
    # Salvar JSON (opcional)
    json_path = os.path.join(pasta, f"dados_{timestamp}.json")
    try:
        df.to_json(json_path, orient='records', indent=2, force_ascii=False)
        print(f"✅ JSON salvo: {json_path}")
    except Exception as e:
        print(f"⚠️  Não foi possível salvar JSON: {e}")
        json_path = None
    
    print(f"🎯 Total de arquivos salvos: {sum([csv_path is not None, txt_path is not None, json_path is not None])}")
    
    return csv_path, txt_path