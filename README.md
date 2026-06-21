# Dashboard Interativo com Streamlit 

Este projeto consiste no desenvolvimento de um aplicativo web interativo utilizando Streamlit, com o objetivo de praticar conceitos fundamentais de engenharia de software aplicados ao contexto de dados. O aplicativo permite visualizar gráficos interativos (histograma e dispersão) a partir de um conjunto de dados em CSV.

O projeto inclui:
- criação e uso de ambiente virtual  
- análise exploratória em Jupyter Notebook  
- desenvolvimento de um dashboard com Streamlit  
- implantação do app na nuvem via Render  

## Funcionalidades do Aplicativo

O aplicativo web oferece:
- Cabeçalho descritivo  
- Botão para gerar histograma usando Plotly Express  
- Botão para gerar gráfico de dispersão  
- Alternativamente, caixas de seleção (`st.checkbox`) podem ser usadas para gerar gráficos sob demanda  
- Visualização interativa dos dados carregados a partir de um arquivo CSV  

## Conjunto de Dados

O projeto utiliza o arquivo:

vehicles_us.csv

Este dataset contém anúncios de vendas de carros nos EUA.  
Você pode substituí-lo por qualquer outro dataset em formato CSV, se desejar.

## Estrutura do Repositório

.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
├── notebooks
│   └── EDA.ipynb
└── .streamlit
    └── config.toml

## Análise Exploratória (EDA)

A análise exploratória foi realizada no arquivo:

notebooks/EDA.ipynb

Nele foram criados gráficos iniciais com Plotly Express para entender o comportamento das variáveis do dataset.

## Como Executar o Projeto Localmente

1. Criar ambiente virtual

python -m venv vehicles_env

2. Ativar o ambiente

Windows:
vehicles_env\Scripts\activate

Mac/Linux:
source vehicles_env/bin/activate

3. Instalar dependências

pip install -r requirements.txt

4. Executar o aplicativo Streamlit

streamlit run app.py

O app abrirá automaticamente no navegador.

## Deploy no Render

O aplicativo foi implantado no Render utilizando:

Build Command:
pip install --upgrade pip && pip install -r requirements.txt

Start Command:
streamlit run app.py

Arquivo obrigatório para compatibilidade:
.streamlit/config.toml

Link do aplicativo no Render:
(cole aqui quando estiver pronto)

## Tecnologias Utilizadas

- Python  
- Streamlit  
- Plotly Express  
- Pandas  
- Jupyter Notebook  
- Render (deploy)  

## Contato

LinkedIn: https://www.linkedin.com/in/raphael-reinhardt-b484ba37b  
Email: maxrapha13@gmail.com
