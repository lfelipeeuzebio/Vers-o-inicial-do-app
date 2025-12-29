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
        df['Ministros_Eucaristia'].str.contains(busca, case=False, na=False) |
        df['Purificação'].str.contains(busca, case=False, na=False) |
        df['Comunidade'].str.contains(busca, case=False, na=False)
    )

    df_filtrado = df[mask]

    if not df_filtrado.empty: 
        st.success("Aqui está sua escala:")

    df_mostrar = df_filtrado[['Data', 'Dia','Comunidade', 'Horário', 'Celebrante',  'Ministros_Eucaristia', 'Purificação']].copy()
    df_mostrar['Data'] = df_mostrar ['Data'].dt.strftime('%d/%m/%Y')

    st.dataframe(
            df_mostrar.style.background_gradient(cmap='Blues'),
            hide_index=True
        )

else: 
    st.warning("Nenhum dia encontrado, tente novamente!")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://github.com/lfelipeeuzebio/Vers-o-inicial-do-app/blob/a85fe1f94328fb2a21836e0213ddaa7bd486f5f5/fun_paroquia.jpeg");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"]::before {
    content: "";
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(0, 0, 0, 0.5);  
    pointer-events: none;
}

[data-testid="stAppViewContainer"] > * {
    position: relative;
    z-index: 1;
}

[data-testid="stHeader"] {
    background-color: rgba(0,0,0,0);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)








