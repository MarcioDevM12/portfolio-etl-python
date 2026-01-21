# main.py - VERSÃO CORRIGIDA PARA WINDOWS
import sys
import os
import pandas as pd

print("=" * 60)
print("🚀 PIPELINE ETL COMPLETO - WINDOWS")
print("=" * 60)

# IMPORTANTE: Adicionar src ao path do Python
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_src = os.path.join(caminho_atual, 'src')
sys.path.insert(0, caminho_src)

print(f"📁 Caminho do projeto: {caminho_atual}")
print(f"📁 Caminho src: {caminho_src}")

# Tentar importar módulos
try:
    # Tente importar de duas formas diferentes
    try:
        # Método 1: Importar módulo completo
        import extract
        print("✅ Módulo 'extract' importado")
    except ImportError:
        # Método 2: Tentar importar funções específicas
        from extract import extrair_dados, extrair_com_escolha
        print("✅ Funções importadas diretamente")
    
    import transform
    import load
    print("✅ Todos os módulos carregados com sucesso!")
    
except ImportError as e:
    print(f"❌ ERRO CRÍTICO ao carregar módulos: {e}")
    print("\n📋 Verifique se existem estes arquivos:")
    print(f"   • {caminho_src}\\extract.py")
    print(f"   • {caminho_src}\\transform.py")
    print(f"   • {caminho_src}\\load.py")
    print(f"   • {caminho_src}\\__init__.py")
    
    # Listar arquivos na pasta src
    print(f"\n📁 Conteúdo da pasta src:")
    try:
        arquivos = os.listdir(caminho_src)
        for arq in arquivos:
            print(f"   • {arq}")
    except:
        print("   (Não foi possível listar a pasta)")
    
    input("\nPressione Enter para sair...")
    sys.exit(1)

def main():
    print("\n" + "=" * 40)
    print("ETAPA 1: EXTRAÇÃO")
    print("=" * 40)
    
    # VERIFICAÇÃO: A função existe?
    try:
        # Chamar a função corretamente
        df = extract.extrair_com_escolha()
    except AttributeError:
        print("⚠️  Função 'extrair_com_escolha' não encontrada no módulo")
        print("Usando 'extrair_dados' como fallback...")
        df = extract.extrair_dados()
    
    print(f"📥 Dados extraídos: {len(df)} registros")
    
    if df.empty:
        print("❌ Nenhum dado extraído. Encerrando.")
        input("Pressione Enter para sair...")
        return
    
    print("\nPrimeiras linhas dos dados:")
    print(df.head())
    
    print("\n" + "=" * 40)
    print("ETAPA 2: TRANSFORMAÇÃO")
    print("=" * 40)
    
    # Transformar dados
    try:
        df_transformado = transform.transformar_simples(df)
    except AttributeError:
        print("⚠️  Função 'transformar_simples' não encontrada")
        print("Aplicando transformação básica manualmente...")
        df_transformado = df.copy()
        if 'valor' in df.columns:
            df_transformado['status'] = df['valor'].apply(
                lambda x: 'ALTO' if x > 150 else 'BAIXO'
            )
        df_transformado['mensagem'] = 'Processado'
    
    print(f"🔄 Dados transformados: {len(df_transformado)} registros")
    print("\nDados após transformação:")
    print(df_transformado.head())
    
    # Calcular totais
    try:
        totais = transform.calcular_totais(df_transformado)
        print(f"\n📊 Estatísticas:")
        print(f"   • Total: {totais['total']}")
        print(f"   • Média: {totais['media']:.2f}")
        print(f"   • Quantidade: {totais['quantidade']}")
    except:
        print("\n⚠️  Não foi possível calcular estatísticas")
    
    print("\n" + "=" * 40)
    print("ETAPA 3: CARREGAMENTO")
    print("=" * 40)
    
    # Salvar arquivos
    try:
        csv_path, txt_path = load.salvar_arquivos(df_transformado)
        print(f"\n✅ Arquivos salvos com sucesso!")
        print(f"   • CSV: {csv_path}")
        print(f"   • TXT: {txt_path}")
    except Exception as e:
        print(f"❌ Erro ao salvar arquivos: {e}")
        print("Tentando salvar manualmente...")
        
        # Salvar manualmente
        os.makedirs("data\\output", exist_ok=True)
        csv_manual = "data\\output\\resultado_manual.csv"
        df_transformado.to_csv(csv_manual, index=False, encoding='utf-8-sig')
        print(f"   • CSV (manual): {csv_manual}")
    
    print("\n" + "=" * 60)
    print("✅ PIPELINE CONCLUÍDO!")
    print("=" * 60)
    
    # Perguntar se quer abrir a pasta
    resposta = input("\n📂 Abrir pasta de resultados? (s/n): ").lower()
    if resposta == 's':
        pasta_output = os.path.join(caminho_atual, "data", "output")
        os.system(f'explorer "{pasta_output}"')
    
    print("\n🎯 PRÓXIMOS PASSOS:")
    print("1. Verifique os arquivos em data\\output\\")
    print("2. Modifique extract.py para adicionar mais dados")
    print("3. Experimente criar suas próprias transformações")

if __name__ == "__main__":
    main()
    input("\n👋 Pressione Enter para finalizar...")