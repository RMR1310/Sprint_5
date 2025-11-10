@"
# Análise de Veículos (Sprint 5)

Breve descrição: aplicação web em Streamlit para exploração e visualização de um dataset de anúncios de veículos usados nos EUA. Permite carregar o ficheiro CSV, inspecionar colunas e gerar gráficos interativos para análise exploratória.

Funcionalidades principais
- Leitura de `vehicles_us.csv` e verificação rápida de dimensões e colunas.
- Histograma do odómetro (odometer).
- Gráfico de dispersão preço vs odómetro (price vs odometer).
- Filtros básicos por ano do modelo, tipo e combustível (quando implementados).
- Execução local com Streamlit: visualização interativa e exportação/inspeção de subsets.

Como executar (ambiente Windows, PowerShell)
1. Ativar a virtualenv do projeto:
   - PowerShell (se necessário ajustar política):  
     Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force  
     .\.venv\Scripts\Activate.ps1
2. Instalar dependências (caso necessário):  
   python -m pip install -r requirements.txt
3. Executar a aplicação:  
   python -m streamlit run app.py

Estrutura do repositório
- app.py — aplicação principal Streamlit  
- streamlit_app.py — alternativa/auxiliar (se aplicável)  
- data/ ou ./ — local esperado do `vehicles_us.csv`  
- notebooks/ — análises exploratórias em Jupyter  
- requirements.txt — dependências do projeto

Notas e responsabilidades
- O ficheiro `vehicles_us.csv` deve estar presente em `C:\Users\<user>\Documents\Sprint_5\vehicles_us.csv` ou em `data/vehicles_us.csv` conforme o código.  
- Confirma a virtualenv ativa antes de correr a app para garantir que o Streamlit está acessível no ambiente correto.

Autor e contato
- Raphael — Sprint 5 (local).  

Licença
- MIT
"@ | Set-Content -Path .\README.md -Encoding utf8; Write-Output "README atualizado"
