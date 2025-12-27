import pandas as pd
import streamlit as st

st.title("Escala Mensal - Paróquia Nossa Senhora Medianeira")

st.markdown("Digite seu nome para ver os dias em que está escalado.")

try:
    df = pd.read_excel("escala_medianeira.xlsx")
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
    #st.success("Planilha carregada")
except FileNotFoundError:
    st.error ("Arquivo não encontrado! Contate o coordenador.")
    st.stop()
except Exception as e:
    st.error(f"Erro ao carregar {e}")
    st.stop()

busca = st.text_input("Digite seu nome para consultar a escala")

if busca:
    mask= (
        df['Celebrante'].str.contains(busca, case=False, na=False) |
        df['Ministros_Eucaristia'].str.contains(busca, case=False, na=False)
    )

    df_filtrado = df[mask]

    if not df_filtrado.empty: 
        st.success("Aqui está sua escala:")

    df_mostrar = df_filtrado[['Data', 'Comunidade', 'Horário', 'Celebrante', 'Ministros_Eucaristia']].copy()
    df_mostrar['Data'] = df_mostrar ['Data'].dt.strftime('%d/%m/%Y')

    st.dataframe(
            df_mostrar.style.background_gradient(cmap='Blues')  # Destaque azul
        )

else: 
    st.warning("Nenhum dia encontrado, tente novamente!")

