# =============================================================================
# CALCULADORA DE IMPOSTOS BRASILEIROS - Módulo de Lógica
# Autor: ROGER EDUARDO DE AMORIM
# Data: Outubro 2025
# Copyright (c) 2025 ROGER EDUARDO DE AMORIM. Todos os direitos reservados.
# Propósito: Contém as funções de cálculo dos regimes tributários.
# =============================================================================

# --- CONSTANTES DE ALÍQUOTAS E MARGENS (Melhor legibilidade e manutenção) ---

# Alíquotas do Lucro Presumido (Regime Cumulativo)
PIS_ALIQUOTA_CUMULATIVO = 0.0065  # 0.65%
COFINS_ALIQUOTA_CUMULATIVO = 0.03   # 3.00%
IRPJ_ALIQUOTA_PRESUMIDO = 0.15     # 15%
CSLL_ALIQUOTA_PRESUMIDO = 0.09     # 9%

# Alíquotas do Lucro Real (Regime Não-Cumulativo)
PIS_ALIQUOTA_NAO_CUMULATIVO = 0.0165 # 1.65%
COFINS_ALIQUOTA_NAO_CUMULATIVO = 0.076 # 7.6%
IRPJ_ALIQUOTA_REAL = 0.15          # 15%
CSLL_ALIQUOTA_REAL = 0.09          # 9%

# Margens de Presunção para Lucro Presumido
MARGEM_PRESUNCAO = {"comercio": 0.08, "industria": 0.08, "servico": 0.32}


def calcular_simples_nacional(faturamento_anual: float, anexo: str = "I") -> dict:
    """
    Calcula o imposto mensal pelo Simples Nacional (versão inicial simplificada).
    O cálculo usa a fórmula: [(RBT12 * Alíquota) - Parcela a Deduzir] / 12 meses.
    """
    # Lista de faixas do Simples Nacional (Limite de Faturamento, Alíquota Efetiva, Parcela a Deduzir)
    faixas = [
        (180000.00, 0.04, 0.00),
        (360000.00, 0.073, 5940.00),
        (720000.00, 0.095, 13860.00),
        (1800000.00, 0.107, 22500.00),
        (3600000.00, 0.143, 87300.00),
        (4800000.00, 0.19, 378000.00)
    ]
    
    for limite, aliquota, deducao in faixas:
        if faturamento_anual <= limite:
            imposto = (faturamento_anual * aliquota - deducao) / 12
            return {"Regime": "Simples Nacional", "Anexo": anexo, "Imposto Mensal": round(imposto, 2)}

    # Retorna erro se o faturamento ultrapassar o limite máximo
    return {"Erro": "Faturamento acima do limite do Simples Nacional"}


def calcular_lucro_presumido(faturamento_trimestral: float, atividade: str = "comercio") -> dict:
    """
    Cálculo simplificado do Lucro Presumido, considerando IRPJ, CSLL, PIS e COFINS.
    """
    # Cálculo da Base de Cálculo Presumida (Faturamento * Margem de Presunção)
    base = faturamento_trimestral * MARGEM_PRESUNCAO.get(atividade, MARGEM_PRESUNCAO["comercio"])

    # Aplicação das alíquotas constantes
    irpj = base * IRPJ_ALIQUOTA_PRESUMIDO
    csll = base * CSLL_ALIQUOTA_PRESUMIDO
    pis = faturamento_trimestral * PIS_ALIQUOTA_CUMULATIVO
    cofins = faturamento_trimestral * COFINS_ALIQUOTA_CUMULATIVO

    total = irpj + csll + pis + cofins
    return {
        "Regime": "Lucro Presumido",
        "Atividade": atividade,
        "Imposto Trimestral": round(total, 2)
    }


def calcular_lucro_real(receita: float, despesas: float) -> dict:
    """
    Cálculo simplificado do Lucro Real (anual ou trimestral)
    A base de cálculo é o lucro líquido (Receita - Despesas Dedutíveis).
    """
    lucro_real = receita - despesas
    
    if lucro_real <= 0:
        return {"Regime": "Lucro Real", "Mensagem": "Prejuízo Fiscal - Sem IRPJ/CSLL"}
    
    # Aplicação das alíquotas constantes
    irpj = lucro_real * IRPJ_ALIQUOTA_REAL
    csll = lucro_real * CSLL_ALIQUOTA_REAL
    pis = receita * PIS_ALIQUOTA_NAO_CUMULATIVO
    cofins = receita * COFINS_ALIQUOTA_NAO_CUMULATIVO

    total = irpj + csll + pis + cofins
    return {
        "Regime": "Lucro Real",
        "Lucro": round(lucro_real, 2),
        "Imposto Total": round(total, 2)
    }