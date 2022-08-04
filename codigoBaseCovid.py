import pandas as pd #biblioteca para tratamento de dados
import plotly.express as px #biblioteca pra gráficos interativos
import streamlit as st #biblioteca pro front-end

#streamlit run codigoBase.py no terminal para rodar os módulos.

#Lendo o Dataset
df = pd.read_csv("https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv")

#melhorando o nome das colunas da tabela
df = df.rename(columns={'newDeaths': 'Novos Óbitos', 'NewCase' : 'Novos Casos', 'deaths_per_100k_inhabitants': 'Óbitos por 100 mil habitantes', 'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

#Seleção do Estado
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual Estado ?',estados)
#state = 'MS'

#Seleção da Coluna
#column = 'Casos por 100 mil habitantes'
colunas = ['Novos Óbitos', 'Novos Casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual dado demonstrar?',colunas)

#Seleção das linhas que pretencem ao estado
df = df[df['state'] == state]


fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de ecolher o estado e o tipo de informação para mostrar o gráfico. Utilize o menu lateral para escolher.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Os dados foram obtidos a partir do site: https://github.com/wcota/covid19br')
