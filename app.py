from pathlib import Path # para pegar a informação do caminho
import streamlit as st 
from PIL import Image

# Configurações Estruturais:
diretorio = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print(diretorio)
arquivo_css = diretorio / "styles" / "styles.css"
arquivo_pdf = diretorio / "assets" / "curriculo.pdf"
arquivo_imagem = diretorio / "assets" / "foto.jpg"

# Configurações Gerais

titulo = "Curriculo | Mikael Paz e Silva"
nome = "Mikael Paz e Silva"
descricao = """
    Estudante de Engenharia de Controle e Automação
"""
email = "mikaelpazesilva@gmail.com"
midiasocial = {
    "Linkedin":"https://br.linkedin.com/in/mikael-paz-e-silva-243b82213",
    "Github":"https://github.com/Mikael-paz"
}
cursos = {
    "Programação em Python":"https://drive.google.com/drive/folders/12sWT86z_8xvFFWtlyCmJ-4XLKGusVJ4A?usp=drive_link",
    "Curso de inglês Program Access Microscholarship":"https://drive.google.com/drive/folders/12sWT86z_8xvFFWtlyCmJ-4XLKGusVJ4A?usp=drive_link"
}

# Carregando Assets
with open(arquivo_css) as c:
    st.markdown(f"<style>{c.read()}<\style>",unsafe_allow_html=True)

with open(arquivo_pdf, "rb") as arquivo_pdf:
    pdfleitura = arquivo_pdf.read()

image = Image.open(arquivo_imagem)

# Criando Layout
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(image, width=250)
    st.write(" :email: "+email)
    st.subheader("O melhor e mais apto jovem para a sua empresa")
    st.header("Contrate AGORA! :arrow_right: ")

with col2:
    st.title(nome)
    st.subheader(descricao)
    st.download_button(
        label="Download Curriculo", # Nome do botão
        data=pdfleitura, # Arquivo PDF que será baixado
        file_name="Mikael - Curriculo.pdf", # Nome do arquivo quando for baixado
        mime="application/octet-stream" # Não precisa abrir no navegador
    )

# Adicionando Midias Sociais
colunas = st.columns(len(midiasocial))
for indice, (plataforma, link) in enumerate(midiasocial.items()):
    colunas[indice].write(f"[{plataforma}]({link})")

# Adicionando Experiências
st.write("#")
st.subheader("Experiências")
st.write("""
            - 💹 Experiência em Suporte de TI
            - 💹 Experiência em Atendimento ao Cliente
            - 💹 Experiência em Gestão de Pessoas
""")

# Adicionando Habilidades
st.write("#")
st.subheader("Habilidades")
st.write("""
         - 💹 Inglês fluente
         - 💹 Español fluente
         - 💹 Português intermedio
         - 💹 Excel em dia
         - 💹 Python em progresso
""")

# Historico de Trabalho
st.write("#")
st.subheader("Histórico de Trabalho")
st.write("---")

st.write("🧑‍💻","***CEO | Gringo Produções")
st.write("01/2023 - Atual")
st.write("""
        - 💹 Ainda não criei esta empresa, mas queria...
         """)

st.write("🧑‍💻", "TÉCNICO EM TI - INTELLINOTE")
st.write("Abril 2019 à Fevereiro 2020")
st.write("""
        Tem como responsabilidades montagem, acabamento e 
         manutenção de computadores, além da identificação e 
         correção de problemas em aparelhos eletrônicos.
""")

st.write("🧑‍💻", "CONCIERGE BILÍNGUE - DECK PINA BAR")
st.write("Dezembro 2020 à Abril 2021")
st.write("""
        Atendimento aos clientes , conduzindo as mesas orientando 
         sobre a escolha do pratos tirando úvidas do menu prestando 
         informações sobre o local, controlando a entrada/saída dos 
         clientes.
""")

# Cursos
st.write("#")
st.subheader("Cursos")
st.write("---")
for curso,link in cursos.items():
    st.write(f"[{curso},{link}]")