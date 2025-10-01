💰 Calculadora de Impostos ME/EPP (Simples Nacional, Presumido e Real)
<p align="center">
<img src="https://github.com/rogeramorim7/calculadora-impostos-br-streamlit/blob/main/assets/github.gif" alt="Screenshot da Calculadora de Impostos em Streamlit" width="700">
</p>

🚀 Propósito do Projeto:
Este projeto é uma Calculadora de Impostos interativa desenvolvida em Python com Streamlit, destinada a simular de forma simplificada a carga tributária em três dos principais regimes fiscais brasileiros: Simples Nacional, Lucro Presumido e Lucro Real.

Seu principal objetivo é servir como peça de portfólio, demonstrando proficiência em:

Desenvolvimento Web Rápido: Utilizando o Streamlit para criar uma interface de usuário funcional.

Modularização e Boas Práticas Python: Uso de funções, tipagem de dados (type hinting) e separação clara da lógica (calculadora_impostos.py) da interface (app.py).

Modelagem de Lógica de Negócio (Fiscal): Codificando as regras simplificadas de cálculo baseadas nas legislações vigentes.

✨ Funcionalidades
O aplicativo permite ao usuário selecionar o regime e inserir dados específicos para obter uma estimativa de imposto:

Regime Selecionado	Base de Cálculo	Saída Estimada
Simples Nacional	Faturamento Anual	Imposto Mensal
Lucro Presumido	Faturamento Trimestral e Tipo de Atividade	Imposto Trimestral
Lucro Real	Receita Total e Despesas Dedutíveis	Imposto Total

🛠️ Tecnologias Utilizadas
Ferramenta	Descrição
Python	Linguagem principal de back-end e desenvolvimento.
Streamlit	Framework de desenvolvimento front-end para Python.
Git & GitHub	Controle de versão e hospedagem do repositório.

⚙️ Como Executar o Projeto Localmente
Pré-requisitos
Certifique-se de ter o Python 3.8+ instalado em sua máquina.

1. Clonar o Repositório

Bash
# Substitua rogeramorim7 pelo seu nome de usuário e o nome do repositório, se for diferente
git clone https://github.com/rogeramorim7/calculadora-impostos-br-streamlit.git
cd calculadora-impostos-br-streamlit

2. Configurar o Ambiente
Recomendamos o uso de um ambiente virtual para isolar as dependências do projeto.

Bash
# Cria e ativa o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
.\venv\Scripts\activate   # Windows

3. Instalar as Dependências
O projeto utiliza apenas a biblioteca streamlit. Você pode instalar usando o requirements.txt (que deve ter sido criado):

Bash
pip install -r requirements.txt

4. Rodar o Aplicativo
Execute o arquivo principal com o Streamlit:
Bash
streamlit run app.py

O aplicativo será aberto automaticamente no seu navegador padrão, no endereço: http://localhost:8501.

⚠️ Isenção de Responsabilidade (Disclaimer)
Os cálculos neste projeto são simulações simplificadas e didáticas, criadas exclusivamente para fins de demonstração de portfólio.
Eles não consideram o Fator R (Simples Nacional), adicional de IRPJ, diferenças estaduais (ICMS) ou municipais (ISS), e outras particularidades fiscais.
Este projeto não deve ser usado como base para tomada de decisão fiscal ou contábil real. Consulte sempre um contador profissional para cálculos precisos.

🤝 Conclusão e Convite
Este projeto representa o ponto final de um esforço que uniu lógica de negócios (fiscal) e desenvolvimento moderno em Python com Streamlit.

Se você gostou da iniciativa, sinta-se à vontade para deixar uma estrela (star) no repositório. O feedback, sugestões de melhoria ou oportunidades de colaboração são sempre muito bem-vindos!

Fique à vontade para entrar em contato:
Linkedin https://www.linkedin.com/in/roger-de-amorim-300a14307/
Instagram https://www.instagram.com/rogerdeamorim_/
