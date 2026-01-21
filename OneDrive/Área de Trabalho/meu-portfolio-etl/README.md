# 🏦 Pipeline ETL com Python - Projeto de Portfólio

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![ETL](https://img.shields.io/badge/ETL-Pipeline-green)
![Status](https://img.shields.io/badge/Status-Concluído-success)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-black)

> Pipeline ETL completo desenvolvido em Python para processamento de dados financeiros, demonstrando habilidades em engenharia de dados e ciência de dados.

## 📋 Índice
- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias](#-tecnologias)
- [Instalação](#-instalação)
- [Uso](#-uso)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Exemplo de Saída](#-exemplo-de-saída)
- [Autor](#-autor)
- [Licença](#-licença)

## 🎯 Visão Geral

Este projeto implementa um pipeline ETL (Extract, Transform, Load) completo para processamento de dados de clientes bancários. Desenvolvido como parte de um curso/projeto de portfólio, demonstra habilidades práticas em:

- **Extração** de dados de múltiplas fontes
- **Transformação** com lógica de negócio complexa
- **Carregamento** em diferentes formatos
- **Tratamento de erros** robusto
- **Logging** profissional

## ✨ Funcionalidades

### 📥 Extração (Extract)
- Leitura de arquivos CSV/Excel com encoding correto para Windows
- Geração de dados fictícios para testes
- Sistema de fallback automático
- Validação de arquivos de entrada

### 🔄 Transformação (Transform)
- Classificação de clientes por faixa de saldo
- Cálculo de métricas financeiras
- Geração de mensagens personalizadas
- Adição de metadados (timestamp, status processamento)

### 📤 Carregamento (Load)
- Exportação para múltiplos formatos (CSV, JSON, TXT)
- Geração de relatórios textuais completos
- Organização automática em pastas com timestamp
- Backup de dados processados

### 🛡️ Recursos Avançados
- Sistema de logging profissional com rotação
- Tratamento robusto de erros em todas as etapas
- Interface interativa via linha de comando
- Código modular e altamente reutilizável

## 🛠️ Tecnologias

- **Python 3.9+** - Linguagem principal
- **Pandas** - Manipulação de dados
- **Git** - Controle de versão
- **Windows OS** - Ambiente de desenvolvimento

## 📦 Instalação

### Pré-requisitos
- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/portfolio-etl-python.git
cd portfolio-etl-python