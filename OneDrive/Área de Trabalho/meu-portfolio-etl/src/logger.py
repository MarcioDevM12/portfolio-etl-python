# src\logger.py - Sistema de logging para Windows
import logging
import os
from datetime import datetime

def setup_logger(nome="etl_pipeline"):
    """Configura o sistema de logging"""
    
    # Criar pasta de logs se não existir
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    
    # Nome do arquivo com data
    data_atual = datetime.now().strftime("%Y%m%d")
    log_file = os.path.join(log_dir, f"{nome}_{data_atual}.log")
    
    # Configurar logger
    logger = logging.getLogger(nome)
    logger.setLevel(logging.DEBUG)
    
    # Evitar logs duplicados
    if not logger.handlers:
        # Handler para arquivo
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # Handler para console
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.INFO)
        
        # Adicionar handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Criar logger global
logger = setup_logger()

def log_inicio_processo(nome_processo):
    """Registra início de processo"""
    logger.info("=" * 50)
    logger.info(f"INICIANDO: {nome_processo}")
    logger.info("=" * 50)

def log_fim_processo(nome_processo, sucesso=True):
    """Registra fim de processo"""
    status = "SUCESSO" if sucesso else "FALHA"
    logger.info("=" * 50)
    logger.info(f"FINALIZADO: {nome_processo} - {status}")
    logger.info("=" * 50)