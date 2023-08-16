# Despesas de Deputados Federais - Análise de Dados (2023)

Este repositório contém um aplicativo Streamlit para analisar e visualizar os dados de despesas de deputados federais no ano de 2023. O aplicativo carrega os dados de despesas de dois arquivos CSV e fornece visualizações interativas, incluindo gráficos de gastos totais, distribuição por UF (Unidade Federativa), gastos por partido e gastos por tipo de despesa.

## Pré-requisitos

Certifique-se de ter o Python instalado em seu ambiente e as bibliotecas Streamlit e Pandas. Você pode instalá-las usando o seguinte comando:

```bash
pip install streamlit pandas
```

## Como Executar

1. Clone este repositório para o seu ambiente local:

```bash
git clone https://github.com/Gabbyroba/Site-Deputados.git
```

2. Navegue até o diretório do repositório:

```bash
cd Site-Deputados
```

3. Execute o aplicativo Streamlit:

```bash
streamlit run main.py
```

O aplicativo será aberto no seu navegador padrão e você poderá interagir com as visualizações.

## Visão Geral do Código

O código contido neste repositório realiza as seguintes tarefas:

- Carrega os dados de despesas de deputados federais de dois arquivos CSV.
- Filtra e limpa os dados, removendo entradas com valores negativos.
- Calcula e exibe o valor líquido total das despesas.
- Apresenta visualizações interativas utilizando a biblioteca Streamlit.

O código é dividido em três seções principais:

1. **Configuração e Carregamento de Dados:** Importa as bibliotecas necessárias, lê os arquivos CSV e carrega os dados em DataFrames.

2. **Visualizações de Gráficos:** Utiliza a biblioteca Streamlit para criar visualizações interativas, incluindo:
   - Um treemap que mostra os gastos por UF.
   - Um gráfico de barras que exibe os gastos por partido.
   - Gráficos de barras agrupadas que mostram os gastos por tipo de despesa, agrupados por partido.

## Contribuições

Contribuições para melhorias e novas funcionalidades são bem-vindas! Se você encontrar problemas ou tiver sugestões, sinta-se à vontade para abrir uma **Issue** ou enviar um **Pull Request**.

## Agradecimentos

Este aplicativo foi desenvolvido usando a biblioteca Streamlit para visualizações interativas e a biblioteca Pandas para manipulação de dados. Agradecemos às comunidades dessas bibliotecas por tornar possível a criação deste projeto.

