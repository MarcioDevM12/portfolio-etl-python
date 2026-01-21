# src\transform.py
import pandas as pd

def transformar_simples(df):
    """Transformação básica dos dados"""
    print("🔄 Aplicando transformações...")
    
    if df.empty:
        print("⚠️  DataFrame vazio, retornando vazio")
        return df
    
    df_transformado = df.copy()
    
    # Verificar colunas disponíveis
    colunas = list(df.columns)
    print(f"📊 Colunas disponíveis: {colunas}")
    
    # Adicionar coluna de status baseada em saldo ou valor
    if 'saldo' in colunas:
        print("💰 Classificando por saldo...")
        df_transformado['status_saldo'] = df_transformado['saldo'].apply(
            lambda x: 'ALTO' if x > 3000 else 'MÉDIO' if x > 1000 else 'BAIXO'
        )
    
    if 'valor' in colunas:
        print("💰 Classificando por valor...")
        df_transformado['status_valor'] = df_transformado['valor'].apply(
            lambda x: 'ALTO' if x > 150 else 'BAIXO'
        )
    
    # Adicionar mensagem
    if 'nome' in colunas:
        df_transformado['mensagem'] = df_transformado['nome'].apply(
            lambda nome: f"Olá {nome}! Seus dados foram processados."
        )
    else:
        df_transformado['mensagem'] = 'Processado com sucesso'
    
    # Adicionar timestamp
    from datetime import datetime
    df_transformado['processado_em'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"✅ {len(df_transformado)} registros transformados")
    return df_transformado

def calcular_totais(df):
    """Calcula totais e médias"""
    print("📈 Calculando estatísticas...")
    
    resultados = {
        'quantidade': len(df)
    }
    
    if 'saldo' in df.columns:
        resultados['total_saldo'] = df['saldo'].sum()
        resultados['media_saldo'] = df['saldo'].mean()
        resultados['max_saldo'] = df['saldo'].max()
        resultados['min_saldo'] = df['saldo'].min()
    
    if 'valor' in df.columns:
        resultados['total_valor'] = df['valor'].sum()
        resultados['media_valor'] = df['valor'].mean()
    
    if 'idade' in df.columns:
        resultados['media_idade'] = df['idade'].mean()
    
    print(f"📊 Estatísticas calculadas: {len(resultados)} métricas")
    return resultados