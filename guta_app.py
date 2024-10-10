import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Título da aplicação
st.title("Do que a Guta é mais apaixonada?")

# Pergunta para o usuário
resposta = st.selectbox(
    "Escolha uma das opções:",
    ("Selecione uma opção", "moto", "praia", "carro")
)

# Lógica para mostrar a resposta somente após a seleção
if resposta == "moto":
    # Gerar um coração
    t = np.linspace(0, 2 * np.pi, 100)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.set_aspect('equal')
    plt.title("Coração para Guta")
    st.pyplot(fig)  # Exibe o gráfico no Streamlit
    
    # Exibir a frase
    st.write("Você sabe do que eu mais gosto, basta agora perceber o quanto sou apaixonada por você.")
    
elif resposta == "praia":
    st.write("Acho que precisa me conhecer mais")
    
elif resposta == "carro":
    st.write("Até gosto, mas não sou apaixonada, você errou.")
