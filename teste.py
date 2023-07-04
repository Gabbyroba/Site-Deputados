import pandas as pd
import streamlit as st
import plotly.figure_factory as ff

# Configurar título da página
st.set_page_config(page_title='Despesas Deputados Federais 2023')

# Ler arquivos e transformar em DF
df = pd.read_csv('despesasdepfinal.csv')
df2 = pd.read_csv('despesasdepfinalcopia.csv')

# Excluir colunas com valores negativos
df = df.drop([12636, 23040, 32069, 33479], axis='index')

# Função para carregar dados
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv('despesasdepfinal.csv')
    return tabela

# Função para carregar dados 2
@st.cache_data
def carregar_dados2():
    tabela2 = pd.read_csv('despesasdepfinalcopia.csv')
    return tabela2

# Somar valores da coluna valorLiquido
total_gastos = df['valorLiquido'].sum()

# Plotar um cartão com a soma
st.subheader('Valor Líquido')
st.info(f"R${total_gastos:.2f}")

with st.container():
    # Título e Separador
    st.subheader('Análise de dados DF - 2023')
    st.title('Gráficos')
    st.write('---')

with st.container():
    st.subheader('Dashboard Deputados')
    html_code = '''
        <div style="display: flex; justify-content: center;">
            <iframe title="dashboarddep" width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiYTIyNjA4MWMtMzZiZS00YmFmLWE4MDYtNzMwNTU3ZjE4MDQ2IiwidCI6Ijg0ODVhNDUyLWY5YjEtNGM0ZS04ODRlLWZiMGQzMWExNTMwZCJ9" frameborder="0" allowFullScreen="true"></iframe>
        </div>
    '''

    st.components.v1.html(html_code, height=600)

with st.container():
    # Calcular a contagem de ocorrência de cada siglaUF
    counts = df['siglaUF'].value_counts()

    # Criar um DataFrame com as informações
    df_treemap = pd.DataFrame({'siglaUF': counts.index, 'count': counts.values, 'valorLiquido': counts.values})

    # Função para formatar valores em "Milhões"
    def format_value(value):
        if value >= 1_000_000:
            return f"{value/1_000_000:.2f} Mi"
        return f"{value:.2f}"

    # Criar o treemap
    fig2 = {
        'data': [{
            'type': 'treemap',
            'labels': df_treemap['siglaUF'],
            'parents': [""] * len(df_treemap),
            'values': df_treemap['valorLiquido'],
            'text': df_treemap['valorLiquido'].apply(format_value),
            'textposition': "middle center",
            'hovertemplate': '<b>%{label}</b> <br> Valor: %{text}'
        }],
        'layout': {
            'title': 'Gastos por UF'
        }
    }

    # Exibir o gráfico no Streamlit
    st.plotly_chart(fig2, use_container_width=True)

    # Ordenar o DataFrame em ordem decrescente com base na coluna 'valorLiquido'
    df_sorted = df.sort_values('valorLiquido', ascending=False)

    # Dados para o gráfico de barras
    x = df_sorted['siglaPartido']
    y = df_sorted['valorLiquido']

    # Criar o gráfico de barras
    fig = {
        'data': [{
            'type': 'bar',
            'x': x,
            'y': y
        }],
        'layout': {
            'title': 'Gastos por partido',
            'xaxis': {'title': 'Sigla do Partido'},
            'yaxis': {'title': 'Valor das Despesas'},
            'barmode': 'group'
        }
    }

    # Plotar o gráfico usando Plotly
    st.plotly_chart(fig, use_container_width=True)

    # Dados para o gráfico de barras agrupadas
    x = df2['tipoDespesa']
    y = df2['valorLiquido']
    categories = df2['siglaPartido'].unique()

    # Criar gráfico de barras agrupadas
    fig = {
        'data': [],
        'layout': {
            'xaxis': {'title': 'Tipo de Despesa'},
            'yaxis': {'title': 'Valor Despesas'},
            'barmode': 'stack',
            'title': 'Gastos por Tipo de Despesa',
            'xaxis_tickangle': -45
        }
    }

    for partido in categories:
        partido_data = df2[df2['siglaPartido'] == partido]
        fig['data'].append({
            'type': 'bar',
            'x': x,
            'y': partido_data['valorLiquido'],
            'name': partido
        })

    # Plotar gráfico com plotly
    st.plotly_chart(fig, use_container_width=True)