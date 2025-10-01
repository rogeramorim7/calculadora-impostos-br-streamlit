# =============================================================================
# CALCULADORA DE IMPOSTOS BRASILEIROS - Streamlit App
# Autor: ROGER EDUARDO DE AMORIM
# Data: Outubro 2025
# Copyright (c) 2025 ROGER EDUARDO DE AMORIM. Todos os direitos reservados.
# Propósito: Interface interativa para simulação fiscal simplificada.
# =============================================================================

import streamlit as st
from calculadora_impostos import (
    calcular_simples_nacional,
    calcular_lucro_presumido,
    calcular_lucro_real
)

# --- Definição de Funções de Utilidade ---

def formatar_moeda(valor):
    """
    Função auxiliar para formatar um valor float para o formato de moeda brasileira (R$).
    Isso substitui o ponto decimal (padrão Python) pela vírgula e adiciona o separador de milhar.
    """
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# --- Configuração Inicial do Streamlit ---

st.set_page_config(page_title="Calculadora de Impostos", page_icon="💰")

st.title("💰 Calculadora de Impostos")
st.write("Simule rapidamente os impostos nos regimes: **Simples Nacional, Lucro Presumido e Lucro Real**.")

# --- Seleção do Regime Tributário (Radio Button) ---

opcao = st.radio("Escolha o regime tributário:", ["Simples Nacional", "Lucro Presumido", "Lucro Real"])


# --- Bloco de Cálculo: Simples Nacional ---

if opcao == "Simples Nacional":
    faturamento = st.number_input("Faturamento anual (R$)", min_value=0.0)
    
    if st.button("Calcular"):
        resultado = calcular_simples_nacional(faturamento)
        
        if "Erro" in resultado:
            st.error(resultado["Erro"])
        else:
            st.success(f"O valor aproximado do imposto mensal é **{formatar_moeda(resultado['Imposto Mensal'])}**.")
            
            st.markdown("""
            📘 **Base legal:** O cálculo segue a **Lei Complementar nº 123/2006 (Simples Nacional)**, 
            que define as alíquotas progressivas conforme o faturamento anual e o anexo escolhido.  
            """)


# --- Bloco de Cálculo: Lucro Presumido ---

elif opcao == "Lucro Presumido":
    faturamento = st.number_input("Faturamento trimestral (R$)", min_value=0.0)
    atividade = st.selectbox("Atividade", ["comercio", "industria", "servico"])
    
    if st.button("Calcular"):
        resultado = calcular_lucro_presumido(faturamento, atividade)
        
        st.success(f"O valor aproximado do imposto trimestral é **{formatar_moeda(resultado['Imposto Trimestral'])}**.")
        
        st.markdown("""
        📘 **Base legal:** O cálculo do **Lucro Presumido** é regulamentado pelo **Decreto nº 9.580/2018 (RIR/2018)**,
        que define as margens de presunção da receita (8% comércio/indústria, 32% serviços) e 
        aplica IRPJ, CSLL, PIS e COFINS.  
        """)


# --- Bloco de Cálculo: Lucro Real ---

elif opcao == "Lucro Real":
    receita = st.number_input("Receita total (R$)", min_value=0.0)
    despesas = st.number_input("Despesas dedutíveis (R$)", min_value=0.0)
    
    if st.button("Calcular"):
        resultado = calcular_lucro_real(receita, despesas)
        
        if "Mensagem" in resultado:
            st.warning(resultado["Mensagem"])
        else:
            st.success(f"O valor aproximado do imposto total é **{formatar_moeda(resultado['Imposto Total'])}**.")
            
            st.markdown("""
            📘 **Base legal:** O **Lucro Real** é regulamentado pelo **Decreto nº 9.580/2018 (RIR/2018)** e pela **Lei nº 9.430/1996**.  
            Nele, a base de cálculo é o **lucro líquido ajustado pelas adições e exclusões fiscais**, com aplicação de IRPJ (15%), CSLL (9%), PIS e COFINS (não cumulativos).
            """)