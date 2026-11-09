import streamlit as st
import pandas as pd
import plotly.express as px

if __name__ == '__main__':
    st.set_page_config(page_title="Top 500 Albuns", layout="wide")

    col_ind1, col_ind2, col_ind3 = st.columns([1, 2, 1])
    with col_ind2:
        st.image("image.png")

    st.divider()
    st.title('DASHBOARD | The 500 Greatest Albuns of All Time', text_alignment='center')

    tab1, tab2, tab3 = st.tabs([
            '🏠: Início', 
            '📊: Visualizações', 
            '⏳: Visão Anual'     
    ])

    df = pd.read_csv('../data/500_best_albums.csv')
        
    num_artistas = df['artist'].nunique()
    num_generos = df['genre'].nunique()
    num_anos = df['year'].nunique()


    with tab1:
        text_col1, text_col2, text_col3 = st.columns([1, 0.05, 0.6])

        with text_col1:
            st.markdown('''
            ### Introdução

            A *Rolling Stone* é uma revista famosa, fundada nos Estados Unidos em 1967, com foco em música, política e cultura pop. Ela também é conhecida por suas compilações envolvendo música, e uma das mais discutidas é a sua lista dos 500 maiores álbuns de todos os tempos (ou *The 500 Greatest Albuns of All Time*), que compila álbuns com impacto artístico, comercial e cultural na música popular. Foi criada originalmente em 2003, mas passou por revisões em 2012, 2020 e 2023, visando incluir mais álbuns de pop, hip-hop, R&B/soul e música latina.

            O dataset *The 500 Greatest Albuns of All Time* compila a versão mais recente da lista da *Rolling Stone* em formato .csv, e é utilizado para esse trabalho de análise de dados.''')

            st.divider()

            st.markdown('''
            ### Objetivos

            Para explorar e analisar devidamente os dados dessa lista, isso é feito considerando como objetivo principal obter as respostas das seguintes perguntas:

            - Qual é o artista que mais aparece no dataset?
            - Qual o gênero musical mais frequente no dataset? 
            - Como os álbuns se concentram por ano?

            Para obter essas respostas e outras informações, foram gerados os seguintes gráficos:
            - Top 10 artistas mais frequentes (Gráfico de barras)
            - Top 10 gêneros mais frequentes (Gráfico de barras)
            - Relação entre número de músicas e duração do álbum (_Scatterplot_)
            - Contagem de álbuns por ano (Gráfico de barras)
            - Contagem de álbuns no tempo por gênero musical (Gráfico de barras interativo por ano e total)
            
            ''')

        with text_col3:
            st.image('magazine.png')
            st.image('n1.png')

    with tab2:
        col1, col2, col3 = st.columns(3)
        col1.metric('Número de artistas', num_artistas, border=True)
        col2.metric('Número de gêneros', num_generos, border=True)
        col3.metric('Número de anos', num_anos, border=True)

        st.divider()

    
    
        clna1, clna2 = st.columns(2)

        with clna1:
            artistas = df['artist'].value_counts().head(10)

            fig = px.bar(
                artistas,
                title="Top 10 artistas mais frequentes",
                orientation='h',
                color_discrete_sequence=['#ed1c24']
            )

            fig.update_layout(yaxis={'categoryorder':'total ascending'})

            st.plotly_chart(fig)       

        with clna2:


            generos = df['genre'].value_counts().head(10)

            fig3 = px.bar(
                generos,
                title="Top 10 gêneros mais frequentes",
                orientation='h',
                color_discrete_sequence=['#ed1c24']
            )

            fig3.update_layout(
                yaxis={'categoryorder': 'total ascending'},     
            )

            st.plotly_chart(fig3)


        fig4 = px.scatter(
                        df,
                        x='number_of_songs',
                        y='durations_in_seconds',
                        color='genre',
                        hover_data=['artist', 'genre'],
                        title='Relação de número de músicas por duração de álbum',
                        labels={
                            'number_of_songs': 'Número de Músicas',
                            'durations_in_seconds': 'Duração Total (segundos)',
                            'genre': 'Gênero'
                        },
                    )
        
        st.plotly_chart(fig4)
         
        

        st.divider()

    with tab3:
        col1, col2, col3 = st.columns(3)
        col1.metric('Número de artistas', num_artistas, border=True)
        col2.metric('Número de gêneros', num_generos, border=True)
        col3.metric('Número de anos', num_anos, border=True)

        st.divider()

        anos = df['year'].value_counts().sort_index()
        
        fig1 = px.bar(
            anos,
            title="Contagem de álbuns por ano",
            color_discrete_sequence=['#ed1c24']
        )

        st.plotly_chart(fig1)

        st.divider()

        generos = df['genre'].unique()
        genero_escolhido = st.selectbox('Escolha um gênero musical:', generos)

        df_ge = df[df['genre'] == genero_escolhido]

        # Plotando grafico para o genero escolhido:
        anos_ge = df_ge['year'].value_counts().sort_index()
        fig5 = px.bar(
                    anos_ge,
                    title="Contagem de álbuns no tempo por gênero musical",
                    color_discrete_sequence=['#ed1c24']
                )
        
        st.plotly_chart(fig5)
