import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os


#config
st.set_page_config(page_title="Joeapp", page_icon="🤖", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
    

def local_css(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, file_name)
    with open(path) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("style/style.css")
email_address ="huerta.joe.0103@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    st.subheader("Hola, bienvenido a Joeapp :wave:")
    st.title("Infraestructura Web.")
    st.write(
        "Esta es una página web para la materia de Infraestructura Web."
    )
    st.write("[Saber más >](https://valerapp.com/)")



# sobre nosotros
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Sobre nosotros")
        st.write(
            """
            Nuestro objetivo es poder aportar valor a los negocios ayudandoles a ahorrar tiempo y dinero a través de la implantación de nuevas tecnologías como la inteligencia artifical, analisis de datos o implantación de software de automatización.
            Seguramente te vamos a poder ayudar si:

            - Tienes un negocio y quieres mejorar tus procesos de trabajo para ahorrar tiempo y dinero
            - Tienes trabajadores que emplean parte de su jornada a realizar tareas repetitivas sin valor añadido para tu negocio
            - No tienes claras las métricas de tu negocio y quieres tomar decisiones basadas en datos
            - Quieres mejorar la experiencia de tus clientes
            - Usas herramientas de software antiguas o poco eficientes o procesos en los que usas papel y bolígrafo

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )
        st.write("[Más sobre nosotros>](https://valerapp.com/about/)")
    with right_column:
        st_lottie(load_lottieurl(lottie_file), height=400)


