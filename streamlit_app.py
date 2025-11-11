# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("App principal - Sprint 5")
st.header("Análise de Veículos")
st.write("Esta é a app principal. Veja se o CSV processado está disponível em data/vehicles_processed.csv")

try:
    df = pd.read_csv("data/vehicles_processed.csv", encoding="utf-8")
    st.write(f"CSV carregado com sucesso  linhas: {len(df)}")
    st.dataframe(df.head(5))

    hist_button = st.button("Criar histograma")
    if hist_button:
        st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros")
        fig = px.histogram(df, x="odometer", nbins=50, title="Distribuição de Odômetro")
        st.plotly_chart(fig, use_container_width=True)

    scatter_button = st.button("Criar gráfico de dispersão")
    if scatter_button:
        st.write("Criando um gráfico de dispersão entre preço e odômetro")
        df_plot = df[['price','odometer']].dropna().head(1000)
        if not df_plot.empty:
            fig = px.scatter(df_plot, x='odometer', y='price', title='Preço vs Odômetro (amostra)', trendline='ols')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Não há dados suficientes para desenhar o gráfico de dispersão")
except Exception as e:
    st.error(f"Erro ao carregar CSV: {e}")
